# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 13:29:00 2021

@author: sjfre
"""
#%% Comparison Operators
# True numerical
print(21 == 21)

# False numerical
print(21 == 42)

# True string
print('hello world' == 'hello world')

# False string
print('hello world' == 'Hello world')

# True with not operator
print('me' != 'you')

# True numerical of mixed type
print(42 == 42.0)

# False due to mixed type
print(21 == '21')

#%% Boolean Evaluation
# Valid Python but not to be used
print(True == True)
print(True != False)

# Valid Python and SHOULD be used
print(True is True)
print(True is not False)

# Equivalent If Statements
a = True

# Truth
if a is True:
    pass
if a is not False:
    pass
if a:
    pass

# False
if a is False:
    pass
if a is not True:
    pass
if not a:
    pass

#%% Boolean Operators
# 'and', 'or', and 'not' work with booleans

### Mixing Boolean & Comparison
# True && True
print((5 < 6) and (7 < 8))

# True && False
print((5 < 6) and (6 < 5))

# True || False
print((21 == 21) or (21 == 42))

#%% if/else Statements
name = 'Sam'
if name == 'Sam':
    print('Hi, Sam.')
else:
    print('Hello stranger!')
    
# elif Statements
age = 21
if name == 'Prof. Wang':
    print('Hello, Prof. Wang.')
elif age > 65:
    print('You are of retirement age!')
else:
    print('You are not Prof. Wang nor of retirement age.')
    
# while Loops
spam = 0
while spam < 5:
    print('Spam!')
    spam += 1
    
# break Statements
while True:
    name = input('Please type your name.')
    if name == 'your name':
        break
print('You followed directions!')

# continue Statements
while True:
    name = input('Who are you?')
    if name != 'Sam':
        continue
    print('Hello, Sam.')
    pwd = input('What is the \'password\'?')
    if pwd == 'password':
        break
print('Logged in!')

#%% for Loops and range()
print('My name is')
for i in range(7):
    print('Jimmy Seven Times ({})'.format(str(i)))
    
# range() with variable step
for i in range(0,20,4):
    print(i)
    
# for/else statement
for i in [0,2,4,6,8,10]:
    if i == 3:
        break
else:
    print('No 3 found.')
  
#%% import and random
import random, sys
while True:
    rand = random.randint(1,10)
    print(rand)
    res = input('Type exit to exit, or the number above to continue.')
    if res == 'exit':
        sys.exit()
    elif int(res) == rand:
        continue
    else:
        print('try again')
        
#%% Functions
def hello(name):
    print('Hello, {}!'.format(name))
    
hello('Sam')
hello('Prof. Wang')

import random
def getAnswer(num):
    if num == 1:
        return 'It is certain'
    elif num == 2:
        return 'It is decidedly so'
    elif num == 3:
        return 'Yes'
    elif num == 4:
        return 'Reply hazy try again'
    elif num == 5:
        return 'Ask again later'
    elif num == 6:
        return 'Concentrate and ask again'
    elif num == 7:
        return 'My reply is no'
    elif num == 8:
        return 'Outlook not so good'
    elif num == 9:
        return 'Very doubtful'

r = random.randint(1, 9)
print(getAnswer(r))

#%% None
# since print doesn't return anything, this will be true
spam = print('spam')
print(spam is None) 

#%% Scopes
def glo():
    global stri
    stri = 'Changed In Function'

stri = 'First Set'
print(stri)
glo()
print(stri)