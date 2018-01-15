import logging
import os.path
from utilities.hexdump import HexDump

#----------------------------------------------------------------------
# Chunk Class
#----------------------------------------------------------------------
class Chunk:
  ctype = None
  clen = None
  data = None

  #--------------------------------------------------------------------
  def __init__(self, ctype, clen, data):
    self.ctype = ctype
    self.clen = clen
    self.data = data

#----------------------------------------------------------------------
# SeqHdr Class
#----------------------------------------------------------------------
class SeqHdr:
  fmt = None
  ntrks = None
  division = None

  #--------------------------------------------------------------------
  def __init__(self, chunk):
    logging.debug("Chunk|"+chunk.ctype)
    HexDump("Chunk Data", chunk.data)

#----------------------------------------------------------------------
# SeqTrk Class
#----------------------------------------------------------------------
class SeqTrk:
  #--------------------------------------------------------------------
  def __init__(self, chunk):
    logging.debug("Chunk|"+chunk.ctype)
    HexDump("Chunk Data", chunk.data)

#----------------------------------------------------------------------
# Sequence Class
#----------------------------------------------------------------------
class Sequence:
  hdr = None
  trks = []

  #--------------------------------------------------------------------
  def __init__(self, chunks):
    for chunk in chunks:
      if chunk.ctype == "MThd":
        self.hdr = SeqHdr(chunk)
      elif chunk.ctpe == "MTrk":
        self.trks.append(SeqTrk(chunk))
      else:
        pass

#----------------------------------------------------------------------
# MidiFile Class
#----------------------------------------------------------------------
class MidiFile:
  chunks = []
  data = None
  dataLen = 0
  seq = None

  #--------------------------------------------------------------------
  def __init__(self):
    pass

  #--------------------------------------------------------------------
  def Read(self, filename):

    self.dataLen = os.path.getsize(filename)

    binFile = open(filename, "rb")
    self.data = memoryview(bytearray(self.dataLen))
    binFile.readinto(self.data)
    binFile.close()

    #HexDump("File", self.data[0: 4])
    HexDump("File", self.data[0:34])

    idx = 0
    while (idx < self.dataLen):
      ctxt = bytearray(self.data[idx:idx+4]).decode("utf-8")
      logging.debug(ctxt)
      idx += 4
      clen = int.from_bytes(self.data[idx:idx+4], byteorder="big")
      idx += 4
      logging.debug(str(clen))
      self.chunks.append(Chunk(ctxt, clen, self.data[idx:idx+clen]))
      text = "Data["+str(idx)+":"+str(idx+clen)+"]"
      HexDump(text, self.data[idx:idx+clen])
      idx += clen

    self.seq = Sequence(self.chunks)

    logging.debug("file read")
