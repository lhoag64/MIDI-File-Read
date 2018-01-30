import logging
import os.path
from utilities.hexdump import HexDump

#----------------------------------------------------------------------
# MHdr Class
#---
# Data related to a MHdr
#----------------------------------------------------------------------
class MHdr:
  fmt = None
  ntrks = None
  division = None

  #--------------------------------------------------------------------
  def __init__(self, chunk):
    logging.debug("Chunk|"+chunk.ctype)
    HexDump("Chunk Data", chunk.data)
    self.fmt = int.from_bytes(chunk.data[0:2], byteorder="big")
    self.ntrks = int.from_bytes(chunk.data[2:4], byteorder="big")
    self.division = int.from_bytes(chunk.data[4:6], byteorder="big")

#----------------------------------------------------------------------
class MTrkEvent:
  deltaTime = None
  event = None

#----------------------------------------------------------------------
class Sysex:
  sLen = None
  sData = None

#----------------------------------------------------------------------
class MetaEvent:
  eType = None
  eLen = None
  eData = None

#----------------------------------------------------------------------
class MidiEvent:
  sByte = None

#----------------------------------------------------------------------
# MTrk Class
#----------------------------------------------------------------------
class MTrk:
  #--------------------------------------------------------------------
  def __init__(self, chunk):
    logging.debug("Chunk|"+chunk.ctype)
    HexDump("Chunk Data", chunk.data[0:32])
    clen = chunk.data.nbytes
    cidx = 0
    while cidx < clen:
      #----------------------------------------------------------------
      # Read Delta-Time
      #----------------------------------------------------------------
      idx = cidx
      val = 0
      while idx < 4:
        buf = chunk.data[idx] & 0xff
        idx += 1
        val = (val << 7) + buf
        if (buf & 0x80) == 0:
          break
      deltaTime = val
      cidx += idx

      #----------------------------------------------------------------
      # Read type - Sysex (F0), Meta (FF), Midi
      #----------------------------------------------------------------
      buf = chunk.data[cidx] & 0xff
      cidx += 1
      if buf == 0xff:
        evtType = "Meta"
        mevtType = chunk.data[cidx] & 0xff
        cidx += 1
        mevtLen = chunk.data[cidx] & 0xff
        cidx += 1
        cidx +=1 mevtLen




#----------------------------------------------------------------------
# Chunk Class
#---
# A chunk in a MIDI file.  Either a MHdr or MTrk
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
# MidiSeq Class
#---
# Header data and parsed track data
#----------------------------------------------------------------------
class MidiSeq:
  hdr = None
  trks = []

  #--------------------------------------------------------------------
  def __init__(self, chunks):
    for chunk in chunks:
      if chunk.ctype == "MThd":
        self.hdr = MHdr(chunk)
      elif chunk.ctype == "MTrk":
        self.trks.append(MTrk(chunk))
      else:
        pass

#----------------------------------------------------------------------
# MidiFile Class
#---
# Reads a MIDI file into memory and parses it into its compenent parts.
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
