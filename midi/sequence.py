import logging
import midi.file
import midi.chunk

#----------------------------------------------------------------------
class Sequence(object):

  #--------------------------------------------------------------------
  def __init__(self, filename=None):
    if filename is not None:
      self.chunkList = midi.file.File(filename).Read()
      logging.debug("")


  #--------------------------------------------------------------------
  def Read(self, filename):
    self.chunkList = midi.file.File(filename).Read()

    logging.debug("")
