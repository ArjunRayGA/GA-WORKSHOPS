# SLIDE - GENERAL PURPOSE, INTERPRETED, HIGH LEVEL
# SLIDE - INTERPRETER 
# SLIDE - WHERE IT'S USED
# SLIDE - COMMUNITY 

print 'hello world!'

# statments are everything that can make up 1+ lines of code

# expressions are statements that specifically evaluate to a value that is returned
# print 'hello world!' is an expression that returns the contents of the string 'hello world' to the standard output


# let's take a look at THE KOAN OF PYTHON 
import this

# Anaconda installed a python environment along with a few different integrated development environments (IDEs) and some math/sciene/stats pacakges

# Spyder
# Jupyter Notebook
# python REPL/interpreter [python/python -c]

# we can also edit our code in a text editor and run it using the python interpreter

'''
this is a multiline comment
we can put as many lines of comment between these triple quotes as we want!
these comments are often used to document what a function or class does
'''

# this is a single line comment! Everything after the # is a comment, everything before is evaluated
print 'hi' # this line would print 'this' to the standard output, and this comment would be completed ignored by the interpreter!

# comments should really only be used when its really not obvious what your code is doing
# python is so easy to read, almost just like English, that there's no need to comment extensively
# comment maintenance can be burdensome. Before you write comments, make sure your code couldnt be refactored to be simpler

# variable types in python


# this loops through all the different variable types in Python and prints them
import types
for var_name in vars(types):
    if 'Type' in var_name:
        print var_name


# we are going to be concerned with the following types:
# - Booleans
# - Strings
# - Ints/Floats
# - Lists
# - Tuples
# - Dicts
# - Functions
# - Classes


# DECLARING VARIABLES

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

my_var = 1
invalid-var = 1
0invalid_var = 1


# STRINGS

# declaration
my_string = 'this'
# OR
my_string = "this"

# returning values
my_string
#VS
print my_string
# why are these different?

# try this:
my_string = 'first line\nsecond line'

my_string
#VS
print my_string
# why are these different?

multiline_string = '''
my name is Arjun
and I'm a teacher at General Assembly
'''
# OR
multiline_string = """
my name is Arjun
and I'm a teacher at General Assembly
"""

# string concatenation
str_1 = 'In the beggining, '
str_2 = 'there was Assembly'
print str_1 + str_2

str_3 = str_1 + str_2
print str_3

str_4 = "PROLOGUE: "
str_4 += str_3
print str_4

# special chars

# \n - newline
# \t - tab
# \' - escaped single quote
# \" - escaped double quote

# unicode string; you can get unicode characters outside of the standard alphanumeric characters by using
# strings starting with u'' to indicate unicode, and \u[unicode symbol number] for unicode symbols
ustring = u'I have to get to work, \u2602 or \u2600..\u2639'
print ustring

# text transformations
sentence = "I aim to become a Python hacker!"
sentence.upper()
sentence.lower()
sentence.capitalize()

# chaining
sentence = "i AIm tO BeCoMe a PytHOn HaCkEr!"
sentence.lower().capitalize()
sentence = sentence.lower().capitalize()

# searching in string
paragraph = '''In the works of Tarantino, a predominant concept is the distinction between
ground and figure. In a sense, Sartre suggests the use of rationalism to attack
colonialist perceptions of sexuality. Marx uses the term ‘subcapitalist
materialism’ to denote the rubicon, and subsequent futility, of conceptualist
class.

“Society is used in the service of class divisions,” says Derrida. Thus,
Sargeant[1] suggests that the works of Tarantino are
empowering. The main theme of Finnis’s[2] model of
rationalism is the role of the participant as artist.'''

'Tarantino' in paragraph

# stripping
padded = '\t    There area a lot of spaces and tabs around this string\'s contents    \t\t'
padded.strip()
padded.lstrip()
padded.rstrip()

num_padded = '00000why are there zeros surrounding this string?0000'
num_padded.strip('0')

# splitting
# a string can be split into substrings, which are then returned as a list

sentence.split()
sentence.split('a')
list(sentence)

# slicing string
# slicing takes three positional arguments: starting index (inclusive), ending index (exclusive), skipping - how many positions to skip each time

sentence[2:5]
sentence[:5]
sentence[5:]
sentence[:]

# slicing and skipping
import random
hidden_message = 'you have managed to decode this sentence'
scrambled = ''
gap = 6
for i in hidden_message:
    for n in range(gap):
        scrambled += chr(random.randint(65, 123))
        print n
    scrambled += i
    print scrambled

scrambled = 'T{vSzXyJ^osatoCJuWZOurtwnDi cAIxMFhXkB\\caaoTpLVnvSqIppfe_TYDAc TrJrbamRuPvGPas[rGqWniqfduIahZ_YvVgHxWpVheXDYy_{dsIur{^ L[hQTrt`j^n`voaPKzpF IIOnWodrxpEcjehcThaTcbtoJZ`obH[aSZdEuVfT[eK]fptE TfcCs]t[RX]e\\hxcgtOairYORWcsNNekoB wqp^FmsHRkExGenyRlrGnUc\\pTrtgW{rHheUYOIUJnUREozScYjwH\\ae'
# unscramble the message in scrambled
# the first letter of the hidden message is 'y'
# the message is embedded in scrambled at regular intervals

scrambled[6::7]


# how do we remove a word from the middle of a string? how do we replace it?
# looks at str.replace method

# string substitution
# https://pyformat.info/

print 'my name is {} and I am {} years old'.format('Arjun', 33)
print 'I want to subsitute the {1} and {0} value in a different order'.format('second', 'first')
print 'Your name is {name}, today is {day_of_week} and we are in the {class_name} class'.format(name='Sara', day_of_week='Saturday', class_name='Introduction to Python Bootcamp')







# INTEGERS AND FLOATS

# declaration
my_int = 10
my_float = 1.6

type(my_int)
type(my_float)

# operators

# + addition
# - subtraction
# * multiplication
# / division
# ** power
# % remainder on division

# integer division and remainders
my_int / 3
my_int % 3

# conversion
type(my_int/1.)
type(my_int*1.)
int(my_float)
type(int(my_float))

# maximum sizes
import sys
sys.maxint
sys.float_info

# incrementing/decreminting in place
my_int += 2
my_int -= 1
my_int *= 6
my_int /= 2

# rounding floats

import math
math.ceil(3.14157)
math.floor(6.62607004)

round(3.14157)
round(3.14157, 3)



# LISTS
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

