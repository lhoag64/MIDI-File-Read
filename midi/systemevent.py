import logging

from midi.event import Event

#----------------------------------------------------------------------
SystemEventDict = \
  {
    # System Common
    0x00 : (0xff, "System Exclusive"),
    0x01 : (0x00, "MTC Quarter Frame"),
    0x02 : (0x02, "Song Position Pointer"),
    0x03 : (0x01, "Song Select"),
    0x04 : (0x00, "Undefined"),
    0x05 : (0x00, "Undefined"),
    0x06 : (0x00, "Tune Request"),
    0x07 : (0x00, "End Or Exclusive"),
    # System Real Time
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
  elif (etype == 0x01):
    event = SystemMTCQuarterFrame(trk, dtime, sb, etype, elen, edata, name)
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

  #--------------------------------------------------------------------
  def DataToStr(self, data, dlen):
    return super().DataToStr(data, dlen)

#----------------------------------------------------------------------
class SystemSysex(SystemEvent):

  IdTextDict = \
    {
      0x00000001: "Sequential Circuits",
      0x00000004: "Moog",
      0x00000005: "Passport Designs",
      0x00000006: "Lexicon",
      0x00000007: "Kurzweil",
      0x00000008: "Fender",
      0x0000000a: "AKG Acoustics",
      0x0000000f: "Ensonic",
      0x00000010: "Oberheim",
      0x00000011: "Apple",
      0x00000013: "Digidesign",
      0x00000018: "Emu",
      0x0000001a: "Art",
      0x0000001c: "Eventide",
      0x00000022: "Synthaxe",
      0x00000024: "Hohner",
      0x00000029: "PPG",
      0x0000002b: "SSL",
      0x0000002d: "Hinton",
      0x0000002f: "Elka",
      0x00000030: "Dynacodr",
      0x00000033: "Nord",
      0x00000036: "Cheetah",
      0x0000003e: "Waldorf",
      0x00000040: "Kawai",
      0x00000041: "Roland",
      0x00000042: "Korg",
      0x00000043: "Yamaha",
      0x00000044: "Akai",
      0x00000048: "JVC",
      0x0000004c: "Sony",
      0x0000004e: "Teac",
      0x00000051: "Foster",
      0x00000052: "Zoom",
      0x0000007d: "Non-Commercial",
      0x0000007e: "Non Real Time",
      0x0000007f: "Real Time",
    }  

  #--------------------------------------------------------------------
  def __init__(self, trk, dtime, sb, etype, elen, edata, name):
    super().__init__(trk, dtime, sb, etype, elen, edata, name)
    idx = 0
    b = self.data[0]
    if b != 0:
      self.idcode = b
      idx += 1
    else:
      self.idcode = (self.data[1] << 8) + (self.data[2] << 0)     
      idx += 2
    self.idtext = SystemSysex.IdTextDict[self.idcode]
    self.data = self.data[idx:]

  #--------------------------------------------------------------------
  def __repr__(self):
    s = "|SYST|"
    s += "{:2d}".format(self.trk) + "|"
    s += "{:08x}".format(self.dtime) + "|"
    s += "{:<40s}".format(self.name) + "|"
    s += "\n"
    s += "{:>27s}".format("|  ")
    s += "{:08x}".format(self.idcode) + " "
    s += "{:<20s}".format(self.idtext) + " "
    s += "\n"
    s += "{:>27s}".format("|  ")
    s += super().DataToStr(self.data, self.dlen)
    return s

#----------------------------------------------------------------------
class SystemMTCQuarterFrame(SystemEvent):

  #--------------------------------------------------------------------
  def __init__(self, trk, dtime, sb, etype, elen, edata, name):
    super().__init__(trk, dtime, sb, etype, elen, edata, name)
    self.msgtype = self.data[0] >> 4
    self.msgdata = self.data[0] & 0x0f

  #--------------------------------------------------------------------
  def __repr__(self):
    s = "|SYST|"
    s += "{:2d}".format(self.trk) + "|"
    s += "{:08x}".format(self.dtime) + "|"
    s += "{:<20s}".format(self.name) + "|"
    s += "{:02x}".format(self.msgtype) + "|"
    s += "{:02x}".format(self.msgdata) + "|"
    return s

#----------------------------------------------------------------------
class SystemSongPositionPointer(SystemEvent):

  #--------------------------------------------------------------------
  def __init__(self, trk, dtime, sb, etype, elen, edata, name):
    super().__init__(trk, dtime, sb, etype, elen, edata, name)
    self.lsb = self.data[0]
    self.msb = self.data[0]
    self.ptr = (self.msb << 8) + (self.lsb << 0)

  #--------------------------------------------------------------------
  def __repr__(self):
    s = "|SYST|"
    s += "{:2d}".format(self.trk) + "|"
    s += "{:08x}".format(self.dtime) + "|"
    s += "{:<20s}".format(self.name) + "|"
    s += "{:02x}".format(self.lsb) + "|"
    s += "{:02x}".format(self.msb) + "|"
    s += "{:08x}".format(self.ptr) + "|"
    return s

#----------------------------------------------------------------------
class SystemSongSelect(SystemEvent):

  #--------------------------------------------------------------------
  def __init__(self, trk, dtime, sb, etype, elen, edata, name):
    super().__init__(trk, dtime, sb, etype, elen, edata, name)
    self.song = self.data[0]

  #--------------------------------------------------------------------
  def __repr__(self):
    s = "|SYST|"
    s += "{:2d}".format(self.trk) + "|"
    s += "{:08x}".format(self.dtime) + "|"
    s += "{:<20s}".format(self.name) + "|"
    s += "{:02x}".format(self.song) + "|"
    return s

#----------------------------------------------------------------------
class SystemTuneRequest(SystemEvent):

  #--------------------------------------------------------------------
  def __init__(self, trk, dtime, sb, etype, elen, edata, name):
    super().__init__(trk, dtime, sb, etype, elen, edata, name)

  #--------------------------------------------------------------------
  def __repr__(self):
    s = "|SYST|"
    s += "{:2d}".format(self.trk) + "|"
    s += "{:08x}".format(self.dtime) + "|"
    s += "{:<20s}".format(self.name) + "|"
    return s

#----------------------------------------------------------------------
class SystemEndSysex(SystemEvent):

  #--------------------------------------------------------------------
  def __init__(self, trk, dtime, sb, etype, elen, edata, name):
    super().__init__(trk, dtime, sb, etype, elen, edata, name)
    Exception("Invalid System Event type")

#----------------------------------------------------------------------
class SystemTimingClock(SystemEvent):

  #--------------------------------------------------------------------
  def __init__(self, trk, dtime, sb, etype, elen, edata, name):
    super().__init__(trk, dtime, sb, etype, elen, edata, name)

  #--------------------------------------------------------------------
  def __repr__(self):
    s = "|SYST|"
    s += "{:2d}".format(self.trk) + "|"
    s += "{:08x}".format(self.dtime) + "|"
    s += "{:<20s}".format(self.name) + "|"
    return s

#----------------------------------------------------------------------
class SystemStart(SystemEvent):

  #--------------------------------------------------------------------
  def __init__(self, trk, dtime, sb, etype, elen, edata, name):
    super().__init__(trk, dtime, sb, etype, elen, edata, name)

  #--------------------------------------------------------------------
  def __repr__(self):
    s = "|SYST|"
    s += "{:2d}".format(self.trk) + "|"
    s += "{:08x}".format(self.dtime) + "|"
    s += "{:<20s}".format(self.name) + "|"
    return s

#----------------------------------------------------------------------
class SystemContinue(SystemEvent):

  #--------------------------------------------------------------------
  def __init__(self, trk, dtime, sb, etype, elen, edata, name):
    super().__init__(trk, dtime, sb, etype, elen, edata, name)

  #--------------------------------------------------------------------
  def __repr__(self):
    s = "|SYST|"
    s += "{:2d}".format(self.trk) + "|"
    s += "{:08x}".format(self.dtime) + "|"
    s += "{:<20s}".format(self.name) + "|"
    return s

#----------------------------------------------------------------------
class SystemStop(SystemEvent):

  #--------------------------------------------------------------------
  def __init__(self, trk, dtime, sb, etype, elen, edata, name):
    super().__init__(trk, dtime, sb, etype, elen, edata, name)

  #--------------------------------------------------------------------
  def __repr__(self):
    s = "|SYST|"
    s += "{:2d}".format(self.trk) + "|"
    s += "{:08x}".format(self.dtime) + "|"
    s += "{:<20s}".format(self.name) + "|"
    return s

#----------------------------------------------------------------------
class SystemActiveSensing(SystemEvent):

  #--------------------------------------------------------------------
  def __init__(self, trk, dtime, sb, etype, elen, edata, name):
    super().__init__(trk, dtime, sb, etype, elen, edata, name)

  #--------------------------------------------------------------------
  def __repr__(self):
    s = "|SYST|"
    s += "{:2d}".format(self.trk) + "|"
    s += "{:08x}".format(self.dtime) + "|"
    s += "{:<20s}".format(self.name) + "|"
    return s

#----------------------------------------------------------------------
class SystemReset(SystemEvent):

  #--------------------------------------------------------------------
  def __init__(self, trk, dtime, sb, etype, elen, edata, name):
    super().__init__(trk, dtime, sb, etype, elen, edata, name)
    Exception("Invalid System Event type")



