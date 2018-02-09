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
