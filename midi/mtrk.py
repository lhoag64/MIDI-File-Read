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

  #--------------------------------------------------------------------
  def ProcessEvents(self, trkNum):

    done = False
    while not done:
      #HexDump("Top of Buffer", self.cData.GetData(), 64)
      event = self.__ParseFileEvent(trkNum, self.cData)
      if event is None:
        done = True

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
#  MetaEventDict = \
#    {
#      0x00 : (0xff, "Sequence Number"),
#      0x01 : (0xff, "Text"),
#      0x02 : (0xff, "Copyright"),
#      0x03 : (0xff, "Track Name"),
#      0x04 : (0xff, "Instrument Name"),
#      0x05 : (0xff, "Lyric"),
#      0x06 : (0xff, "Marker"),
#      0x07 : (0xff, "Cue Point"),
#      0x08 : (0xff, "Program Name"),
#      0x09 : (0xff, "Device Name"),
#      0x20 : (0xff, "MIDI Channel Prefix"),
#      0x21 : (0xff, "MIDI Port"),
#      0x2f : (0xff, "End of Track"),
#      0x51 : (0xff, "Tempo"),
#      0x54 : (0xff, "SMPTE Offset"),
#      0x58 : (0xff, "Time Signature"),
#      0x59 : (0xff, "Key Signature"),
#      0x7f : (0xff, "Sequencer Specific Meta Event")
#    }

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
#  SystemEventDict = \
#    {
#      0x00 : (0xff, "System Exclusive"),
#      0x01 : (0x00, "Undefined"),
#      0x02 : (0x02, "Song Position Pointer"),
#      0x03 : (0x01, "Song Select"),
#      0x04 : (0x00, "Undefined"),
#      0x05 : (0x00, "Undefined"),
#      0x06 : (0x00, "Tune Request"),
#      0x07 : (0x00, "End Or Exclusive"),
#      0x08 : (0x00, "Timeing Clock"),
#      0x09 : (0x00, "Undefined"),
#      0x0a : (0x00, "Start"),
#      0x0b : (0x00, "Continue"),
#      0x0c : (0x00, "Stop"),
#      0x0d : (0x00, "Undefined"),
#      0x0e : (0x00, "Active Sensing"),
#      0x0f : (0x00, "Reset"),
#    }

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

    self.prvSB = sb
    return CreateSystemEvent(trk, dtime, sb, eType, eLen, eData, params[1])

  #--------------------------------------------------------------------
#  MidiEventDict = \
#    {
#      0x08 : (0x02, "Note Off"),
#      0x09 : (0x02, "Note On"),
#      0x0a : (0x02, "Key Pressure"),
#      0x0b : (0x02, "Control Change"),
#      0x0c : (0x01, "Program Change"),
#      0x0d : (0x01, "Channel Pressure"),
#      0x0e : (0x02, "Pitch Wheel"),
#    }

  #----------------------------------------------------------------------
  def __ParseFileMidiEvent(self, trk, data, dtime):
    #sIdx = data.GetIdx()

    sb = data.PeekByte()
    if sb < 0x80:
      sb = self.prvSB
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

    self.prvSB = sb
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