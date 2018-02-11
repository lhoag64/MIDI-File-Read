import logging

from midi.event import Event

#--------------------------------------------------------------------
MetaEventDict = \
  {
    0x00 : (0xff, "Sequence Number"),
    0x01 : (0xff, "Text"),
    0x02 : (0xff, "Copyright"),
    0x03 : (0xff, "Track Name"),
    0x04 : (0xff, "Instrument Name"),
    0x05 : (0xff, "Lyric"),
    0x06 : (0xff, "Marker"),
    0x07 : (0xff, "Cue Point"),
    0x08 : (0xff, "Program Name"),
    0x09 : (0xff, "Device Name"),
    0x20 : (0xff, "MIDI Channel Prefix"),
    0x21 : (0xff, "MIDI Port"),
    0x2f : (0xff, "End of Track"),
    0x51 : (0xff, "Tempo"),
    0x54 : (0xff, "SMPTE Offset"),
    0x58 : (0xff, "Time Signature"),
    0x59 : (0xff, "Key Signature"),
    0x7f : (0xff, "Sequencer Specific Meta Event")
  }

#----------------------------------------------------------------------
def CreateMetaEvent(trk, dtime, sb, etype, elen, edata, name):
  event = None

  if etype == 0x00:
    event = MetaSeqNum(trk, dtime, sb, etype, elen, edata, name)
  elif etype == 0x01:
    event = MetaText(trk, dtime, sb, etype, elen, edata, name)
  elif etype == 0x02:
    event = MetaCopyright(trk, dtime, sb, etype, elen, edata, name)
  elif etype == 0x03:
    event = MetaTrackName(trk, dtime, sb, etype, elen, edata, name)
  elif etype == 0x04:
    event = MetaInstrumentName(trk, dtime, sb, etype, elen, edata, name)
  elif etype == 0x05:
    event = MetaLyric(trk, dtime, sb, etype, elen, edata, name)
  elif etype == 0x06:
    event = MetaMarker(trk, dtime, sb, etype, elen, edata, name)
  elif etype == 0x07:
    event = MetaCuePoint(trk, dtime, sb, etype, elen, edata, name)
  elif etype == 0x08:
    event = MetaProgramName(trk, dtime, sb, etype, elen, edata, name)
  elif etype == 0x09:
    event = MetaDeviceName(trk, dtime, sb, etype, elen, edata, name)
  elif etype == 0x20:
    event = MetaMidiChannelPrefix(trk, dtime, sb, etype, elen, edata, name)
  elif etype == 0x21:
    event = MetaMidiPort(trk, dtime, sb, etype, elen, edata, name)
  elif etype == 0x2f:
    event = MetaEndOfTrack(trk, dtime, sb, etype, elen, edata, name)
  elif etype == 0x51:
    event = MetaTempo(trk, dtime, sb, etype, elen, edata, name)
  elif etype == 0x54:
    event = MetaSmpteOffset(trk, dtime, sb, etype, elen, edata, name)
  elif etype == 0x58:
    event = MetaTimeSignature(trk, dtime, sb, etype, elen, edata, name)
  elif etype == 0x59:
    event = MetaKeySignature(trk, dtime, sb, etype, elen, edata, name)
  elif etype == 0x7f:
    event = MetaSequencerData(trk, dtime, sb, etype, elen, edata, name)
  else:
    Exception("Unknown Meta Event type")

  return event


#----------------------------------------------------------------------
class MetaEvent(Event):

  #--------------------------------------------------------------------
  def __init__(self, trk, dtime, sb, etype, elen, edata, name):
    super().__init__(trk, dtime, sb, etype, elen, edata, name)

  #--------------------------------------------------------------------
#  def __repr__(self):

#----------------------------------------------------------------------
class MetaSeqNum(MetaEvent):

  #--------------------------------------------------------------------
  def __init__(self, trk, dtime, sb, etype, elen, edata, name):
    super().__init__(trk, dtime, sb, etype, elen, edata, name)

  #--------------------------------------------------------------------
#  def __repr__(self):
#    pass

#----------------------------------------------------------------------
class MetaText(MetaEvent):

  #--------------------------------------------------------------------
  def __init__(self, trk, dtime, sb, etype, elen, edata, name):
    super().__init__(trk, dtime, sb, etype, elen, edata, name)
    if self.data is not None:
      self.text = self.data.decode("utf-8")
    else:
      self.text = None

  #--------------------------------------------------------------------
#  def __repr__(self):
#    super().__repr__()
#    logging.debug(self.text)

#----------------------------------------------------------------------
class MetaCopyright(MetaEvent):

  #--------------------------------------------------------------------
  def __init__(self, trk, dtime, sb, etype, elen, edata, name):
    super().__init__(trk, dtime, sb, etype, elen, edata, name)
    if self.data is not None:
      self.text = self.data.decode("utf-8")
    else:
      self.text = None

  #--------------------------------------------------------------------
  def __repr__(self):
    s = "|META|"
    s += "{:2d}".format(self.trk) + "|"
    s += "{:08x}".format(self.dtime) + "|"
    s += "{:<40s}".format(self.name) + "|"
    if self.text is not None:
      s += "\n"
      s += "{:>27s}".format("|  ")
      s += "{:s}".format(self.text) + "|"
    return s

#----------------------------------------------------------------------
class MetaTrackName(MetaEvent):

  #--------------------------------------------------------------------
  def __init__(self, trk, dtime, sb, etype, elen, edata, name):
    super().__init__(trk, dtime, sb, etype, elen, edata, name)
    if self.data is not None:
      self.text = self.data.decode("utf-8")
    else:
      self.text = None

  #--------------------------------------------------------------------
  def __repr__(self):
    s = "|META|"
    s += "{:2d}".format(self.trk) + "|"
    s += "{:08x}".format(self.dtime) + "|"
    s += "{:<40s}".format(self.name) + "|"
    if self.text is not None:
      s += "\n"
      s += "{:>27s}".format("|  ")
      s += "{:s}".format(self.text) + "|"
    return s

#----------------------------------------------------------------------
class MetaInstrumentName(MetaEvent):

  #--------------------------------------------------------------------
  def __init__(self, trk, dtime, sb, etype, elen, edata, name):
    super().__init__(trk, dtime, sb, etype, elen, edata, name)
    if self.data is not None:
      self.text = self.data.decode("utf-8")
    else:
      self.text = None

  #--------------------------------------------------------------------
  def __repr__(self):
    s = "|META|"
    s += "{:2d}".format(self.trk) + "|"
    s += "{:08x}".format(self.dtime) + "|"
    s += "{:<40s}".format(self.name) + "|"
    if self.text is not None:
      s += "\n"
      s += "{:>27s}".format("|  ")
      s += "{:s}".format(self.text) + "|"
    return s

#----------------------------------------------------------------------
class MetaLyric(MetaEvent):

  #--------------------------------------------------------------------
  def __init__(self, trk, dtime, sb, etype, elen, edata, name):
    super().__init__(trk, dtime, sb, etype, elen, edata, name)
    if self.data is not None:
      self.text = self.data.decode("utf-8")
    else:
      self.text = None
  
  #--------------------------------------------------------------------
  def __repr__(self):
    s = "|META|"
    s += "{:2d}".format(self.trk) + "|"
    s += "{:08x}".format(self.dtime) + "|"
    s += "{:<40s}".format(self.name) + "|"
    if self.text is not None:
      s += "\n"
      s += "{:>27s}".format("|  ")
      s += "{:s}".format(self.text) + "|"
    return s

#----------------------------------------------------------------------
class MetaMarker(MetaEvent):

  #--------------------------------------------------------------------
  def __init__(self, trk, dtime, sb, etype, elen, edata, name):
    super().__init__(trk, dtime, sb, etype, elen, edata, name)
    if self.data is not None:
      self.text = self.data.decode("utf-8")
    else:
      self.text = None

  #--------------------------------------------------------------------
  def __repr__(self):
    s = "|META|"
    s += "{:2d}".format(self.trk) + "|"
    s += "{:08x}".format(self.dtime) + "|"
    s += "{:<40s}".format(self.name) + "|"
    if self.text is not None:
      s += "\n"
      s += "{:>27s}".format("|  ")
      s += "{:s}".format(self.text)
    return s

#----------------------------------------------------------------------
class MetaCuePoint(MetaEvent):

  #--------------------------------------------------------------------
  def __init__(self, trk, dtime, sb, etype, elen, edata, name):
    super().__init__(trk, dtime, sb, etype, elen, edata, name)

  #--------------------------------------------------------------------
#  def __repr__(self):
#    pass

#----------------------------------------------------------------------
class MetaProgramName(MetaEvent):

  #--------------------------------------------------------------------
  def __init__(self, trk, dtime, sb, etype, elen, edata, name):
    super().__init__(trk, dtime, sb, etype, elen, edata, name)

  #--------------------------------------------------------------------
#  def __repr__(self):
#    pass

#----------------------------------------------------------------------
class MetaDeviceName(MetaEvent):

  #--------------------------------------------------------------------
  def __init__(self, trk, dtime, sb, etype, elen, edata, name):
    super().__init__(trk, dtime, sb, etype, elen, edata, name)

  #--------------------------------------------------------------------
#  def __repr__(self):
#    pass

#----------------------------------------------------------------------
class MetaMidiChannelPrefix(MetaEvent):

  #--------------------------------------------------------------------
  def __init__(self, trk, dtime, sb, etype, elen, edata, name):
    super().__init__(trk, dtime, sb, etype, elen, edata, name)

  #--------------------------------------------------------------------
#  def __repr__(self):
#    pass

  #--------------------------------------------------------------------
class MetaMidiPort(MetaEvent):

  #--------------------------------------------------------------------
  def __init__(self, trk, dtime, sb, etype, elen, edata, name):
    super().__init__(trk, dtime, sb, etype, elen, edata, name)
    self.port = self.data[0]

  #--------------------------------------------------------------------
  def __repr__(self):
    s = "|META|"
    s += "{:2d}".format(self.trk) + "|"
    s += "{:08x}".format(self.dtime) + "|"
    s += "{:<40s}".format(self.name) + "|"
    s += "{:02x}".format(self.port) + "|"
    s += "\n"
    s += "{:>27s}".format("|  ")
    s += "{:2d}".format(self.port) + "|"
    return s

#----------------------------------------------------------------------
class MetaEndOfTrack(MetaEvent):

  #--------------------------------------------------------------------
  def __init__(self, trk, dtime, sb, etype, elen, edata, name):
    super().__init__(trk, dtime, sb, etype, elen, edata, name)

  #--------------------------------------------------------------------
  def __repr__(self):
    s = "|META|"
    s += "{:2d}".format(self.trk) + "|"
    s += "{:08x}".format(self.dtime) + "|"
    s += "{:<40s}".format("End of Track") + "|"
    return s

#----------------------------------------------------------------------
class MetaTempo(MetaEvent):

  #--------------------------------------------------------------------
  def __init__(self, trk, dtime, sb, etype, elen, edata, name):
    super().__init__(trk, dtime, sb, etype, elen, edata, name)
    self.tempo0 = (self.data[0] << 16)
    self.tempo1 = (self.data[1] <<  8)
    self.tempo2 = (self.data[2] <<  0)
    self.tempo = self.tempo0 + self.tempo1 + self.tempo2
    t = float(self.tempo)
    bpm = (60.0 * 1000.0 * 1000.0) / t
    self.bpm = int(round(bpm))

  #--------------------------------------------------------------------
  def __repr__(self):
    s = "|META|"
    s += "{:2d}".format(self.trk) + "|"
    s += "{:08x}".format(self.dtime) + "|"
    s += "{:<40s}".format(self.name) + "|"
    s += "{:02x}".format(self.data[0]) + "|"
    s += "{:02x}".format(self.data[1]) + "|"
    s += "{:02x}".format(self.data[2]) + "|"
    s += "\n"
    s += "{:>27s}".format("|  ")
    s += "{:3d}".format(self.bpm) + " bpm"
    return s

#----------------------------------------------------------------------
class MetaSmpteOffset(MetaEvent):

  #--------------------------------------------------------------------
  def __init__(self, trk, dtime, sb, etype, elen, edata, name):
    super().__init__(trk, dtime, sb, etype, elen, edata, name)
    self.hr = self.data[0]
    self.mn = self.data[1]
    self.se = self.data[2]
    self.fr = self.data[3]
    self.ff = self.data[4]
    self.frmRate = self.hr >> 5
    if self.frmRate == 0:
      self.fps = 24
    elif self.frmRate == 1:
      self.fps = 25
    elif self.frmRate == 10:
      self.fps = 30
    elif self.frmRate == 11:
      self.fps = 30
    else:
      Exception("Invalid SMPTE frame rate")

    self.hour = self.hr & 0x1f
    self.min = self.mn
    self.sec = self.se
    self.frm = self.fr
    self.subFrm = self.ff

  #--------------------------------------------------------------------
  def __repr__(self):
    s = "|META|"
    s += "{:2d}".format(self.trk) + "|"
    s += "{:08x}".format(self.dtime) + "|"
    s += "{:<40s}".format(self.name) + "|"
    s += "{:02x}".format(self.hr) + "|"
    s += "{:02x}".format(self.mn) + "|"
    s += "{:02x}".format(self.se) + "|"
    s += "{:02x}".format(self.fr) + "|"
    s += "{:02x}".format(self.ff) + "|"
    s += "\n"
    s += "{:>27s}".format("|  ")
    s += "{:02d}".format(self.hour) + ":"
    s += "{:02d}".format(self.min) + ":"
    s += "{:02d}".format(self.sec) + ":"
    s += "{:02d}".format(self.frm) + ":"
    s += "{:02d}".format(self.subFrm) + " "
    s += "{:2d}".format(self.fps) + " fps"
    return s

#----------------------------------------------------------------------
class MetaTimeSignature(MetaEvent):

  #--------------------------------------------------------------------
  def __init__(self, trk, dtime, sb, etype, elen, edata, name):
    super().__init__(trk, dtime, sb, etype, elen, edata, name)
    self.nn = self.data[0]
    self.dd = self.data[1]
    self.cc = self.data[2]
    self.bb = self.data[3]
    self.beatsPerBar = self.nn
    beat = 2.0 ** (-self.dd)
    beat = 1.0 / beat
    self.beatVal = int(round(beat))
    self.clicks = self.cc
    self.notated32ndPerQuarter = self.bb

  #--------------------------------------------------------------------
  def __repr__(self):
    s = "|META|"
    s += "{:2d}".format(self.trk) + "|"
    s += "{:08x}".format(self.dtime) + "|"
    s += "{:<40s}".format(self.name) + "|"
    s += "{:02x}".format(self.nn) + "|"
    s += "{:02x}".format(self.dd) + "|"
    s += "{:02x}".format(self.cc) + "|"
    s += "{:02x}".format(self.bb) + "|"
    s += "\n"
    s += "{:>27s}".format("|  ")
    s += "TS: {:02d}".format(self.beatsPerBar) + "/"
    s += "{:02d}".format(self.beatVal) + " "
    s += "Clicks:{:02d}".format(self.clicks) + " "
    s += "32nds:{:02d}".format(self.notated32ndPerQuarter)
    return s

#----------------------------------------------------------------------
class MetaKeySignature(MetaEvent):

  KeyDict = \
  {
    -7: ("Cb", "G#"),
    -6: ("Gb", "Eb"),
    -5: ("Db", "Bb"),
    -4: ("Ab", "F"),
    -3: ("Eb", "C"),
    -2: ("Bb", "G"),
    -1: ("F",  "D"),
     0: ("C",  "A"),
     1: ("G",  "E"),
     2: ("D",  "B"),
     3: ("A",  "F#"),
     4: ("E",  "C#"),
     5: ("B",  "G#"),
     6: ("F#", "D#"),
     7: ("C#", "Bb"),
  }

  #--------------------------------------------------------------------
  def __init__(self, trk, dtime, sb, etype, elen, edata, name):
    super().__init__(trk, dtime, sb, etype, elen, edata, name)
    self.sf = int.from_bytes(self.data[:1], byteorder="big", signed=True)
    self.mi = int.from_bytes(self.data[1:], byteorder="big", signed=False)
    self.key = self.KeyDict[self.sf][self.mi]
    if self.mi == 0:
      self.keyType = "Major"
    else:
      self.keyType = "Minor"

  #--------------------------------------------------------------------
  def __repr__(self):
    s = "|META|"
    s += "{:2d}".format(self.trk) + "|"
    s += "{:08x}".format(self.dtime) + "|"
    s += "{:<40s}".format(self.name) + "|"
    s += "{:02x}".format(self.data[0]) + "|"
    s += "{:02x}".format(self.data[1]) + "|"
    s += "\n"
    s += "{:>27s}".format("|  ")
    s += "{:<s}".format(self.key) + " "
    s += "{:<s}".format(self.keyType)
    return s

#----------------------------------------------------------------------
class MetaSequencerData(MetaEvent):

  #--------------------------------------------------------------------
  def __init__(self, trk, dtime, sb, etype, elen, edata, name):
    super().__init__(trk, dtime, sb, etype, elen, edata, name)

  #--------------------------------------------------------------------
#  def __repr__(self):
#    pass






