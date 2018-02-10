import logging
from utilities.hexdump import HexDump

from midi.systemevent import SystemEventDict
from midi.systemevent import CreateSystemEvent
from midi.metaevent import MetaEventDict
from midi.metaevent import CreateMetaEvent
from midi.midievent import MidiEventDict
from midi.midievent import CreateMidiEvent

#----------------------------------------------------------------------
class MTrk(object):

  #--------------------------------------------------------------------
  def __init__(self, cType, cData):
    self.cType = cType
    self.cData = cData
    self.prvSb = 0xff
    self.eventList = []

  #--------------------------------------------------------------------
  def ProcessEvents(self, trkNum):

    done = False
    while not done:
      #HexDump("Top of Buffer", self.cData.GetData(), 64)
      event = self.__ParseFileEvent(trkNum, self.cData)
      if event is None:
        done = True
      else:
        self.eventList.append(event)

    logging.debug("")

  #--------------------------------------------------------------------
  def __ParseFileEvent(self, trkNum, data):

    if data.EOB():
      return None

    dTime = self.__ReadVLQ(data)
    sByte = data.PeekByte()

    event = None
    if sByte == 0xff:
      event = self.__ParseFileMetaEvent(trkNum, data, dTime)
    elif (sByte & 0xf0) == 0xf0:
      event = self.__ParseFileSystemEvent(trkNum, data, dTime)
    else:
      event = self.__ParseFileMidiEvent(trkNum, data, dTime)

    logging.debug(event)
    return event

  #--------------------------------------------------------------------
  def __ParseFileMetaEvent(self, trk, data, dtime):
    #sIdx = data.GetIdx()

    sb = data.ReadByte()
    if (sb == 0xff):
      eType = data.ReadByte()

    params = MetaEventDict[eType]

    if params[0] == 0xff:
      eLen = self.__ReadVLQ(data)
    else:
      eLen = params[0]
    eData = data.ReadBytes(eLen)

    #eIdx = data.GetIdx()
    #rawData = data.Slice(sIdx, eIdx - sIdx)
    #HexDump(params[1], rawData)

    self.prvSb = sb
    return CreateMetaEvent(trk, dtime, sb, eType, eLen, eData, params[1])

  #--------------------------------------------------------------------
  def __ParseFileSystemEvent(self, trk, data, dtime):
    #sIdx = data.GetIdx()

    sb = data.ReadByte()
    eType = sb & 0x0f

    params = SystemEventDict[eType]

    if params[0] == 0xff:
      eLen = self.__ReadVLQ(data)
    else:
      eLen = params[0]
    eData = data.ReadBytes(eLen)

    #eIdx = data.GetIdx()
    #rawData = data.Slice(sIdx, eIdx - sIdx)
    #HexDump(params[1], rawData)

    self.prvSb = sb
    return CreateSystemEvent(trk, dtime, sb, eType, eLen, eData, params[1])

  #----------------------------------------------------------------------
  def __ParseFileMidiEvent(self, trk, data, dtime):
    #sIdx = data.GetIdx()

    sb = data.PeekByte()
    if sb < 0x80:
      sb = self.prvSb
    else:
      sb = data.ReadByte()

    eType = (sb & 0xf0) >> 4
    #chan = sb & 0x0f

    params = MidiEventDict[eType]

    eLen = params[0]
    eData = data.ReadBytes(eLen)

    #eIdx = data.GetIdx()
    #rawData = data.Slice(sIdx, eIdx - sIdx)
    #HexDump(params[1], rawData)

    self.prvSb = sb
    return CreateMidiEvent(trk, dtime, sb, eType, eLen, eData, params[1])

  #--------------------------------------------------------------------
  def __ReadVLQ(self, data):

    val = 0
    while True:
      buf = data.ReadByte()
      val = (val << 7) + buf
      if buf & 0x80 == 0:
        break

    return val