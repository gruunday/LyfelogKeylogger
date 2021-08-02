#!/usr/bin/python3

import pyxhook
import socket
import time
import sched
import logging
import datetime
from pathlib import Path
import requests
import os


class MetricFling:
  def __init__(self):
    self.count = 0
    self.hostname = socket.gethostname()
    os.environ["DISPLAY"] = ":1"


  def get_headers(self):
    with open('/etc/api.key', 'r') as f:
      key = f.readline().strip('\n')
      return {'x-api-key' : key, 'hostname' : self.hostname, 'metric': str(self.count), 'time': str(time.time())}

  def report(self):
    r = requests.post(f'https://lyfelog.skunkjunk.space/metric/', headers=self.get_headers())

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
    m = MetricFling()
    m.run()
