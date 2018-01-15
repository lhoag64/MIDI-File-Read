import logging
import configparser

from utilities.args import ParseArgs
from utilities.logconfig import LogConfig
from midimod.file import MidiFile

if (__name__ == "__main__"):

  args = ParseArgs()
  if (len(args) < 1):
    exit()

  config = configparser.SafeConfigParser()
  config.read(args["INIFILE"])

  LogConfig(config.get("FILES", "LOGFILE"))

  logging.debug("Program Entry")

  midiFile = MidiFile()
  midiFile.Read(config.get("FILES", "MIDFILE"))






  logging.debug("Program Exit")
