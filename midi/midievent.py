import logging


#----------------------------------------------------------------------
MidiEventDict = \
  {
    0x08 : (0x02, "Note Off"),
    0x09 : (0x02, "Note On"),
    0x0a : (0x02, "Key Pressure"),
    0x0b : (0x02, "Control Change"),
    0x0c : (0x01, "Program Change"),
    0x0d : (0x01, "Channel Pressure"),
    0x0e : (0x02, "Pitch Wheel"),
  }

#----------------------------------------------------------------------
def CreateMidiEvent(trk, dtime, sb, etype, elen, edata, name):
  event = None

  if etype == 0x08:
    event = MidiNoteOff(trk, dtime, sb, etype, elen, edata, name)
  elif etype == 0x09:
    event = MidiNoteOn(trk, dtime, sb, etype, elen, edata, name)
  elif etype == 0x0a:
    event = MidiKeyPressure(trk, dtime, sb, etype, elen, edata, name)
  elif etype == 0x0b:
    event = MidiControlChange(trk, dtime, sb, etype, elen, edata, name)
  elif etype == 0x0c:
    event = MidiProgramChange(trk, dtime, sb, etype, elen, edata, name)
  elif etype == 0x0d:
    event = MidiChannelPressure(trk, dtime, sb, etype, elen, edata, name)
  elif etype == 0x0e:
    event = MidiPitchWheel(trk, dtime, sb, etype, elen, edata, name)
  else:
    Exception("Unknown Midi Event type")

  return event

#----------------------------------------------------------------------
class MidiEvent(object):

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
    #s += format(self.type, "02x") + " "
    #s += format(self.chan, "02x") + " "
    #s += format(self.dlen, "02x") + " "
    if self.data is not None:
      for b in self.data:
        s += format(b, "02x") + " "
    s += "\'" + self.name + "\'"

    return s

#----------------------------------------------------------------------
class MidiNoteOff(MidiEvent):

  #--------------------------------------------------------------------
  def __init__(self, trk, dtime, sb, etype, elen, edata, name):
    super().__init__(trk, dtime, sb, etype, elen, edata, name)

  #--------------------------------------------------------------------
#  def __repr__(self):
#    pass

#----------------------------------------------------------------------
class MidiNoteOn(MidiEvent):

  #--------------------------------------------------------------------
  def __init__(self, trk, dtime, sb, etype, elen, edata, name):
    super().__init__(trk, dtime, sb, etype, elen, edata, name)

  #--------------------------------------------------------------------
#  def __repr__(self):
#    pass

#----------------------------------------------------------------------
class MidiKeyPressure(MidiEvent):

  #--------------------------------------------------------------------
  def __init__(self, trk, dtime, sb, etype, elen, edata, name):
    super().__init__(trk, dtime, sb, etype, elen, edata, name)

  #--------------------------------------------------------------------
#  def __repr__(self):
#    pass

#----------------------------------------------------------------------
class MidiControlChange(MidiEvent):

  #--------------------------------------------------------------------
  def __init__(self, trk, dtime, sb, etype, elen, edata, name):
    super().__init__(trk, dtime, sb, etype, elen, edata, name)

  #--------------------------------------------------------------------
#  def __repr__(self):
#    pass

#----------------------------------------------------------------------
class MidiProgramChange(MidiEvent):

  #--------------------------------------------------------------------
  def __init__(self, trk, dtime, sb, etype, elen, edata, name):
    super().__init__(trk, dtime, sb, etype, elen, edata, name)

  #--------------------------------------------------------------------
#  def __repr__(self):
#    pass

#----------------------------------------------------------------------
class MidiChannelPressure(MidiEvent):

  #--------------------------------------------------------------------
  def __init__(self, trk, dtime, sb, etype, elen, edata, name):
    super().__init__(trk, dtime, sb, etype, elen, edata, name)

  #--------------------------------------------------------------------
#  def __repr__(self):
#    pass

#----------------------------------------------------------------------
class MidiPitchWheel(MidiEvent):

  #--------------------------------------------------------------------
  def __init__(self, trk, dtime, sb, etype, elen, edata, name):
    super().__init__(trk, dtime, sb, etype, elen, edata, name)

  #--------------------------------------------------------------------
#  def __repr__(self):
#    pass


