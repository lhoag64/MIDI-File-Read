import logging

#----------------------------------------------------------------------
class Buffer(object):
  bufferCnt = 0

  #--------------------------------------------------------------------
  def __init__(self, obj=None, cnt=None):
    Buffer.bufferCnt += 1
    self.bufId = Buffer.bufferCnt
    self.dCnt = cnt
    self.bLen = cnt
    if cnt is not None:
      self.data = memoryview(bytearray(cnt))
    else:
      self.data = None
    self.cIdx = 0
    logging.debug('created buffer ' + str(self.bufId))

  #--------------------------------------------------------------------
  def __del__(self, obj=None, cnt=None):
    logging.debug("deleting buffer " + str(self.bufId))
    if self.data is not None:
      self.data.release()
    Buffer.bufferCnt -= 1

  #--------------------------------------------------------------------
  def GetDataCnt(self):
    return self.dCnt

  #--------------------------------------------------------------------
  def GetData(self):
    return self.data[self.cIdx:]


  #--------------------------------------------------------------------
  #def __getitem(self):
  #  return self

  #--------------------------------------------------------------------
  def ReadFileInto(self, fp, cnt):
      if self.data is not None:
        self.data.release()
      self.data = memoryview(bytearray(cnt))
      self.dCnt = cnt
      self.bLen = cnt
      fp.readinto(self.data)

  #--------------------------------------------------------------------
  def ReadBufferInto(self, buffer, cnt):
      if self.data is not None:
        self.data.release()
      self.dCnt = cnt
      self.bLen = cnt
      self.data = buffer.ReadBytes(cnt)

  #--------------------------------------------------------------------
  def Copy(self, cnt):
    pass

  #--------------------------------------------------------------------
  def GetIdx(self):
    return self.cIdx

  #--------------------------------------------------------------------
  def Rewind(self, cnt):
    if (self.cIdx - cnt) > 0:
      self.cIdx -= cnt
    else:
      raise Exception("Attempt to Rewind Buffer before start")
  
  #--------------------------------------------------------------------
  def EOB(self):
    return self.cIdx == self.bLen

  #--------------------------------------------------------------------
  def Slice(self, startIdx=None, cnt=None):
    if startIdx is None:
      sIdx = self.cIdx
    else:
      sIdx = startIdx
    
    if cnt is None:
      eIdx = self.bLen
    else:
      eIdx = sIdx + cnt

    return self.data[sIdx:eIdx]

  #--------------------------------------------------------------------
  def ReadString(self, cnt):
    val = None
    if self.dCnt != 0 and self.cIdx + cnt <= self.bLen:
      val = bytearray(self.data[self.cIdx:self.cIdx + cnt]).decode("utf-8")
      self.cIdx += cnt
      self.dCnt -= cnt
    return val

  #--------------------------------------------------------------------
  def ReadBytes(self, cnt):
    val = None
    if self.dCnt != 0 and self.cIdx + cnt <= self.bLen:
      val = self.data[self.cIdx:self.cIdx + cnt]
      self.cIdx += cnt
      self.dCnt -= cnt
    return val

  #--------------------------------------------------------------------
  def ReadByte(self):
    return self.__ReadNum(1)
  
  #--------------------------------------------------------------------
  def ReadShort(self):
    return self.__ReadNum(2)

  #--------------------------------------------------------------------
  def ReadInt(self):
    return self.__ReadNum(4)

  #--------------------------------------------------------------------
  def ReadLong(self):
    return self.__ReadNum(8)

  #--------------------------------------------------------------------
  def __ReadNum(self, cnt):
    val = None
    if self.dCnt != 0 and self.cIdx + cnt <= self.bLen:
      val = int.from_bytes(self.data[self.cIdx:self.cIdx + cnt], byteorder="big")
      self.cIdx += cnt
      self.dCnt -= cnt
    return val

  #--------------------------------------------------------------------
  def PeekByte(self):
    return self.__PeekNum(1)
  
  #--------------------------------------------------------------------
  def PeekShort(self):
    return self.__PeekNum(2)

  #--------------------------------------------------------------------
  def PeekInt(self):
    return self.__PeekNum(4)

  #--------------------------------------------------------------------
  def PeekLong(self):
    return self.__PeekNum(8)

  #--------------------------------------------------------------------
  def __PeekNum(self, cnt):
    val = None
    if self.dCnt != 0 and self.cIdx + cnt <= self.bLen:
      val = int.from_bytes(self.data[self.cIdx:self.cIdx + cnt], byteorder="big")
    return val
