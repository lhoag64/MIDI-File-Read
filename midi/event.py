import logging

#----------------------------------------------------------------------
class Event(object):

  #--------------------------------------------------------------------
  def __init__(self, trk, dtime, sb, etype, elen, edata, name):
    self.trk = trk
    self.dtime = dtime
    self.sb = sb
    self.type = etype
    self.dlen = elen
    if (elen > 0):
      self.data = bytes(edata)
    else:
      self.data = None
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
    #s += "\n                       "
    ##members = [attr for attr in dir(self)]
    #members = vars(self)
    #for member in members:
    #  if not callable(getattr(self, member)):
    #    s += "\n                    " + member 

    return s

  #--------------------------------------------------------------------
  def DataToStr(self, data, dlen):
    s = ""
    if (self.dlen > 0) and (self.data is not None):
      s += "\n"
      s += "{:>69s}".format("|")
      idx = 0
      for b in self.data:
        s += "{:02x}".format(b)
        s += " "
        idx += 1
        if (idx % 16) == 0:
          if idx != self.dlen:
            s += "\n"
            s += "{:>69s}".format("|")
    return s