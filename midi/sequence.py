import logging
import midi.chunk

#----------------------------------------------------------------------
class Sequence(object):

  #--------------------------------------------------------------------
  def __init__(self, filename=None):
    if filename is not None:
      self.__Read(filename)

  #--------------------------------------------------------------------
  def Read(self, filename):
    self.__Read(filename)

  #--------------------------------------------------------------------
  def __Read(self, filename):
    self.chunkList = midi.chunk.ChunkList()

    fp = open(filename, "rb")

    trkCnt = 0
    trk = 0
    done = False
    while not done:
      chunk = self.__ReadChunk(fp)
      if chunk is not None:
        if type(chunk) is midi.chunk.MThd:
          self.chunkList.AddMThd(chunk)
          trkCnt = self.chunkList.GetTrkCnt()
        else:
          self.chunkList.AddMTrk(chunk)
          trk += 1
      else:
        done = True
      
    if trk != trkCnt:
      logging.warning("Mismatch of tracks in MIDI file")

    logging.debug("")

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
