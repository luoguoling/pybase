__author__ = 'Administrator'
import os
import logging
#os.chmod()
#os.path.exists("")
a = 33
logging.basicConfig(filename=os.path.join(os.getcwd(),'log11.txt'),level=logging.WARN,filemode='w',format='%(asctime)s - %(levelname)s:%(message)s ')
logging.debug('debug')
logging.info('info')
logging.warning('warn')
logging.error('influence')
print os.getcwd()
logging.debug(a)
print logging.getLevelName(10)
log = logging.getLogger('root')
log.error('abcde')
try:
    raise Exception,'this is a exception'
except:
    log = logging.getLogger('root')
    log.exception('exception')