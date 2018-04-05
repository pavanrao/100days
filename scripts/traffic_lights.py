from time import sleep
import itertools
import random

colors = 'Red Green Yellow'.split()
rotation = itertools.cycle(colors)

def rand_timer():
	return random.randint(2,6)

def light_rotation(rotation):
	for color in rotation:
		if color == 'Yellow':
			print('Caution! The color is %s' % color)
			sleep(3)
		elif color == 'Red':
			print('STOP! The color is %s' % color)
			sleep(rand_timer())
		else:
			print('Go! The color is %s' % color)
			sleep(rand_timer())


if __name__ == '__main__':
	light_rotation(rotation)
