import logging

#----------------------------------------------------------------------
class Timing(object):
  pass

#----------------------------------------------------------------------
class PPQN(Timing):

  #--------------------------------------------------------------------
  def __init__(self, div):
    self.div = div

#----------------------------------------------------------------------
class SMPTE(Timing):

  #--------------------------------------------------------------------
  def __init__(self, div):
    self.div = div

