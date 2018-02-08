#import logging
#from enum import Enum
#from utilities.buffer import Buffer
#
##----------------------------------------------------------------------
#class FileEventType:
#  META = 0xff
#  SYSTEM = 0xffff
#  MIDI   = 0x01
#
##----------------------------------------------------------------------
#prvSB = 0xff
#
#def ParseFileEvent(data):
#
#  if data.EOB():
#    return None
#
#  dtime = ReadVLQ(data)
#  sbyte = data.PeekByte()
#
#  event = None
#  if sbyte == 0xff:
#    event = ParseFileMetaEvent(data, dtime, sbyte)
#  elif sbyte & 0xf0 == 0xf0:
#    event = ParseFileSystemEvent(data, dtime, sbyte)
#  else:
#    event = ParseFileMidiEvent(data, dtime, sbyte)
#
#  return event
#
##----------------------------------------------------------------------
#MetaEventDict = \
#  {
#    0x00 : (0x8000, "Sequence Number"),
#    0x01 : (0x8000, "Text"),
#    0x02 : (0x8000, "Copyright"),
#    0x03 : (0x8000, "Track Name"),
#    0x04 : (0x8000, "Instrument Name"),
#    0x05 : (0x8000, "Lyric"),
#    0x06 : (0x8000, "Marker"),
#    0x07 : (0x8000, "Cue Point"),
#    0x08 : (0x8000, "Program Name"),
#    0x09 : (0x8000, "Device Name"),
#    0x20 : (0x8000, "MIDI Channel Prefix"),
#    0x21 : (0x8000, "MIDI Port"),
#    0x2f : (0x8000, "End of Track"),
#    0x51 : (0x8000, "Tempo"),
#    0x54 : (0x8000, "SMPTE Offset"),
#    0x58 : (0x8000, "Time Signature"),
#    0x59 : (0x8000, "Key Signature"),
#    0x2f : (0x8000, "End of Track"),
#    0x7f : (0x8000, "Sequencer Specific Meta Event")
#  }
##----------------------------------------------------------------------
#def ParseFileMetaEvent(data, dtime, sbyte):
#  global prvSB
#  sIdx = data.GetIdx()
#  sb = data.ReadByte()
#  if (sb == 0xff):
#    sb = data.ReadByte()
#  eType = (sb & 0x7f, sb & 0x80)
#  params = MetaEventDict[eType[0]]
#  if params[0] == 0x8000:
#    eLen = data.ReadByte()
#  else:
#    eLen = 0
#  eData = data.ReadBytes(eLen)
#  eIdx = data.GetIdx()
#
#  rawData = data.Slice(sIdx, eIdx - sIdx)
#
#  prvSB = sb
#  return (params[1], rawData, eData)
#
##----------------------------------------------------------------------
#SystemEventDict = \
#  {
#    0x00 : (0xffff, "System Exclusive"),
#    0x01 : (0x0000, "Undefined"),
#    0x02 : (0x0002, "Song Position Pointer"),
#    0x03 : (0x0001, "Song Select"),
#    0x04 : (0x0000, "Undefined"),
#    0x05 : (0x0000, "Undefined"),
#    0x06 : (0x0000, "Tune Request"),
#    0x07 : (0x0000, "End Or Exclusive"),
#    0x08 : (0x0000, "Timeing Clock"),
#    0x09 : (0x0000, "Undefined"),
#    0x0a : (0x0000, "Start"),
#    0x0b : (0x0000, "Continue"),
#    0x0c : (0x0000, "Stop"),
#    0x0d : (0x0000, "Undefined"),
#    0x0e : (0x0000, "Active Sensing"),
#    0x0f : (0x0000, "Reset"),
#  }
##----------------------------------------------------------------------
#def ParseFileSystemEvent(data, dtime, sbyte):
#  global prvSB
#  sIdx = data.GetIdx()
#  sb = data.ReadByte()
#  eType = (sb & 0x0f, sb & 0xf0)
#  params = SystemEventDict[eType[0]]
#  if params[0] == 0xffff:
#    eLen = ReadVLQ(data)
#  else:
#    eLen = params[0]
#  eData = data.ReadBytes(eLen)
#  eIdx = data.GetIdx()
#
#  rawData = data.Slice(sIdx, eIdx - sIdx)
#
#  prvSB = sb
#  return (params[1], rawData, eData)
#
##----------------------------------------------------------------------
#MidiEventDict = \
#  {
#    0x80 : (0x0002, "Note Off"),
#    0x90 : (0x0002, "Note On"),
#    0xa0 : (0x0002, "Key Pressure"),
#    0xb0 : (0x0002, "Control Change"),
#    0xc0 : (0x0001, "Program Change"),
#    0xd0 : (0x0001, "Channel Pressure"),
#    0xe0 : (0x0002, "Pitch Wheel"),
#  }
##----------------------------------------------------------------------
#def ParseFileMidiEvent(data, dtime, sbype):
#  global prvSB
#  sIdx = data.GetIdx()
#  sb = data.PeekByte()
#  if sb < 0x80:
#    sb = prvSB
#  else:
#    sb = data.ReadByte()
#  eType = (sb & 0x0f, sb & 0xf0)
#  params = MidiEventDict[eType[1]]
#  eLen = params[0]
#  eData = data.ReadBytes(eLen)
#  eIdx = data.GetIdx()
#
#  rawData = data.Slice(sIdx, eIdx - sIdx)
#
#  prvSB = sb
#  return (params[1], rawData, eData)
#
##--------------------------------------------------------------------
#def ReadVLQ(data):
#
#  val = 0
#  while True:
#    buf = data.ReadByte()
#    val = (val << 7) + buf
#    if buf & 0x80 == 0:
#      break
#
#  return val
#
#
#
## <MThd Chunk> = <MThd><Fmt><Track Cnt><Divsion> (16-bit values)
## <MTrk Chunk> = <MTrk><len><MTrk Event>+
# <MTrak Event> = <delta-time(VLQ)><Event>
# <delta-time> = variable-lenght-quantity (VLQ)
# <Event> = <MIDI Event>|<Sysex Event>|<Meta Event>
# <MIDI Event>
# <Sysex Event> = <FO><len(VLQ)><bytes>|<F7><len(VLQ)><bytes>
# <Meta Event> = <FF><type><len><bytes>

# Meta Events
# FF 00 02 SeqNum
# FF 01 len text Event
# FF 02 len text Copyright Notice
# FF 03 len text Sequence/Track Name
# FF 04 len text Instrument Name
# FF 05 len text Lyric
# FF 06 len text Marker
# FF 07 len text Cue Point
# FF 20 01 cc MIDI Channel Prefix
# FF 2F 00 End of Track
# FF 51 02 tttttt Set Tempo
# FF 54 05 hr mn se fr ff SMPTE Offset
# FF 58 04 nn dd cc bb Time Signature
# FF 59 02 sf mi Key Signature
# FF 7F len data Sequencer Specific Meta-Event
# MIDI Events
