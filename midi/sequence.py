import logging

#----------------------------------------------------------------------
class Sequence:

  #--------------------------------------------------------------------
  def __init__(self, filename=None):
    if filename is not None:
      self.__Read(filename)

  #--------------------------------------------------------------------
  def Read(self, filename):
    self.__Read(filename)

  #--------------------------------------------------------------------
  def __Read(self, filename):
    fp = open(filename, "rb")

    done = False
    while not done:
      self.__ReadChunk(fp)

  #--------------------------------------------------------------------
  def __ReadChunk(self, fp):
    chunkType = fp.read(4).decode("utf-8")
    chunkLen = int.from_bytes(fp.read(4), byteorder='big')
    chunkData = fp.read(chunkLen)

    logging.debug("")
