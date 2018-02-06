import logging
import configparser

from utilities.args import ParseArgs
from utilities.logconfig import LogConfig
#from utilities.file import File

from midi.sequence import Sequence

if (__name__ == "__main__"):

  args = ParseArgs()
  if (len(args) < 1):
    exit()

  config = configparser.SafeConfigParser()
  config.read(args["INIFILE"])

  LogConfig(config.get("FILES", "LOGFILE"))

  logging.debug("Program Entry")

  seq = Sequence()
  seq.Read(config.get("FILES", "MIDIFILE"))


  logging.debug("Program Exit")
