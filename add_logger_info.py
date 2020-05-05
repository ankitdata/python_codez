"""
This will help to create log file and save info and errors
"""
import logging
import logging.handlers
_logger = logging.getLogger(__name__)
_logger.addHandler(logging.StreamHandler(sys.stdout))
_logger.setLevel(logging.INFO)

filename = 'your_file.log'

my_logger = logging.getLogger(filename)
my_logger.setLevel(logging.INFO)
handler = logging.handlers.RotatingFileHandler(filename, maxBytes=20)
my_logger.addHandler(handler)

my_logger.info('add message here')

try :
    #add something here
except BaseException as error:
            my_logger.error('{}'.format(error))
