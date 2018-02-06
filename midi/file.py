import logging
import os.path
from utilities.hexdump import HexDump
from utilities.buffer import Buffer

import midi.chunk
import midi.events

#----------------------------------------------------------------------
class File(object):

  #--------------------------------------------------------------------
  def __init__(self, filename=None):
    self.filename = filename
    self.chunkList = None
    self.buffer = None

  #--------------------------------------------------------------------
  def Read(self, filename=None):
    self.chunkList = self.__Read(filename)
    self.__ProcessChunks()

  #--------------------------------------------------------------------
  def __Read(self, filename=None):

    if filename is not None:
      self.filename = filename

    if self.filename is None:
      raise Exception("Invalid Midi file name")

    chunkList = midi.chunk.ChunkList()

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
    done = False
    while not done:
      chunk = self.__ReadChunk(self.buffer)
      if chunk is not None:
        if type(chunk) is midi.chunk.MThd:
          chunkList.AddMThd(chunk)
          trkCnt = chunkList.GetTrkCnt()
        else:
          chunkList.AddMTrk(chunk)
          trk += 1
      else:
        done = True

    if trk != trkCnt:
      logging.warning("Mismatch of tracks in MIDI file")

    return chunkList

  #--------------------------------------------------------------------
  def __ReadChunk(self, buffer):
    chunkType = buffer.ReadString(4)
    chunkLen = buffer.ReadInt()
    if chunkLen is not None:
      chunkData = Buffer()
      chunkData.ReadBufferInto(buffer, chunkLen)

    if chunkType == "MThd":
      chunkObj = midi.chunk.MThd(chunkType, chunkData)
    elif chunkType == "MTrk":
      chunkObj = midi.chunk.MTrk(chunkType, chunkData)
    else:
      chunkObj = None

    return chunkObj

  #--------------------------------------------------------------------
  def __ProcessChunks(self):
    trkList = self.chunkList.GetTrkList()

    for trk in trkList:
      self.__ProcessTrack(trk)


    logging.debug("")
  
  #--------------------------------------------------------------------
  def __ProcessTrack(self, trk):

    eventList = []
    done = False
    while not done:
      HexDump("Track", trk.cData.GetData())
      event = midi.events.ParseFileEvent(trk.cData)
      if event == None:
        done = True
      else:
        eventList.append(event)
        HexDump(event[0],event[1])
        HexDump("MsgData",event[2])

    logging.debug("")

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