#!/usr/bin/env python3

from datetime import datetime
import logging
import os

now = datetime.now()

logging.basicConfig(filename='/var/log/mountbackup.log',level=logging.DEBUG)

os.chdir('/')

if os.path.exists("/bkp/dados"):
  os.system('umount /bkp')
  logging.info(' %s/%s/%s - %s:%s:%s backup desmontado' % (now.day, now.month, now.year, now.hour, now.minute, now.second))

else:
  os.system('mount -a')
  logging.info(' %s/%s/%s - %s:%s:%s backup montado' % (now.day, now.month, now.year, now.hour, now.minute, now.second))

# ------- FIM -------
