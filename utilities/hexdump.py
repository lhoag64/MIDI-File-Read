import logging

#----------------------------------------------------------------------
def HexDump(desc, data, nbytes=None):

  logger = logging.getLogger()

  if (logger.level >= logging.DEBUG):

    inptype = type(data)
    if inptype is memoryview:
      inpdata = data
      inplen = inpdata.nbytes
    elif inptype is type(None):
      return
    else:
      logging.debug("BAD")

    if nbytes is not None:
      if nbytes < inplen:
        inplen = nbytes

    if inplen == 0:
      return

    output = desc
    output += "\n                              "

    cnt = 0
    for item in inpdata:
      output += format(item & 0xff, "02x")
      cnt += 1
      if (cnt == inplen):
        pass
      elif (cnt % 16 == 0):
        if (cnt != inplen):
          output += "\n                              "
      elif (cnt % 8 == 0):
        output += " - "
      else:
        output += " "
      if cnt == inplen:
        break

    logging.debug(output)

