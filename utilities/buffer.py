import logging

#----------------------------------------------------------------------
class Buffer(object):
  data = None
  dLen = None
  cIdx = None

  #--------------------------------------------------------------------
  def __init__(self, len, fp=None):
    self.dLen = len
    self.data = memoryview(bytearray(len))
    if fp is not None:
      fp.readinto(self.data)
    self.cIdx = 0

  #--------------------------------------------------------------------
  def ReadFileInto(self, fp):
      fp.readinto(self.data)

  #--------------------------------------------------------------------
  def ReadByte(self):
    if self.cIdx >= self.dLen:
      raise Exception("Attempt to read past end of buffer")

    val = self.data[self.cIdx]
    self.cIdx += 1

    return val
  
  #--------------------------------------------------------------------
  def ReadShort(self):
    if (self.cIdx + 2) >= self.dLen:
      raise Exception("Attempt to read past end of buffer")

    val = self.data[self.cIdx]
    self.cIdx += 2

    return val
  
  #--------------------------------------------------------------------
  def ReadInt(self):
    if (self.cIdx + 4) >= self.dLen:
      raise Exception("Attempt to read past end of buffer")

    val = self.data[self.cIdx]
    self.cIdx += 4

    return val
  
  #--------------------------------------------------------------------
  def ReadLong(self):
    if (self.cIdx + 8) >= self.dLen:
      raise Exception("Attempt to read past end of buffer")

    val = self.data[self.cIdx]
    self.cIdx += 8

    return val