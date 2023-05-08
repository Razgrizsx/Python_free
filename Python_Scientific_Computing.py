# Reserved Words ///////////////////////////////////////////////
#False, None, True, and, as, assert, break, class, if, def, del, elif,
#else, except, return, for, from, global, try, import, in,
#is, lambda, while, not, or, pass, raise, finally, continue, nonlocal, with, yield.
#/////////////////////////////////////////////////////////////////

 

#Create Virtual Environment/////////////////////////////////////////////////////////////
#python -m venv /path/to/new/virtual/environment#

x = 1
x = x + 1
x ** x #potencia
print(x)
f = None #Emptiness
string = 'string'
# and, or, not

x = ["apple", "banana"]
z = 0
print("banana" in x) #true (is not)
print(x is z) #true if both are the same object
print(x == z) #true if same value

'str'.lower() #lowercase

def functionName(arg):
    return arg

x = 5
if x < 10: 
    print('smaller')
if x > 10: 
    print('bigger')
elif x < 5:
    print('smaller than 5')
else: 
    print('else')    
a = 1
b = 2
y = 3
result = x if a > b else y #Ternary

n = 5

type(5)
float(n) #Convert to float
int(n) #Convert to integer
str(n)
list() # Into Array

list = [1,2,3,4,5,6,7,8,9,10]
print(list[0])
print(list[0:4])
2 in list #>True or False


max()
min()
len()#length
list.index()
#list_or_string_name.index(element, start_pos, end_pos)


isinstance(5, int) #5 es un integer?

try: print('hello')
except: print('bye') #Manage errors

ingreso = input('Who are you? ') # input stops and wait for the input to assign
print('Welcome ', ingreso)

while n > 0 :
    print(n)
    n = n - 1
print('Blastoff!')
sec = [1, 2, 3, 46, 6754, 324]
result = filter(lambda x: x >3, sec)

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

Chris = Person('Chris', 32)

while True:
    line = input('> ')
    if line == 'done':
        break  #break interrupts, continue comes back up
    print(line)
print('Done!')

for i in [1, 2, 3, 4, 5]:
    print(i)

smallest = None
for value in [9, 41, 12, 3, 74, 15]:
    if smallest is None:
        smallest = value
    elif value < smallest:
        smallest = value
    print(smallest, value)
print('After', smallest)


openFile = open('fileName') #(filename, mode ex: 'r' read) openfile is not the data

for data in openFile:   # reads the file each line at a time
    print(data)

for data in openFile:
    if data.startswith('From:') :
        print(data)

line.rstrip() # get rid of the right whitespace including new line

read = openFile.read() #reads the whole thing

'Hello\nWorld' # \n new line, counts as a character



range() #list of numbers

for i in range(len(list)):
    elemento = list[i]         #loop knowing the index unlike the other one
    
list.append('element')
list.sort()
sum('list goes here')


string.split() #lot of spaces like one
' '.join(list)

#Dictionaries///////////////////////////////////////////////////////////////////////////////

dictionarie = dict()
dictionarie['key'] = 'value'
'key' in dictionarie # true or false, check if key exist

print(list(list))
print(list.keys())
print(list.values())
print(list.items())

#count keys

counts= dict()
names = ['a', 'b', 'c', 'd']
for name in names:
    if name not in counts:
        counts[name] = 1
    else : 
        counts[name] = counts[name] + 1

#the same as above
for name in names:
    counts[name] = counts.get(name, 0) + 1

    counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
for key in counts:
    if counts[key] > 10:
        print(key, counts[key])

for aaa,bbb in list.items():
    print(aaa, bbb)                    # key value
                                       # key value etc                 

#tuples, like lists bun in parenthesis , diference is that the tuples are inmutables.////////////////////

t = (1, 2, 3, 4, 5)
print(t[1]) #'2'

(x, y) = ('first', 'second')
print(x) #first

(0, 1, 2) < (5, 1, 2) #true, first is true, it doesnt look at the others, if its equal it jumps to the next.

d = {'a': 10, 'c': 22, 'b': 1 }
sorted(d.items()) #[{'a': 10, 'b': 1, 'c': 22}]

for k,v in sorted(d.items()):
    print(k, v)

#sort by vallue
tmp = list()
for k,v in d:
    tmp.append((v, k))
tmp = sorted(tmp, reverse=True) #[(22, 'c'), (10, 'a'), (1, 'b')]

for k,v in d[:10]:  #limit the iteration to 10
    print(k, v)

[ (v,k) for k,v in d.items() ] #create list of tuples and can use it ex: sorted([ (v,k) for k,v in d.items() ])

#RegEx///////////////////////////////////////////////

import re # must import regular expression

# ^ matches beginning of a line
# $ matches end of the line
# . any character
# \s  whitespace
# \S non-whitespace
# * repeats a character zero or more times
# *?  repeats a character zero or more times (non-greedy)
# + repeats a character one or more times
# +? repeats a character one or more times (non-greedy)
#[aeiou] matches a single character in the listed set
#[^XYZ] matches a single character not in the listed set
#[a-z0-9] the set of characters can include a range
#(  string extraction begins
#)  string extraction ends

re.search() #see if a string matches a regular expression, true or false
re.findall() #extract portion of a string that matches regular expression, take whatever matches

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('From:', line):
        print(line) 

#re.search('^From:', line) # ^ starts with 'From:'
#X.*  starts with X and the serie of any kind of character

#Networking with python //////////////////////////////////////////////////////////////

#Support for tcp socket
import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect( ('data.pr4e.org', 80) )

#Refer to Web_Browser//

#Text Processing
# ord('H') 72 (ascii number)


import urllib.request, urllib.parse, urllib.error #Web Browser using a libray
fhand= urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())

#Web scraping
#pip install beatifulsoup4 
from bs4 import BeautifulSoup
url = input('Enter - ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

#retrieve tags
tags = soup('a')  #can call it to get the anchor tags
for tag in tags:
    print(tag.get('href', None))


#XML

#<people>
#<name>
# Chris
#<name/>
#<people/>

#XML validator 'XSD'

import xml.etree.ElementTree as ET

data = ''' 
    <people>
<name>
 Chris
<name/>
<people/>
'''
tree = ET.fromstring(data)
print('Name', tree.find('name').text)   #findall then for in for more than one

#JSON

import json

data = '''
    {
    name: 'Chris',
    age: 32
    }
'''
info = json.loads(data)
print('Name:', info['name'])

#API
#import oauth
#import hidden

#Objects
#Classes

class PartyAnimal:
    x = 0
    def party(self):
        self.x = self.x + 2
        print(self.x)

an = PartyAnimal()
an.party()
an.party()

#an.x = 4

class PartyAnimal:        #class with constructor (normal, set up variables) and destructor (rare), is automatic
    x = 0
    def __init__(self, name):
        self.name = name                #class with parameter its called s = PartyAnimal('Chris') s.name is Chris
        print('I am constructed')
    
    def __str__(self):                            #print(an) prints this                              
        print('This is an animal contstructor')

    def party(self):
        self.x = self.x + 2
        print(self.x)
    
    def __del__(self):                      # Called when destroyed (overwritten, ex an = 2, an is the instance)
        print('I am destructed', self.x)

class FootballFan(PartyAnimal): #Extends the PartyAnimal class, all its attributes and methods plus the following 
    points=0
    def touchdown(self):
        self.points = self.points + 7
        self.party()
        print(self.name, 'points', self.points)
    

f"{'Hola':*^5}\n" # Formatter *****Hola*****

def function(**kwargs):  #...arg
    return kwargs     #returns a dictionary with the arguments

#Web Scraping
quit() #stop execution
