import logging
import os.path
#from utilities.hexdump import HexDump
from utilities.buffer import Buffer

from midi.mthd import MThd
from midi.mtrk import MTrk

#----------------------------------------------------------------------
class File(object):

  #--------------------------------------------------------------------
  def __init__(self, filename=None):
    self.filename = filename
    self.buffer = None

  #--------------------------------------------------------------------
  def Read(self, filename=None):

    if filename is not None:
      self.filename = filename

    if self.filename is None:
      raise Exception("Invalid Midi file name")

    try:
      fileSize = os.path.getsize(self.filename)
      fp = open(self.filename, "rb")
      self.buffer = Buffer()
      self.buffer.ReadFileInto(fp, fileSize)
    except Exception as exc:
      logging.critical("Exception: " + exc.args[0])
      fp.close()
      raise Exception("Error reading Midi file")

    fp.close()

    trkCnt = 0
    trk = 0
    mThd = None
    mTrkList = []
    done = False
    while not done:
      chunk = self.__Read(self.buffer)
      if chunk is None:
        done = True
      else:
        if type(chunk) is MThd:
          mThd = chunk
          trkCnt = mThd.GetTrkCnt()
        elif type(chunk) is MTrk:
          mTrkList.append(chunk)
          trk += 1
        else:
          Exception("Unknown chunk in Midi file")

    if trk != trkCnt:
      Exception("Mismatch of tracks in MIDI file")

    trk = 1
    trkList = []
    for mTrk in mTrkList:
      trkList.append(mTrk.ProcessEvents(trk))
      trk += 1

    return (mThd.GetTiming(), trkList)

  #----------------------------------------------------------------------
  def __Read(self, buffer):
    cType = buffer.ReadString(4)
    cLen = buffer.ReadInt()

    chunk = None
    if cLen is not None:
      cData = Buffer()
      cData.ReadBufferInto(buffer, cLen)

      if cType == "MThd":
        chunk = MThd(cType, cData)
      else:
        chunk = MTrk(cType, cData)
    
    return chunk





  #--------------------------------------------------------------------
#  def __ReadChunk(self, buffer):
#    chunkType = buffer.ReadString(4)
#    chunkLen = buffer.ReadInt()
#    if chunkLen is not None:
#      chunkData = Buffer()
#      chunkData.ReadBufferInto(buffer, chunkLen)
#
#    if chunkType == "MThd":
#      chunkObj = midi.chunk.MThd(chunkType, chunkData)
#    elif chunkType == "MTrk":
#      chunkObj = midi.chunk.MTrk(chunkType, chunkData)
#    else:
#      chunkObj = None
#
#    return chunkObj

  #--------------------------------------------------------------------
#  def __ProcessChunks(self):
#    trkList = self.chunkList.GetTrkList()
#
#    for trk in trkList:
#      self.__ProcessTrack(trk)
#
#
#    logging.debug("")
  
  #--------------------------------------------------------------------
#  def __ProcessTrack(self, trk):
#
#    eventList = []
#    done = False
#    while not done:
#      HexDump("Track", trk.cData.GetData())
#      event = midi.events.ParseFileEvent(trk.cData)
#      if event == None:
#        done = True
#      else:
#        eventList.append(event)
#        HexDump(event[0],event[1])
#        HexDump("MsgData",event[2])
#
#    logging.debug("")

#  #--------------------------------------------------------------------
#  def __ProcessEvent(self, data):
#    lvc = self.__ReadVLQ(data)
#    val = data.PeekByte()
#    if (val == 0xFF):
#      event = midi.event.MetaEvent(data, lvc)
#    elif (val == 0xF0):
#      event = midi.event.SysexEvent(data, lvc)
#    else:
#      event = midi.event.MidiEvent(data, lvc)
#
#    return event
#
#  #--------------------------------------------------------------------
#  def __ReadVLQ(self, data):
#
#    val = 0
#    while True:
#      buf = data.ReadByte()
#      val = (val << 7) + buf
#      if buf & 0x80 == 0:
#        break
#
#    return val
#