#!/usr/bin/env python
# -*- encoding:utf8 -*-

"""
nagios plugin to monitor redis availability and memory
-------------------------------------------------------
usage
::
    check_redis.py
"""

import os
from optparse import OptionParser

#nagios return codes
UNKNOWN = -1
OK = 0
WARNING = 1
CRITICAL = 2

parser = OptionParser()
parser.add_option("-w", "--memory-warning", dest="WARN_MEMORY",
                  help="Memory usage that raises warning signal.")
parser.add_option("-c", "--memory-critical", dest="CRIT_MEMORY",
                  help="Memory usage that raises critical signal.")

options, args = parser.parse_args()

WARN_MEMORY = int(options.WARN_MEMORY)
CRIT_MEMORY =  int(options.CRIT_MEMORY)

REDIS_MEM_CHECK='redis-cli info | grep used_memory:'
REDIS_SERVICE_CHECK='service redis-server status'

def get_redis_status():
    try:
        if 'inactive' in os.popen('%s' % (REDIS_SERVICE_CHECK)).read():
            return ('Service is offline.', CRITICAL)
        else:
            status_output = os.popen('%s' % (REDIS_MEM_CHECK)).read().split(':')
            mem = int(status_output[1])
            if WARN_MEMORY < mem < CRIT_MEMORY:
                return ('WARNING: Using too much memory: %s' % mem, WARNING)
            elif mem > CRIT_MEMORY:
                return ('CRITICAL: Using too much memory: %s' % mem, CRITICAL)
            return ('OK: Redis is online and OK. Memory Used: %s' % mem, OK)
    except Exception as e:
        print "CRITICAL: Could not get REDIS status.", e
        raise SystemExit, CRITICAL

output = get_redis_status()

print output[0]
raise SystemExit, output[1]
