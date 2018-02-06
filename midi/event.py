import logging
from utilities.buffer import Buffer

#----------------------------------------------------------------------
def ParseFileEvent(data, dtime):
  byte
id

#  #--------------------------------------------------------------------
#  def ReadVLQ(self, data):
#
#    val = 0
#    while True:
#      buf = data.ReadByte()
#      val = (val << 7) + buf
#      if buf & 0x80 == 0:
#        break
#
#    return val


#----------------------------------------------------------------------
class Event(object):
  #--------------------------------------------------------------------
  def __init(self):
    pass

#----------------------------------------------------------------------
class MidiEvent(Event):
  #--------------------------------------------------------------------
  def __init(self, data=None, dtime=None):
    if data is None):
      return

    self.dtime = dtime
    byte = data.ReadByte()
    self.chNum = byte & 0x08
    self.

#----------------------------------------------------------------------
class SysexEvent(Event):
  #--------------------------------------------------------------------
  def __init(self, data=None, dtime=None):
    pass

#----------------------------------------------------------------------
class MetaEvent(Event):
  #--------------------------------------------------------------------
  def __init(self, data=None, dtime=None):
    pass

