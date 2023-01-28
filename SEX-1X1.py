import os

try:

	import requestsexcept ImportError:

	print('\n [×] requests module not installed!...\n')

	os.system('pip install requests')
