import logging

#----------------------------------------------------------------------
class ChunkList(object):
  hdr = None
  trkList = None

  def AddMThd(self, mThd):
    if self.hdr == None:
      self.hdr = mThd
    else:
      raise Exception("Corrupt MIDI file - More than one MHdr")

  def AddMTrk(self, mTrk):
    if self.trkList is None:
      self.trkList = []
    if type(mTrk) is MTrk:
      self.trkList.append(mTrk)
    else:
      raise Exception("Corrupt MIDI file - expecting MTrk")

  def GetTrkCnt(self):
    return self.hdr.cTrks

#----------------------------------------------------------------------
class Chunk(object):

  #--------------------------------------------------------------------
  def __init__(self):
    self.cType = None
    self.cData = None

#----------------------------------------------------------------------
class MThd(Chunk):

  #--------------------------------------------------------------------
  def __init__(self,cType, cData):
    if cData.nbytes != 6:
      raise Exception("Invalid MThd size")

    super().__init__()
    self.cType = cType
    self.cData = cData
    self.cFmt = int.from_bytes(self.cData[0:2], byteorder="big")
    self.cTrks = int.from_bytes(self.cData[2:4], byteorder="big")
    self.cDiv = int.from_bytes(self.cData[4:6], byteorder="big")

#----------------------------------------------------------------------
class MTrk(Chunk):

  #--------------------------------------------------------------------
  def __init__(self,cType, cData):
    super().__init__()
    self.cType = cType
    self.cData = cData



