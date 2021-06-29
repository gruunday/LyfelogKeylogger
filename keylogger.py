#!/usr/bin/python3 env

import pyxhook
import socket
import time
import sched


class MetricFling:
  def __init__(self):
    carbon_server = "51.77.58.219"
    carbon_port = 2003
    self.addr = (carbon_server, carbon_port)
    self.count = 0
    self.sock = socket.socket()
    connected = False
    self.sock.connect(self.addr)

  def fling(self, count):
    metric = f'keylogger.starboard {self.count} {time.time()}\n'
    #print(metric)
    self.count = 0
    self.sock.sendall(metric.encode('utf-8'))
    self.s.enter(10, 1, self.fling, (self.count,))

  def on_keypress(self, event):
    self.count += 1

  def run(self):
      hm = pyxhook.HookManager()
      hm.KeyDown = self.on_keypress
      hm.HookKeyboard()
      hm.start()

      # Every 60 Seconds report that minutes keys hit
      self.s = sched.scheduler(time.time, time.sleep)
      self.s.enter(10, 1, self.fling, (self.count,))
      self.s.run()

if __name__ == '__main__':
    m = MetricFling()
    m.run()

# If space is hit exit
#  if event.Ascii == 32:
#    exit(0)
