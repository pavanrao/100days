import itertools
import random

NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos', 
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']

names2 = [name.split() for name in NAMES]
print(names2)

names3 = [[name.title() for name in names ]for names in names2]
print(names3)

names4 = [', '.join(names) for names in names3]
print(names4)
#['Arnold, Schwarzenegger', 'Alec, Baldwin', 'Bob, Belderbos', 'Julian, Sequeira', 'Sandra, Bullock', 'Keanu, Reeves', 'Julbob, Pybites', 'Bob, Belderbos', 'Julian, Sequeira', 'Al, Pacino', 'Brad, Pitt', 'Matt, Damon', 'Brad, Pitt']

def gen_pairs(names = names4):
	name1 = names4.pop(random.randint(0,len(names4)))
	name2 = names4.pop(random.randint(0,len(names4)))
	yield(f'{name1} teams up with {name2}')

pairs = gen_pairs()

for pair in pairs:
	print(pair)


