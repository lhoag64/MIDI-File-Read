import logging

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
class MetaEvent(object):

  #--------------------------------------------------------------------
  def __init__(self, trk, dtime, sb, etype, elen, edata, name):
    self.trk = trk
    self.dtime = dtime
    self.sb = sb
    self.type = etype
    self.dlen = elen
    self.data = edata
    self.name = name

  #--------------------------------------------------------------------
  def __repr__(self):
    s = ""
    s += format(self.dtime, "08x") + " "
    s += format(self.sb, "02x") + " "
    s += format(self.type, "02x") + " "
    s += format(self.dlen, "02x") + " "
    if self.data is not None:
      for b in self.data:
        s += format(b, "02x") + " "
    s += "\'" + self.name + "\'"

    return s

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

  #--------------------------------------------------------------------
#  def __repr__(self):
#    pass

#----------------------------------------------------------------------
class MetaCopyright(MetaEvent):

  #--------------------------------------------------------------------
  def __init__(self, trk, dtime, sb, etype, elen, edata, name):
    super().__init__(trk, dtime, sb, etype, elen, edata, name)

  #--------------------------------------------------------------------
#  def __repr__(self):
#    pass

#----------------------------------------------------------------------
class MetaTrackName(MetaEvent):

  #--------------------------------------------------------------------
  def __init__(self, trk, dtime, sb, etype, elen, edata, name):
    super().__init__(trk, dtime, sb, etype, elen, edata, name)

  #--------------------------------------------------------------------
#  def __repr__(self):
#    pass

#----------------------------------------------------------------------
class MetaInstrumentName(MetaEvent):

  #--------------------------------------------------------------------
  def __init__(self, trk, dtime, sb, etype, elen, edata, name):
    super().__init__(trk, dtime, sb, etype, elen, edata, name)

  #--------------------------------------------------------------------
#  def __repr__(self):
#    pass

#----------------------------------------------------------------------
class MetaLyric(MetaEvent):

  #--------------------------------------------------------------------
  def __init__(self, trk, dtime, sb, etype, elen, edata, name):
    super().__init__(trk, dtime, sb, etype, elen, edata, name)

  #--------------------------------------------------------------------
#  def __repr__(self):
#    pass

#----------------------------------------------------------------------
class MetaMarker(MetaEvent):

  #--------------------------------------------------------------------
  def __init__(self, trk, dtime, sb, etype, elen, edata, name):
    super().__init__(trk, dtime, sb, etype, elen, edata, name)

  #--------------------------------------------------------------------
#  def __repr__(self):
#    pass

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

  #--------------------------------------------------------------------
#  def __repr__(self):
#    pass

#----------------------------------------------------------------------
class MetaEndOfTrack(MetaEvent):

  #--------------------------------------------------------------------
  def __init__(self, trk, dtime, sb, etype, elen, edata, name):
    super().__init__(trk, dtime, sb, etype, elen, edata, name)

  #--------------------------------------------------------------------
#  def __repr__(self):
#    pass

#----------------------------------------------------------------------
class MetaTempo(MetaEvent):

  #--------------------------------------------------------------------
  def __init__(self, trk, dtime, sb, etype, elen, edata, name):
    super().__init__(trk, dtime, sb, etype, elen, edata, name)

  #--------------------------------------------------------------------
#  def __repr__(self):
#    pass

#----------------------------------------------------------------------
class MetaSmpteOffset(MetaEvent):

  #--------------------------------------------------------------------
  def __init__(self, trk, dtime, sb, etype, elen, edata, name):
    super().__init__(trk, dtime, sb, etype, elen, edata, name)

  #--------------------------------------------------------------------
#  def __repr__(self):
#    pass

#----------------------------------------------------------------------
class MetaTimeSignature(MetaEvent):

  #--------------------------------------------------------------------
  def __init__(self, trk, dtime, sb, etype, elen, edata, name):
    super().__init__(trk, dtime, sb, etype, elen, edata, name)

  #--------------------------------------------------------------------
#  def __repr__(self):
#    pass

#----------------------------------------------------------------------
class MetaKeySignature(MetaEvent):

  #--------------------------------------------------------------------
  def __init__(self, trk, dtime, sb, etype, elen, edata, name):
    super().__init__(trk, dtime, sb, etype, elen, edata, name)

  #--------------------------------------------------------------------
#  def __repr__(self):
#    pass

#----------------------------------------------------------------------
class MetaSequencerData(MetaEvent):

  #--------------------------------------------------------------------
  def __init__(self, trk, dtime, sb, etype, elen, edata, name):
    super().__init__(trk, dtime, sb, etype, elen, edata, name)

  #--------------------------------------------------------------------
#  def __repr__(self):
#    pass






