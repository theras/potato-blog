from .admin_views import *
from .post_views import *

import logging
def exception_test(request):
	logging.debug('Debug log')
	logging.warn('Warn log')
	logging.error('Error log')
	raise Exception()