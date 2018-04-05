import itertools
import sys
import time


symbols = itertools.cycle('-\|/')

`#TODO: Create a spinner with a progress bar. progress bar should slowly increase with a fast spinner at the end.

while True:
	sys.stdout.write('\r' + next(symbols))
	sys.stdout.flush()
	time.sleep(0.25)

