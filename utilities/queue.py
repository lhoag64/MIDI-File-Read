import logging
import threading

#----------------------------------------------------------------------
class QueueMsg:
  def __init__(self, msgtype, msgdata):
    self.type = msgtype
    self.data = msgdata

#----------------------------------------------------------------------
class Queue:
  def __init__(self):
    self.list = []
    self.event = threading.Event()
    self.lock = threading.Lock()

  #--------------------------------------------------------------------
  def Put(self, msg):
    self.lock.acquire()
    self.list.append(msg)
    self.event.set()
    self.lock.release()
    logging.debug('MSGQ |PUT |' + msg.type + '|' + str(msg.data))

  #--------------------------------------------------------------------
  def Get(self):
    self.lock.acquire()
    if (not self.list):
      msg = self.list.pop(0)
    else:
      msg = None
    self.lock.release()
    if (msg):
      logging.debug('MSGQ |GET |' + msg.type + '|' + str(msg.data))
    return msg

  #--------------------------------------------------------------------
  def Wait(self):
    logging.debug('MSGQ |WAIT|')
    self.event.wait()
    self.lock.acquire()
    self.event.clear()
    self.lock.release()
