#!/usr/bin/python3
import sys
sys.path.insert(0,"/var/www/myapp/")
sys.path.insert(0,"/var/www/myapp/myapp/")

import logging
logging.basicConfig(stream=sys.stderr)

from myapp import app as application

