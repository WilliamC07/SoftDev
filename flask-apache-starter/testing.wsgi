#!/usr/bin/python3
import sys
sys.path.insert(0,"/var/www/testing/")
sys.path.insert(0,"/var/www/testing/testing/")

import logging
logging.basicConfig(stream=sys.stderr)

from testing import app as application