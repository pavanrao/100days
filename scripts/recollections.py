"""
Trying out defaultdict, namedtuple, deque, Counter
Funny story: 
	from collections import.. . was not working when i first tried
	I realized that I had named this file as collections.py.
"""
from collections import defaultdict, namedtuple, deque, Counter
import csv
import random
from urllib.request import urlretrieve
from datetime import datetime, date, timedelta




user1 = ('pavan', 'rao')
f'{user1[0]} is a {user1[1]}'
#'pavan is a rao'

User = namedtuple('User', 'first last')
user2 = User(first = 'pavan', last = 'rao')
user2
#User(first='pavan', last='rao')
user1
#('pavan', 'rao')
user2.first
#'pavan'
user2.last
#'rao'

f'{user2.first} is a {user2.last}'
#'pavan is a rao'

users = {'rao': 'coder'}

#users['reema']
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#KeyError: 'reema'
users['rao']
#'coder'
users['reema'] = 'hacker'
users['reema']
#'hacker'
users
#{'rao': 'coder', 'reema': 'hacker'}

users.get('riya') is None
#True

others = [('pavan', 'tester'), ('vijaya', 'PM')]
others
#[('pavan', 'tester'), ('vijaya', 'PM')]
type(others)
#<class 'list'>
type(others[0])
#<class 'tuple'>

userlist = defaultdict(list)
for name,role in others:
    userlist[name].append(role)

userlist
#defaultdict(<class 'list'>, {'pavan': ['tester'], 'vijaya': ['PM']})

users
#{'rao': 'coder', 'reema': 'hacker'}
for name in users:
    print(name, users[name])

#rao coder
#reema hacker

for name in users:
    userlist[name].append(users[name])


userlist
#defaultdict(<class 'list'>, {'pavan': ['tester'], 'vijaya': ['PM'], 'rao': ['coder'], 'reema': ['hacker']})


userlist['rao'].append('dad')

userlist
#defaultdict(<class 'list'>, {'pavan': ['tester'], 'vijaya': ['PM'], 'rao': ['coder', 'dad'], 'reema': ['hacker']})



words = "In publishing and graphic design, lorem ipsum is a placeholder text \
commonly used to demonstrate the visual form of a document without relying on \
meaningful content (also called greeking). Replacing the actual content with \
placeholder text allows designers to design the form of the content before the \
content itself has been produced. The lorem ipsum text is typically a scrambled \
section of De finibus bonorum et malorum, a 1st-century BC Latin text by Cicero, \
with words altered, added, and removed to make it nonsensical, improper Latin. \
A variation of the ordinary lorem ipsum text has been used in typesetting since \
the 1960s or earlier, when it was popularized by advertisements for Letraset \
transfer sheets. It was introduced to the Information Age in the mid-1980s by \
Aldus Corporation, which employed it in graphics and word-processing templates \
for its desktop publishing program PageMaker.".split()

print(words[:5])


common_words = {}

for word in words:
	if word not in common_words:
		common_words[word] = 0
	common_words[word] += 1

print(common_words)


for k, v in sorted(common_words.items(),
	key = lambda x: x[1],
	reverse = True) [:5] :
    
    print(k,v)

print("\nusing counter")
print(Counter(words).most_common(5))


lst = list(range(10000000))
deq = deque(range(10000000))

def insert_delete(ds):
	for _ in range(10):
		index = random.choice(range(100))
		ds.remove(index)
		ds.insert(index,index)

print(datetime.now())
insert_delete(lst)
print(datetime.now())

insert_delete(deq)
print(datetime.now())

