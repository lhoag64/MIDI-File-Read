#import logging
import csv

#-------------------------------------------------------------------------------
class CsvHdrColumn:
  def __init__(self, desc, index):
    self.desc = desc
    self.index = index

#-------------------------------------------------------------------------------
class CsvColumn:
  def __init__(self, desc, index):
    self.desc = desc
    self.index = index
    self.rows = []

  def AddRow(self, val):
    self.rows.append(val)

#-------------------------------------------------------------------------------
class CsvFile:
  def __init__(self):
    self.reader = None
    self.fp = None

  def Open(self, filename):
    self.fp = open(filename, 'r')
    self.reader = csv.reader(self.fp)

  def GetRow(self):
    try:
      return next(self.reader)
    except StopIteration:
      return None

  def Close(self):
    self.fp.close()
