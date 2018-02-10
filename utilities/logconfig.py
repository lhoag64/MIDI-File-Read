import logging

#----------------------------------------------------------------------
def LogConfig(name):

  with open(name, 'w') as dummy:
    pass

  #logfmt = '%(asctime)s %(levelname)s-%(message)s'
  logfmt = '%(levelname)s--%(message)s'
  formatter = logging.Formatter(logfmt)

  logging.basicConfig(level=logging.DEBUG, format=logfmt)

  log = logging.getLogger()
  fh = logging.FileHandler(name)
  fh.setFormatter(formatter)
  log.addHandler(fh)
