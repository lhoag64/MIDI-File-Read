import logging
from utilities.hexdump import HexDump
from utilities.buffer import Buffer

import midi.chunk

#----------------------------------------------------------------------
class File(object):
  filename = None

  #--------------------------------------------------------------------
  def __init__(self, filename=None):
    self.filename = filename
    self.chunkList = None

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

      fp = open(self.filename, "rb")

      trkCnt = 0
      trk = 0
      done = False
      while not done:
        chunk = self.__ReadChunk(fp)
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

    except Exception as exc:
      logging.critical("Exception: " + exc.args)
      fp.close()
      raise Exception("Error reading Midi file")

    fp.close()

    return chunkList

  #--------------------------------------------------------------------
  def __ReadChunk(self, fp):
    chunkType = fp.read(4).decode("utf-8")
    chunkLen = int.from_bytes(fp.read(4), byteorder='big')

    if chunkType == "" and chunkLen == 0:
      chunkData = None
    else:
      chunkData = memoryview(bytearray(chunkLen))
      fp.readinto(chunkData)
      if chunkData.nbytes != chunkLen:
        raise Exception("Read error in MIDI file")

    if chunkType == "MThd":
      chunkObj = midi.chunk.MThd(chunkType, chunkData)
    elif chunkType == "MTrk":
      chunkObj = midi.chunk.MTrk(chunkType, chunkData)
    else:
      chunkObj = None

    return chunkObj

  #--------------------------------------------------------------------
  def __ProcessChunks(self):
    #trkCnt = self.chunkList.GetTrkCnt()
    trkList = self.chunkList.GetTrkList()

    for trk in trkList:
      self.__ProcessTrack(trk)


    logging.debug("")
  
  #--------------------------------------------------------------------
  def __ProcessTrack(self, trk):
    HexDump("Track", trk.cData)

    maxIdx = trk.cData.nbytes
    curIdx = 0

    while curIdx < maxIdx:
      (event, idx) = self.__ProcessEvent(trk.cData, curIdx)

    logging.debug("")

  #--------------------------------------------------------------------
  def __ProcessEvent(self, data, cIdx):
    (lvc, idx) = self.__ReadVLQ(data, cIdx)
    deltaTime = lvc
    cIdx = idx

  #--------------------------------------------------------------------
  def __ReadVLQ(self, data, cIdx):
    idx = cIdx
    val = 0
    while idx < 4:
      buf = data[idx] & 0xff
      idx += 1
      val = (val << 7) + buf
      if buf & 0x80 == 0:
        break

    return (val, idx)
