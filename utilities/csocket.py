import logging
import socket

#----------------------------------------------------------------------
class CSocket:
  def __init__(self):
    self.cs = None

  #--------------------------------------------------------------------
  def Create(self):
    logging.debug('SOCK |CREATE')
    self.cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

  #--------------------------------------------------------------------
  def Connect(self, host, port):
    logging.debug('SOCK |CONNECT')
    self.cs.connect((host, port))

  #--------------------------------------------------------------------
  def Close(self):
    logging.debug('SOCK |CLOSE')
    try:
      self.cs.close()
    except OSError:
      pass

  #--------------------------------------------------------------------
  def Shutdown(self):
    logging.debug('SOCK |SHUTDOWN')
    try:
      self.cs.shutdown(socket.SHUT_RDWR)
    except OSError:
      pass
  #--------------------------------------------------------------------
  def Send(self, msg):
    try:
      logging.info(msg.strip(' \n\t\r\000'))
      logging.debug('SOCK |SEND-----------------------------------')
      logging.debug('SOCK |SEND|' + msg.strip(' \n\t\r\000'))
      logging.debug('SOCK |SEND-----------------------------------')
      msg = msg + '\r'
      cnt = self.cs.send(msg.encode())
      if (cnt != len(msg)):
        logging.debug('SOCK |SEND|CNT |' + str(cnt))
    except socket.error as excMsg:
      logging.debug(excMsg.strerror)
      return None
    return 1

  #--------------------------------------------------------------------
  def Recv(self, maxlen):
    try:
      buf = self.cs.recv(maxlen)
    except socket.error as excMsg:
      logging.debug(excMsg.strerror)
      return None
    except AttributeError:
      return None
    buf = buf.decode()
    logging.info(buf.strip(' \n\t\r\000'))
    logging.debug('SOCK |RECV-----------------------------------')
    logging.debug('SOCK |RECV|' + buf.strip(' \n\t\r\000'))
    logging.debug('SOCK |RECV-----------------------------------')
    return buf
