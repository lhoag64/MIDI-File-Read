import logging

from midi.event import Event

#----------------------------------------------------------------------
SystemEventDict = \
  {
    0x00 : (0xff, "System Exclusive"),
    0x01 : (0x00, "Undefined"),
    0x02 : (0x02, "Song Position Pointer"),
    0x03 : (0x01, "Song Select"),
    0x04 : (0x00, "Undefined"),
    0x05 : (0x00, "Undefined"),
    0x06 : (0x00, "Tune Request"),
    0x07 : (0x00, "End Or Exclusive"),
    0x08 : (0x00, "Timeing Clock"),
    0x09 : (0x00, "Undefined"),
    0x0a : (0x00, "Start"),
    0x0b : (0x00, "Continue"),
    0x0c : (0x00, "Stop"),
    0x0d : (0x00, "Undefined"),
    0x0e : (0x00, "Active Sensing"),
    0x0f : (0x00, "Reset"),
  }

#----------------------------------------------------------------------
def CreateSystemEvent(trk, dtime, sb, etype, elen, edata, name):
  event = None

  if (etype == 0x00):
    event = SystemSysex(trk, dtime, sb, etype, elen, edata, name)
  elif (etype == 0x02):
    event = SystemSongPositionPointer(trk, dtime, sb, etype, elen, edata, name)
  elif (etype == 0x03):
    event = SystemSongSelect(trk, dtime, sb, etype, elen, edata, name)
  elif (etype == 0x06):
    event = SystemTuneRequest(trk, dtime, sb, etype, elen, edata, name)
  elif (etype == 0x07):
    event = SystemEndSysex(trk, dtime, sb, etype, elen, edata, name)
  elif (etype == 0x08):
    event = SystemTimingClock(trk, dtime, sb, etype, elen, edata, name)
  elif (etype == 0x0a):
    event = SystemStart(trk, dtime, sb, etype, elen, edata, name)
  elif (etype == 0x0b):
    event = SystemContinue(trk, dtime, sb, etype, elen, edata, name)
  elif (etype == 0x0c):
    event = SystemStop(trk, dtime, sb, etype, elen, edata, name)
  elif (etype == 0x0e):
    event = SystemActiveSensing(trk, dtime, sb, etype, elen, edata, name)
  elif (etype == 0x0f):
    event = SystemReset(trk, dtime, sb, etype, elen, edata, name)
  else:
    Exception("Unknown System Event type")

  return event

#----------------------------------------------------------------------
class SystemEvent(Event):

  #--------------------------------------------------------------------
  def __init__(self, trk, dtime, sb, etype, elen, edata, name):
    super().__init__(trk, dtime, sb, etype, elen, edata, name)

  #--------------------------------------------------------------------
  #def __repr__(self):

#----------------------------------------------------------------------
class SystemSysex(SystemEvent):

  #--------------------------------------------------------------------
  def __init__(self, trk, dtime, sb, etype, elen, edata, name):
    super().__init__(trk, dtime, sb, etype, elen, edata, name)

  #--------------------------------------------------------------------
  def __repr__(self):
    s = "|SYST|"
    s += "{:2d}".format(self.trk) + "|"
    s += "{:08x}".format(self.dtime) + "|"
    s += "{:<20s}".format(self.name) + "|"
    if (self.dlen > 0) and (self.data is not None):
      s += "\n"
      s += "{:>69s}".format("|")
      idx = 0
      for b in self.data:
        s += "{:02x}".format(b)
        s += " "
        idx += 1
        if (idx % 8) == 0:
          if idx != self.dlen:
            s += "\n"
            s += "{:>69s}".format("|")
    return s

#----------------------------------------------------------------------
class SystemSongPositionPointer(SystemEvent):

  #--------------------------------------------------------------------
  def __init__(self, trk, dtime, sb, etype, elen, edata, name):
    super().__init__(trk, dtime, sb, etype, elen, edata, name)

  #--------------------------------------------------------------------
#  def __repr__(self):
#    pass

#----------------------------------------------------------------------
class SystemSongSelect(SystemEvent):

  #--------------------------------------------------------------------
  def __init__(self, trk, dtime, sb, etype, elen, edata, name):
    super().__init__(trk, dtime, sb, etype, elen, edata, name)

  #--------------------------------------------------------------------
#  def __repr__(self):
#    pass

#----------------------------------------------------------------------
class SystemTuneRequest(SystemEvent):

  #--------------------------------------------------------------------
  def __init__(self, trk, dtime, sb, etype, elen, edata, name):
    super().__init__(trk, dtime, sb, etype, elen, edata, name)

  #--------------------------------------------------------------------
#  def __repr__(self):
#    pass

#----------------------------------------------------------------------
class SystemEndSysex(SystemEvent):

  #--------------------------------------------------------------------
  def __init__(self, trk, dtime, sb, etype, elen, edata, name):
    super().__init__(trk, dtime, sb, etype, elen, edata, name)

  #--------------------------------------------------------------------
#  def __repr__(self):
#    pass

#----------------------------------------------------------------------
class SystemTimingClock(SystemEvent):

  #--------------------------------------------------------------------
  def __init__(self, trk, dtime, sb, etype, elen, edata, name):
    super().__init__(trk, dtime, sb, etype, elen, edata, name)

  #--------------------------------------------------------------------
#  def __repr__(self):
#    pass

#----------------------------------------------------------------------
class SystemStart(SystemEvent):

  #--------------------------------------------------------------------
  def __init__(self, trk, dtime, sb, etype, elen, edata, name):
    super().__init__(trk, dtime, sb, etype, elen, edata, name)

  #--------------------------------------------------------------------
#  def __repr__(self):
#    pass

#----------------------------------------------------------------------
class SystemContinue(SystemEvent):

  #--------------------------------------------------------------------
  def __init__(self, trk, dtime, sb, etype, elen, edata, name):
    super().__init__(trk, dtime, sb, etype, elen, edata, name)

  #--------------------------------------------------------------------
#  def __repr__(self):
#    pass

#----------------------------------------------------------------------
class SystemStop(SystemEvent):

  #--------------------------------------------------------------------
  def __init__(self, trk, dtime, sb, etype, elen, edata, name):
    super().__init__(trk, dtime, sb, etype, elen, edata, name)

  #--------------------------------------------------------------------
#  def __repr__(self):
#    pass

#----------------------------------------------------------------------
class SystemActiveSensing(SystemEvent):

  #--------------------------------------------------------------------
  def __init__(self, trk, dtime, sb, etype, elen, edata, name):
    super().__init__(trk, dtime, sb, etype, elen, edata, name)

  #--------------------------------------------------------------------
#  def __repr__(self):
#    pass

#----------------------------------------------------------------------
class SystemReset(SystemEvent):

  #--------------------------------------------------------------------
  def __init__(self, trk, dtime, sb, etype, elen, edata, name):
    super().__init__(trk, dtime, sb, etype, elen, edata, name)

  #--------------------------------------------------------------------
#  def __repr__(self):
#    pass


