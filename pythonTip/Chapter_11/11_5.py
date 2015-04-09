#!usr/bin/env python

import logging

logging.debug('Debugging information')
logging.info('Information message')
logging.warning('Warning:config file %s not fouond', 'server.conf')
logging.error('Error occurred')
logging.critical('Critical error -- shutting down')
