from collections import Counter
import calendar
import itertools
import random
import re
import string
import requests

names = 'pavan vijaya reema riya vinay preethi dayananad google hacker news quick'.split()

for name in names:
	print(name.title())


first_half_alphabet = list(string.ascii_lowercase)[:13]
print(first_half_alphabet)


new_names = []

for name in names:
	if name[0] in first_half_alphabet:
		new_names.append(name.title())

print(new_names)

print(', '.join(new_names))


new_names2 = [ name.title() for name in names if name[0] in first_half_alphabet]

print(new_names2)

print(', '.join(new_names2))




resp = requests.get('http://projects.bobbelderbos.com/pcc/harry.txt')
words = resp.text.lower().split()

print(words[:5])
print(len(words))

count = Counter(words)
print(count.most_common(5))

print('-' in words)

words = [ re.sub(r'\W+', r'',word) for word in words]

print('-' in words)

print(len(words))

resp = requests.get('http://projects.bobbelderbos.com/pcc/stopwords.txt')
stopwords = resp.text.lower().split()
print(stopwords[:5])

words = [word for word in words if word.strip() and word not in stopwords]

print(words[:5])

print(len(words))

print(count.most_common(5))
count = Counter(words)
print(count.most_common(5))


### Generators

def num_gen():
	for i in range(10000):
		yield i

gen = num_gen()

next(gen)

for i in gen:
	if i % 1000 ==0:
		print(i)
try:
	next(gen)
except StopIteration:
	print("StopIteration exception: end of generator")

print("hellooo")

for i in gen:
	if i%1000 == 0:
		print(i)



options = 'banana mango blueberry redberry yellowberry carrot garlic radish onion milk soy purple'.split()

print(options)

def create_select_options(options = options):
	select_list = []

	for option in options:
		select_list.append(f'<option value={option}>{option.title()}</option>')

	return select_list		

from pprint import pprint as pp
pp(create_select_options())

print(create_select_options())

def create_select_options_gen(options = options):
	for option in options:
		yield f'<option value={option}>{option.title()}</option>'

print("hello")
print(create_select_options_gen())



pp(list(create_select_options_gen()))

