import logging
import os

#----------------------------------------------------------------------
class File:

  #--------------------------------------------------------------------
  def __init__(self, filename=None):
    self.fp = None
    self.fname = filename
    self.fstats = None

    if (filename != None):
      self.__Open()

    logging.debug("")

  #--------------------------------------------------------------------
  def Open(self, filename=None):

    if filename is not None:
      self.fname = filename

    self.__Open()

  #--------------------------------------------------------------------
  def __Open(self):
    try:
      self.fstats = os.stat(self.fname)
    except FileNotFoundError as err:
      raise err

    logging.debug("")
 