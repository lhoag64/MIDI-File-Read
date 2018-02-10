import logging

from midi.event import Event

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
class MidiEvent(Event):

  #--------------------------------------------------------------------
  def __init__(self, trk, dtime, sb, etype, elen, edata, name):
    super().__init__(trk, dtime, sb, etype, elen, edata, name)
    
  #--------------------------------------------------------------------
#  def __repr__(self):

#----------------------------------------------------------------------
class MidiNoteOff(MidiEvent):

  #--------------------------------------------------------------------
  def __init__(self, trk, dtime, sb, etype, elen, edata, name):
    super().__init__(trk, dtime, sb, etype, elen, edata, name)
    self.note = self.data[0]
    self.vel = self.data[1]

  #--------------------------------------------------------------------
  def __repr__(self):
    s = "|MIDI|"
    s += "{:2d}".format(self.trk) + "|"
    s += "{:08x}".format(self.dtime) + "|"
    s += "{:<20s}".format(self.name) + "|"
    s += "{:02x}".format(self.note) + "|"
    s += "{:02x}".format(self.vel) + "|"
    return s

#----------------------------------------------------------------------
class MidiNoteOn(MidiEvent):

  #--------------------------------------------------------------------
  def __init__(self, trk, dtime, sb, etype, elen, edata, name):
    super().__init__(trk, dtime, sb, etype, elen, edata, name)
    self.note = self.data[0]
    self.vel = self.data[1]

  #--------------------------------------------------------------------
  def __repr__(self):
    s = "|MIDI|"
    s += "{:2d}".format(self.trk) + "|"
    s += "{:08x}".format(self.dtime) + "|"
    s += "{:<20s}".format(self.name) + "|"
    s += "{:02x}".format(self.note) + "|"
    s += "{:02x}".format(self.vel) + "|"
    return s

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


