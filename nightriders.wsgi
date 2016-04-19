activate_this = '/var/www/nightriders/env/Scripts/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

import sys
sys.path.insert(0, '/var/www/nightriders')

from nightridershack import app as application
