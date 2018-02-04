import logging

#----------------------------------------------------------------------
def HexDump(desc, data, btyes=None):

  logger = logging.getLogger()

  if (logger.level >= logging.DEBUG):

    inptype = type(data)
    if (inptype == memoryview):
      inpdata = data
      inplen = inpdata.nbytes
    else:
      logging.debug("BAD")

    if bytes is not None:
      inplen = bytes

    output = desc
    output += "\n                              "

    cnt = 0
    for item in inpdata:
      output += format(item & 0xff, "02x")
      cnt += 1
      if (cnt == inplen):
        pass
      elif (cnt % 16 == 0):
        output += "\n                              "
      elif (cnt % 8 == 0):
        output += " - "
      else:
        output += " "

    logging.debug(output)

