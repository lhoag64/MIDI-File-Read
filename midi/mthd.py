import logging
from utilities.buffer import Buffer

from midi.timing import PPQN
from midi.timing import SMPTE

#----------------------------------------------------------------------
class MThd(object):

  #--------------------------------------------------------------------
  def __init__(self, cType, cData):
    if cData.dCnt != 6:
      raise Exception("Invalid MThd size")

    self.cType = cType
    self.cFmt = cData.ReadShort()
    self.cTrkCnt = cData.ReadShort()
    cDiv = cData.ReadShort()
    if cDiv & 0x80:
      self.timing = PPQN(cDiv)
    else:
      self.timing = SMPTE(cDiv)

  #--------------------------------------------------------------------
  def GetTrkCnt(self):
    return self.cTrkCnt
  
  #--------------------------------------------------------------------
  def GetTiming(self):
    return self.cTrkCnt