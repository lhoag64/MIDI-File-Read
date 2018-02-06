import logging
from utilities.buffer import Buffer

#----------------------------------------------------------------------
class ChunkList(object):

  #--------------------------------------------------------------------
  def __init__(self):
    self.hdr = None
    self.trkList = None

  #--------------------------------------------------------------------
  def AddMThd(self, mThd):
    if self.hdr == None:
      self.hdr = mThd
    else:
      raise Exception("Corrupt MIDI file - More than one MHdr")

  #--------------------------------------------------------------------
  def AddMTrk(self, mTrk):
    if self.trkList is None:
      self.trkList = []
    if type(mTrk) is MTrk:
      self.trkList.append(mTrk)
    else:
      raise Exception("Corrupt MIDI file - expecting MTrk")

  #--------------------------------------------------------------------
  def GetTrkCnt(self):
    return self.hdr.cTrks

  #--------------------------------------------------------------------
  def GetTrkList(self):
    return self.trkList

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
    if cData.dCnt != 6:
      raise Exception("Invalid MThd size")

    super().__init__()
    self.cType = cType
    self.cData = cData
    self.cFmt = cData.ReadShort()
    self.cTrks = cData.ReadShort()
    self.cDiv = cData.ReadShort()

#----------------------------------------------------------------------
class MTrk(Chunk):

  #--------------------------------------------------------------------
  def __init__(self,cType, cData):
    super().__init__()
    self.cType = cType
    self.cData = cData



