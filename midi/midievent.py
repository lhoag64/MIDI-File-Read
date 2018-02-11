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

  #    A    0
  #    A#   1
  #    B    2
  #  0 C    3
  #  1 C#   4
  #  2 D    5
  #  3 D#   6
  #  4 E    7
  #  5 F    8
  #  6 F#   9
  #  7 G   10
  #  8 G#  11
  #  9 A
  # 10 A#
  # 11 B

  NoteDict = \
    {
       0 : ("C",  "C"),
       1 : ("C#", "Db"),
       2 : ("D",  "D"),
       3 : ("D#", "Eb"),
       4 : ("E",  "E"),
       5 : ("F",  "F"),
       6 : ("F#", "Gb"),
       7 : ("G",  "G"),
       8 : ("G#", "Ab"),
       9 : ("A",  "A"),
      10 : ("A#", "Bb"),
      11 : ("B",  "B"),
    }

  #--------------------------------------------------------------------
  def __init__(self, trk, dtime, sb, etype, elen, edata, name):
    super().__init__(trk, dtime, sb, etype, elen, edata, name)
    self.nn = self.data[0]
    self.vel = self.data[1]
    dm = divmod(self.nn, 12)
    self.note = self.NoteDict[dm[1]][0]
    self.octave = dm[0] - 2
    #logging.debug("")

  #--------------------------------------------------------------------
  def __repr__(self):
    s = "|MIDI|"
    s += "{:2d}".format(self.trk) + "|"
    s += "{:08x}".format(self.dtime) + "|"
    s += "{:<40s}".format(self.name) + "|"
    s += "{:02x}".format(self.nn) + "|"
    s += "{:02x}".format(self.vel) + "|"
    s += "\n"
    s += "{:>27s}".format("|  ")
    s += "Note:{:2s}".format(self.note) + " "
    s += "{:2d}".format(self.octave) + " "
    s += "Vel:{:3d}".format(self.vel) + " "
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


