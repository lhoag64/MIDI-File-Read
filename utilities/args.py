import sys
import os.path

#----------------------------------------------------------------------
def ParseArgs():
  args = {}

  dummy, pyFile = os.path.split(sys.argv[0])

  if (len(sys.argv) != 2):
    print("usage: " + pyFile + " inifile")
    return None

  for i in range(1, len(sys.argv)):
    if (i == 1):
      args["INIFILE"] = sys.argv[1]

  return args
