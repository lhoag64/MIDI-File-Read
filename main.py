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

#  midiFile = MidiFile()
#  midiFile.Read(config.get("FILES", "MIDFILE"))

#  try:
#    midiFile = File()
#    midiFile.Open(config.get("FILES", "MIDIFILE"))
#  except FileNotFoundError as err:
#    logging.debug("Exception: " + err.strerror)
#    exit()

  seq = Sequence()
  seq.Read(config.get("FILES", "MIDIFILE"))


  logging.debug("Program Exit")
