#!/usr/bin/python3

import pyxhook
import socket
import time
import sched
import os
import datetime
import getpass


class Keylogger:
  def __init__(self):
    self.count = 0
    self.hostname = socket.gethostname()
    os.environ["DISPLAY"] = ":1"

  def report(self):
    today = datetime.date.today()
    filename = today.strftime('%Y%m%d')
    with open(f'/home/{getpass.getuser()}/.keylogger/{filename}.log', 'a+') as f:
      f.write(f'{self.hostname}, {self.count}, {time.time()}\n')

  def fling(self, count):
    self.report()
    self.count = 0
    self.s.enter(10, 1, self.fling, (self.count,))

  def on_keypress(self, event):
    self.count += 1

  def run(self):
      hm = pyxhook.HookManager()
      hm.KeyDown = self.on_keypress
      hm.HookKeyboard()
      hm.start()

      # Every 10 Seconds report that minutes keys hit
      self.s = sched.scheduler(time.time, time.sleep)
      self.s.enter(10, 1, self.fling, (self.count,))
      self.s.run()

if __name__ == '__main__':
    m = Keylogger()
    m.run()
