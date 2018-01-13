# SLIDE - GENERAL PURPOSE, INTERPRETED, HIGH LEVEL
# SLIDE - INTERPRETER 
# SLIDE - WHERE IT'S USED
# SLIDE - COMMUNITY 

# statments are everything that can make up 1+ lines of code

# expressions are statements that specifically evaluate to a value that is returned
# print 'hello world!' is an expression that returns the contents of the string 'hello world' to the standard output

# Anaconda installed a python environment along with a few different integrated development environments (IDEs) and some math/sciene/stats pacakges

# Spyder
# Jupyter Notebook
# python REPL/interpreter [python/python -c]

# we can also edit our code in a text editor and run it using the python interpreter


'''
> HELLO WORLD <
'''

print 'hello world!'



'''
> THE KOAN OF PYTHON <
'''

# let's take a look at THE KOAN OF PYTHON 
import this



'''
> CODE COMMENTS <
'''

# comments should really only be used when its really not obvious what your code is doing
# python is so easy to read, almost just like English, that there's no need to comment extensively
# comment maintenance can be burdensome. Before you write comments, make sure your code couldnt be refactored to be simpler

'''
this is a multiline comment
we can put as many lines of comment between these triple quotes as we want!
these comments are often used to document what a function or class does
'''

# this is a single line comment! Everything after the # is a comment, everything before is evaluated
print 'hi' # this line would print 'this' to the standard output, and this comment would be completed ignored by the interpreter!



'''
> VARIABLE TYPES <
'''

# variable types in python

# this loops through all the different variable types in Python and prints them
import types
for var_name in vars(types):
    if 'Type' in var_name:
        print var_name

# we are going to be concerned with the following types:
# - Booleans: True or False values
# - Strings: ordered collections of characters
# - Ints/Floats: numeric values, integer of floating point
# - Lists: ordered collections of anything
# - Tuples: list lists, but cannot be changed once declared
# - Dicts: key value pairs
# - Functions: blocks of code the execute some logic and return a value, can take input arguments
# - Classes: blueprints for making objects withe methods and properties; the core of Object Oriented Programming.



'''
> DECLARING VARIABLES <
'''
# we declare variables by name and set their value using the '=' assignment operator

my_first_var = 'Hello'
my_second_var = "Hi"
my_third_var = 2
my_fourth_var = True
my_fifth_var = 36.2

# python is dynamically typed; this means that is determines the type of the variable for you automatically given the context
# that the var is declared in and the value passed to the var
print type(my_first_var)
print type(my_second_var)
print type(my_third_var)
print type(my_fourth_var)
print type(my_fifth_var)

# variable naming conventions: all lowercase, starting with a letter or underscore, with underscores between words
# don't use special characters! don't use dashes!
# naming standards: https://www.python.org/dev/peps/pep-0008/

my_var = 1
invalid-var = 1
0invalid_var = 1
invalid_var@ = 1

# you can declare mutiple variables at once
name, age, sex = 'Arjun', 33, 'M'

# || YOU DO ||
# declare 'name', 'sex', and 'age' variables with your own information



'''
> STRINGS <
'''

# strings are ordered collections of characters which are enclosed in single or double quotation marks

# - DECLARATION -
my_string = 'this'
# or
my_string = "this"


# - RETURNING VALUES -
my_string
#vs
print my_string
# why are these different?

# try this:
my_string = 'first line\nsecond line'

my_string
#vs
print my_string
# why are these different?


# - SPECIAL CHARACTERS - 
# these characters, called string literals, return a special designated string when printed, instead of just their character contents

# \n - newline
# \t - tab
# \' - escaped single quote
# \" - escaped double quote

print 'first line\n\ttabbed second line\n\'I can use single quotes if I escape them\''

# you can get unicode characters outside of the standard alphanumeric characters by using
# strings starting with "u" to indicate unicode, and \u[unicode char number] for unicode symbols references
# here are a ton of unicode character code mappings: http://unicode.org/charts/

ustring = u'I have to get to work, \u2602 or \u2600..\u2639'
print ustring

# || YOU DO ||
# declare a string that returne the following between START OUTPUT > and > END OUTPUT when printed (quotation marks and new lines included!)
# START OUTPUT >
# "We may have all come on different ships, but we're in the same boat now."
#     - MLK
# > END OUTPUT
# SOLUTION: quote = '"We may have come on different ships, but we\'re in the same boat now."\n\t- MLK'; print quote

# || YOU DO ||
# replace the double quotes in the above string with special character \u2036 (open quotation), and \u2033 (closed quotation)
# SOLUTION: print u'\u2036We may have come on different ships, but we\'re in the same boat now.\u2033\n\t- MLK'


# - MULTILINE STRINGS -
multiline_string = '''
my name is Arjun
and I'm a teacher at General Assembly
'''
# or
multiline_string = """
my name is Arjun
and I'm a teacher at General Assembly
"""


# - STRING CONCATENATION -
# string can simply be added together

str_1 = 'In the beggining, '
str_2 = 'there was Assembly'

str_3 = str_1 + str_2
print str_3

str_4 = "PROLOGUE: "
str_4 += str_3
print str_4

# In order to add non-string vars with strings, you must convert them to strings first
# this is not always the most elegant way to combine variables and string (see STRING SUBSTITUION below)
print 'Here is a string plus a number: ' + str(5)

# || YOU DO ||
# print a string that says "my name is [your name], and I am [your age] years old" using the 'name' and 'age' vars declared before


# - TEXT TRANSFORMATIONS -

sentence = "I aim to become a Python hacker!"
sentence.upper()
sentence.lower()
sentence.capitalize()

# some methods allow you to chain one method after another. It runs the methods in order, outputing the resultant value
# chaining is also possible with some but not all methods in other types

sentence = "i AIm tO BeCoMe a PytHOn HaCkEr!"
sentence.lower().capitalize()
sentence = sentence.lower().capitalize()


# - STRIPPING -
# allows the removal of trailing space or characters around string

padded = '\t    There area a lot of spaces and tabs around this string\'s contents    \t\t'
padded.strip()
padded.lstrip()
padded.rstrip()

num_padded = '00000why are there zeros surrounding this string?0000'
num_padded.strip('0')


# - SPLITTING -
# a string can be split into substrings, which are then returned as a list

# split at every space (default)
sentence.split()

# split at every 'a'
sentence.split('a')

# split string into individual characters
list(sentence)

# || YOU DO ||
# take the string below, remove the trailing spaces on the left and the trailing repititions of the word 'end' from the rigth then split it into words
weird_string = '\n\t   well~isn\'t~this~a~weird~string?endendend'
# SOLUTION: 'weird_string.lstrip().rstrip('end').split('~')'


# - SLICING -
# slicing takes three positional arguments: starting index (inclusive), ending index (exclusive), skipping - how many positions to skip each time
# arguments are separted by ':' and placed within square brackets

sentence[2:5]
sentence[:5]
sentence[5:]
sentence[:]
sentence[::2]

# || YOU DO ||
# unscramble the message in scrambled
# hint 1: the first letter of the hidden message is 'y'
# hint 2: the message is embedded in scrambled at regular intervals
scrambled = 'T{vSzXyJ^osatoCJuWZOurtwnDi cAIxMFhXkB\\caaoTpLVnvSqIppfe_TYDAc TrJrbamRuPvGPas[rGqWniqfduIahZ_YvVgHxWpVheXDYy_{dsIur{^ L[hQTrt`j^n`voaPKzpF IIOnWodrxpEcjehcThaTcbtoJZ`obH[aSZdEuVfT[eK]fptE TfcCs]t[RX]e\\hxcgtOairYORWcsNNekoB wqp^FmsHRkExGenyRlrGnUc\\pTrtgW{rHheUYOIUJnUREozScYjwH\\ae'
# SOLUTION: 'scrambled[6::7]'


# - SEARCHING -

paragraph = '''In the works of Tarantino, a predominant concept is the distinction between
ground and figure. In a sense, Sartre suggests the use of rationalism to attack
colonialist perceptions of sexuality. Marx uses the term ‘subcapitalist
materialism’ to denote the rubicon, and subsequent futility, of conceptualist
class.

“Society is used in the service of class divisions,” says Derrida. Thus,
Sargeant[1] suggests that the works of Tarantino are
empowering. The main theme of Finnis’s[2] model of
rationalism is the role of the participant as artist.'''

# to check for simple presence of a substring
'Tarantino' in paragraph

# to get the index of the first instance from the left
paragraph.find('Tarantino')

# from the right
paragraph.rfind('Tarantino')

# || YOU DO ||
# read the full documentation for 'str.find': https://docs.python.org/2/library/stdtypes.html#str.find
# find the index of the second 'of'
# SOLUTION: 
"""
first_index = paragraph.find('of')
paragraph.find('of', first_index + 1)
"""

# - REPLACEMENT -
# how do we remove a word from the middle of a string? how do we replace it?

# || YOU DO ||
# looks at str.replace method: https://docs.python.org/2/library/stdtypes.html#str.replace and try to replace the first 'th' with 'the' and make the string all lowercase other than the first word
quote = 'In th End, we will remember not the words of our Enemies, but the silence of our Friends.'
# SOLUTION 'quote.lower().capitalize().replace('th', 'the', 1)' or 'quote.lower().capitalize().replace('th ', 'the ')'


# - STRING SUBSTITUTION -
# strings containing '{}' characters can have those characters replaced with variable value. 
# the '{}' can contain values that determine the index of the var to be inserted, or it's name
#  A string with '{}' values is called a template string as it's the template from which string can be formatted with inserted var values
# more on this: https://pyformat.info/

print 'my name is {} and I am {} years old'.format('Arjun', 33)
print 'I want to subsitute the {1} and {0} value in a different order'.format('second', 'first')
print 'Your name is {name}, today is {day_of_week} and we are in the {class_name} class'.format(name='Sara', day_of_week='Saturday', class_name='Introduction to Python Bootcamp')

# || YOU DO ||
# Generate a multiline template string in the form of a short letter that uses the values of the following variables, and sign your nickname in capital letters
# - variables called 'day_of_week', 'favorite_color', 'nickname', and 'salutation'. 
# SOLUTION:
"""
my_string = \
'''Dear nobody,

I'm writing you this {day_of_week} to let you know that my favorite color is {favorite_color}.
That is all.

{salutation},

{nickname}'''.format(day_of_week='Saturday', favorite_color='black', salutation='Regards', nickname='Arjuan'.upper())
print my_string
"""



'''
> INTEGERS AND FLOATS <
'''

# ints and floats are some of the most commonly used numeric types. There are a few others but they are
# not used very often unless you are doing math with imaginary numbers, or math with very large or very
# small numbers

# - DECLARATION -
# any numbers with a single decimal place will be typed as a float
# any numbers without a decimal place will be typed as an int

my_int = 10
my_float = 1.6

type(my_int)
type(my_float)


# - OPERATORS -

# + addition
# - subtraction
# * multiplication
# / division
# ** power
# % remainder on division

# when you divide integers by other integers, it will only return whole integer values (rounded down)
my_int / 3
my_int % 3


# - CONVERSION -

# conver int to float
type(my_int/1.)
type(my_int*1.)

# convert float to int
int(my_float)
type(int(my_float))


# - MAXIMUM SIZES -

import sys
sys.maxint
sys.float_info

# || YOU DO ||
# what happens when you add 1 to sys.maxint?
# what happens when you multiply 'sys.float_info[0]' (the max size) by 2?
# SOLUTION: it creates a Long type integer which has a larger maximum size and larger memory footprint
# SOLUTION: any value greate than the max flaot size is considerd 'inf', the largest float value ('-inf' is the smallest float value)

# - INCREMENTING/DECRIMINTING IN PLACE -
# you can use the arithmatic operators along with the assignment operator to modify numeric values in place

my_int += 2
my_int
my_int -= 1
my_int
my_int *= 6
my_int
my_int /= 2
my_int


# - ROUNDING FLOATS -
# y
import math
math.ceil(3.14157)
math.floor(6.62607004)

# you can see the truth: the float point is stored as the nearest finite sum of fractions whose denominators are powers of two.
round(3.14157)
round(3.14157, 3)

# - ORDER OF OPERATIONS -
# python arithmatic operators have a set order of operations. you can use the parentheses operator '()' to set an order

# HIGHEST PRESIDENCE
#  ()
#  **
#  *
#  /
#  +
#  -
# LOWEST PRESIDENCE


# || YOU DO ||
# calculate the surface area of a square-based pyramid with
# here is the equation: http://lmgtfy.com/?q=surface+area+of+a+pyramid
# HINT: square root is simply a value to the power 0.5
# - height = 225
# - base_width = 200
# - base_length = 200
#SOLUTION:
"""
h=225
w=200
l=200
area = l * w + l * ((w / 2) ** 2 + h ** 2 + w) ** 0.5 + w * ((l / 2) ** 2 + h ** 2) ** 0.5
print area # 138569.73882953462
"""



'''
> LISTS <
'''

# list contain heterogenous sets of variables in strict order, and can be mutated, added to, or removed from
my_list = ["string", 20, True, 36.33, [0,1,2]]
tic_tac_toe_pos = [[0,1,1],
                   [1,2,0],
                   [0,2,0]]

# indexing lists
my_list[0]
my_list[-2]
my_list[0:1]
my_list[::3]

# indexing multidimensional lists
row0 = tic_tac_toe_pos[0]
row0_col2 = tic_tac_toe_pos[0][2]

# reversing lists
my_list[::-1]
my_list
my_list.reverse()
my_list

# sorting lists
out_of_order = [0,6,2,7,8,3,1]
out_of_order.sort()
out_of_order

# changing values by index
my_list[3]
my_list[3] = 'changed'
my_list


# insert / remove
colors = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
colors.insert('Red-Orange', 1)
colors.remove('Red-Orange')
popped_color = colors.pop(-1)
print popped_color, colors
del colors[1]

# appending / extending
topics = ['Statistics', 'Biology', 'Architecture', 'Microeconomics', 'Computational Complexity', 'Studio Art', 'Composition']
# append takes the value you pass it and adds it as the next index in the list
topics.append('English')
# extend takes the value you pass it as an array, and adds the contents of that array to the end of the list\
topics.extend(['French'])
# what happens when you run this?
topics.extend('World History')

# unpacking lists
topic1, topic2 =  topics[0:2]
print topic1, topic2

# TUPLES
# tuples are just list lists except they are a fixed length and the values are immutable. this makes them more computationally effeceient at scale than lists
# which can be dynamically sized
my_tuple = ('Yes', 'No', 'Maybe')
# none of these
my_tuple[0] = 'Oui'
my_tuple.append('Sort of')

# DICTS
# dicts store key value pairs, where the key must be a string, and the value can be any var type. The keys are ambiguously ordered, unlike indicies in lists

my_dict = {
    'first_name': 'Arjun',
    'last_name': 'Ray',
    'birthday': {
        'year': 1984,
        'month': 'September',
        'day': 11
    },
    'fav_colors': [
        'black',
        'red'
    ],
    'alive': True,
}

# pretty printing a dict
# JSON (JavaScript Object Notation) is a nearly universal data format that uses key value pairs. Python dicts are interconvertable to this data type which is essentially a string that other
# langs can parse back into data objects
import json
print json.dumps(my_dict, indent=4)

# indexing 
my_dict['first_name']
my_dict['birthday']
my_dict['birthday']['year']

# lists of keys, value
my_dict.keys()
my_dict.values()
# notice how order of keys is not static.. do not count on the order of keys in a dictionary!

# changing a key value
my_dict['alive'] = False

# adding a new key value pair
my_dict['occupation'] = 'instructor'

# removing a key value pair
occupation = my_dict.pop('occupation')
print occupation, my_dict

del my_dict['alive']
print my_dict


# BOOLEANS
# booleans are simply True and False values. when you use a logical operateor for a set of expressions, it will return a boolean value


# https://www.tutorialspoint.com/python/python_basic_operators.htm
# == - equal in value
# !== and <> - not equal in value
# is - identity
# and - and operator
# or - or operator
# not - inverse modifier
# < - less than
# > - greater than
# <= - less than or equal to
# >= - greater than or equal to
# in - membnership operator

True and False

False and False

True or False

True == False
True == True
5 == 5

num1 = 5
num2 = '5'
num1 == num2

5 < 6
6 > 5

6 >= 6

5 in [1, 2, 3, 4, 5]
'5' in [1, 2, 3, 4, 5]
'5' not in [1, 2, 3, 4, 5]

'my_key' in {'first_key': 0, 'my_key': 1}

# CONTROL FLOW
# control flow is a way of breaking up the flow of execution in a program based on logical conditions

# SLIDE - CONTROL FLOW
# SLIDE - CONTROL FLOW TYPES https://en.wikipedia.org/wiki/Control_flow

#IF STATEMENTS

if some_logic_statement:
    # do something

if 5 > 4:
    print '5 is greater than 4'

if 5 < 4:
    print '5 is less than 4'


my_val = 20

if my_val > 10:
    print 'greater than 10'
elif my_val < 0:
    print 'is negative'
else:
    print 'neither greater than 10 nor negative'

my_val = 2

# WHILE
# while loops should be used when you wan to wait for some process that takes an unknown ammount of time to finish
# if you know how many loop iterations you want, consider using a for loop instead


import time
import random
milliseconds = 0
max_milliseconds = random.randint(20, 200) 

while milliseconds <= max_milliseconds:
    print '{} milliseconds elapsed'.format(milliseconds)
    time.sleep(0.1)
    milliseconds +=1

# FOR
# for loops are used when you have a known number of loops you want to perform
# you can use for loops to iterate through all of the elements in a list or other iterable type

for n in range(0,200):
    print n

our_list = ['hi', 'there', 'how', 'are', 'you?']

for item in our_list:
    print item

for index, item in enumerate(our_list):
    print 'index of item: {}\nvalue of item: {}\n'.format(index, item)

# how might we iterate through the first 4 items in a list of length 8?

our_dict = {
    'robots': 0,
    'ninjas': 1
}

for key in our_dict:
    print key

for key, value in our_dict.iteritems():
    print 'key: {}\nvalue: {}\n'.format(key, value)

# we can iterate through keys and values of a dictionary, but unlike a list, their order is not guaranteed

for char in 'hello':
    print char


# LIST COMPREHENSIONS

