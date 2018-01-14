"""                                            -------------
-----------------------------------------------| K   E   Y |----------------------------------------------------
|                                              -------------                                                   |
|    '''                                                                                                       |
|    > MAIN SECTION <           a main topic                                                                   |
|    '''                                                                                                       |
|                                                                                                              |
|    # - SUBSECTION -           a subtopic within a main topic                                                 |
|                                                                                                              |
|    # || WE DO ||              a section where you will insert code along with the instructor                 |
|                                                                                                              |
|    # || YOU DO ||             a section where you will be tasked to solve a code problem with your team      |
|                                                                                                              |
----------------------------------------------------------------------------------------------------------------

--------------------
HOW TO USE THIS FILE
--------------------
After going through some introductory slides, we will be spending the majority of our workshop time looking at the
examples and problems within this file. The purpose of this file is to hold all of the relevant topical information
and code snippets that we will run during class. You should not try to run this file. Instead, you should be writing
code snippets during code-alongs and code-problems into the appropriate sections of this file, and executing the code
in the REPL by copying and pasting from here/

Each topic/subtopic will be explored in three sections:
-------------------------------------------------------

"I DO"
For a given topic/subtopic, the instructor will introduce the important ideas, and may use slides or the whiteboard to
demonstrate certain points.

"WE DO"
Then, the instructor will code and the class will code along simultaneously in order to demonstrate details about the
topic and to give you experience writing code with the new concepts. Save the code that you write in the appropriate
section!  These snippets of saved code will both be your classwork and your takeaway notes for future reference.

"YOU DO"
Every so often, there will be a YOU DO section which synthesizes concepts from the past topic(s) and challenges you
to solve a code problem using those concepts. You will be working in teams of 2-3 to solve problems and you will be
given a set amount of time to try and answer the question. It would be easiest if one person per team actually writes
code and this person can switch from one YOU DO section to another so that each team member gets time to write code.
During the YOU DO section, the teacher and TAs will be circulating to try and assist you if you hit a roadblock. After
the alloted time, the instructor will demonstrate the answer to the question.
______________________________________________________________________________________________________________________
"""



'''
> HELLO WORLD <
'''
# this simple statement demonstrates all of the elements of the Read, Evaluate, Print loop (REPL)
# READ - read in the statement below as typed by the user
# EVALUATE - run the 'print' method and take it's argument 'hello world'
# PRINT - takes the result yielded by EVALUATE and prints it to the standard out
# LOOP - you can enter more statements to evaluate which will start the loop again

# || WE DO ||

'''
> THE KOAN OF PYTHON <
'''
# let's take a look at THE KOAN OF PYTHON. More about 'import' after this...

# || WE DO ||

'''
> IMPORTING MODULES <
'''
# modules are pre-packaged bundles of code that provide us with functions, variables, and classes. Some modules come
# bundled with Python as part of the standard library, while others come from packages that optionally can be installed
# module import syntax

import os
import sys

# || WE DO ||

# we can also import modules and alias them to other names
import numpy as np
# || WE DO ||


'''
> CODE COMMENTS <
'''
# comments should really only be used when its really not obvious what your code is doing.
# python is so easy to read, almost just like English, that there's no need to comment extensively.
# comment maintenance can be burdensome. before you write comments, make sure your code cannot just be simplified first

'''
this is a multiline comment
we can put as many lines of comment between these triple quotes as we want!
these comments are often used to document what a function or class does
'''

# this is a single line comment! Everything after the # is a comment, everything before is evaluated
print 'hi' # this line will print 'this' to the standard output, and this comment will be ignored by the interpreter!



'''
> VARIABLE TYPES <
'''
# variable types in python

# this loops through all the different variable types in Python and prints them
# || WE DO ||

    
# we are going to be concerned with the following types:
# - Booleans: True or False values
# - Strings: ordered collections of characters
# - Ints/Floats: numeric values, integer of floating point
# - Lists: ordered collections of anything
# - Tuples: list lists, but cannot be changed once declared
# - Dicts: key value pairs
# - Functions: blocks of code the execute some logic and return a value, can take input arguments
# - Classes: blueprints for making objects with methods and properties; the core of Object Oriented Programming



'''
> DECLARING VARIABLES <
'''
# we declare variables by name and set their value using the '=' assignment operator

# || WE DO ||

# python is dynamically typed; this means that is determines the type of the variable for you automatically given the
# context that the var is declared in and the value passed to the var

# || WE DO ||

# variable naming conventions: all lowercase, starting with a letter or underscore, with underscores between words don't
# use special characters! don't use dashes!
# naming standards: https://www.python.org/dev/peps/pep-0008/
my_var = 1
invalid-var = 1
0invalid_var = 1
invalid_var@ = 1

# you can declare multiple variables at once
# || WE DO ||


# overwriting a variable is as simply as reassigning it
# || WE DO ||


# || YOU DO ||
# declare 'name', 'sex', and 'age' variables with your own information



'''
> STRINGS <
'''
# strings are ordered collections of characters which are enclosed in single or double quotation marks


# - DECLARATION -

# || WE DO ||


# - LENGTH -
# the length of the string

# || WE DO ||


# - RETURNING VALUES -

my_string
# vs
print my_string
# are these different?

# || YOU DO ||
# look ath the contents of 'my_string' by both printing it and just entering it's name. what is the difference? why?
my_string = 'first line\nsecond line'


# - SPECIAL CHARACTERS -
# these characters, called string literals, return a special designated string when printed, instead of just their
# character contents

# \n - newline
# \t - tab
# \' - escaped single quote
# \" - escaped double quote

# || WE DO ||

# you can get unicode characters outside of the standard alphanumeric characters by using
# strings starting with "u" to indicate unicode, and \u[unicode char number] for unicode symbols references
# here are a ton of unicode character code mappings: http://unicode.org/charts/
# || WE DO ||


# || YOU DO ||
# declare a string that returns the following between START OUTPUT > and > END OUTPUT when printed (quotation marks and
# new lines included!)
# START OUTPUT >
# "We may have all come on different ships, but we're in the same boat now."
#     - MLK
# > END OUTPUT

# || YOU DO ||
# replace the double quotes in the above string with special character \u2036 (open quotation), and \u2033 (closed
# quotation)


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

str_1 = 'In the beginning, '
str_2 = 'there was Assembly'
# || WE DO ||

# In order to add non-string vars with strings, you must convert them to strings first
# this is not always the most elegant way to combine variables and string (see STRING SUBSTITUTION below)
# || WE DO ||

# || YOU DO ||
# print a string that says "my name is [your name], and I am [your age] years old" using the 'name' and 'age' vars
# declared before


# - TEXT TRANSFORMATIONS -

sentence = "I aim to become a Python hacker!"
# || WE DO ||


# some methods allow you to chain one method after another. It runs the methods in order, outputting the resultant value
# chaining is also possible with some but not all methods in other types
sentence = "i AIm tO BeCoMe a PytHOn HaCkEr!"
# || WE DO ||



# - STRIPPING -
# allows the removal of trailing space or characters around string

padded = '\t    There are a lot of spaces and tabs around this string\'s contents    \t\t'
# || WE DO ||


num_padded = '00000why are there zeros surrounding this string?0000'
# || WE DO ||


# - SPLITTING -
# a string can be split into substrings, which are then returned as a list

# split at every space (default)
sentence.split()

# split at every 'a'
# || WE DO ||

# split string into individual characters
# || WE DO ||

# || YOU DO ||
# take the string below, remove the trailing spaces on the left and the trailing repetitions of the word 'end' from the
# right then split it into words
weird_string = '\n\t   well~isn\'t~this~a~weird~string?endendend'


# - SLICING -
# slicing takes three positional arguments: starting index (inclusive), ending index (exclusive), skipping - how many
# positions to skip each time.
# arguments are separated by ':' and placed within square brackets.

# || WE DO ||

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
# || WE DO ||

# to get the index of the first instance from the left
# || WE DO ||

# from the right
# || WE DO ||

# || YOU DO ||
# read the full documentation for 'str.find': https://docs.python.org/2/library/stdtypes.html#str.find
# find the index of the second 'of'



# - REPLACEMENT -
# how do we remove a word from the middle of a string? how do we replace it?

# || YOU DO ||
# looks at str.replace method: https://docs.python.org/2/library/stdtypes.html#str.replace and try to replace the first
# 'th' with 'the' and make the string all lowercase other than the first word
quote = 'In th End, we will remember not the words of our Enemies, but the silence of our Friends.'


# - STRING SUBSTITUTION -
# strings containing '{}' characters can have those characters replaced with variable value.
# the '{}' can contain values that determine the index of the var to be inserted, or it's name.
# a string with '{}' values is called a template string as it's the template from which string can be formatted with
# inserted var values.
# more on this: https://pyformat.info/

# || WE DO ||

# || YOU DO ||
# Generate a multiline template string in the form of a short letter that uses the values of the following variables,
# and sign your nickname in capital letters
# - variables called 'day_of_week', 'favorite_color', 'nickname', and 'salutation'.



'''
> INTEGERS AND FLOATS <
'''
# ints and floats are some of the most commonly used numeric types. There are a few others but they are not used very
# often unless you are doing math with imaginary numbers, or math with very large or very small numbers


# - DECLARATION -
# any numbers with a single decimal place will be typed as a float.
# any numbers without a decimal place will be typed as an int.

# || WE DO ||


# - OPERATORS -

# + addition
# - subtraction
# * multiplication
# / division
# || WE DO || power
# % remainder on division

# when you divide integers by other integers, it will only return whole integer values (rounded down)
# || WE DO ||


# - CONVERSION -

# convert int to float
# || WE DO ||

# convert float to int
# || WE DO ||


# - MAXIMUM SIZES -

import sys
sys.maxint
sys.float_info

# || YOU DO ||
# what happens when you add 1 to sys.maxint?
# what happens when you multiply 'sys.float_info[0]' (the max size) by 2?
# SOLUTION: it creates a Long type integer which has a larger maximum size and larger memory footprint
# SOLUTION: any value greater than the max float size is considered 'inf', the largest float value ('-inf' is the smallest
# float value)


# - INCREMENTING/DECREMENTING IN PLACE -
# you can use the arithmetic operators along with the assignment operator to modify numeric values in place

# || WE DO ||

# - ROUNDING FLOATS -

# you can round floats to their nearest integer value using 'math.ceil' and 'math.floor'
# || WE DO ||


# you can round floats to a set number of decimal places using 'round'.
# there are some issues with representing base 10 numbers as binary numbers, what the computer actually stores.
# these issues can show up in rounding: https://docs.python.org/2/tutorial/floatingpoint.html
round(3.14157) # default number of decimal places is 0
# || WE DO ||


# - ORDER OF OPERATIONS -
# python arithmetic operators have a set order of operations. you can use the parentheses operator '()' to set an order

# HIGHEST PRECEDENCE
#  ()
#  **
#  *
#  /
#  +
#  -
# LOWEST PRECEDENCE

# || YOU DO ||
# calculate the surface area of a square-based pyramid with
# here is the equation: http://lmgtfy.com/?q=surface+area+of+a+pyramid
# HINT: square root is simply a value to the power 0.5
# - height = 225
# - base_width = 200
# - base_length = 200



'''
> LISTS <
'''
# list contain heterogenous sets of variables in strict order, and can be mutated, added to, or removed from


# - DECLARATION -

# || WE DO ||

# two-dimensional list
# || WE DO ||


# || YOU DO ||
# how would you declare a 3-dimensional list?
# take the two 2-d lists below and put them together into a list called 'list3'
list1 = [['Irish Wolfhound', 'Great Dane'], ['Beagle', 'Collie'], ['Chihuahua', 'Toy Poodle']]
list2 = [['Tiger', 'Lion'], ['Jaguar', 'Bobcat'], ['Ocelot', 'Maine Coon']]


# - LENGTH -
# the length of the list

len(my_list)


# - INDEXING / SLICING -
# since lists have a set element order, you can select elements by index, or slice parts of them, just like with strings

# || WE DO ||

# indexing multidimensional lists
# || WE DO ||

# || YOU DO ||
# index the 'Jaguar' value from 'list3' above


# - LIST ORDERING -

# reversing lists
# || WE DO ||


out_of_order = [0,6,2,7,8,3,1]

# returning a new sorted list
# || WE DO ||

# in place sorting
# || WE DO ||


# - ADDING/DELETING/CHANGING VALUES -

# changing values by index
# || WE DO ||


# you can insert values into an existing list at a certain index
colors = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
# || WE DO ||

# you can remove a list element by it's value
# || WE DO ||

# or you can remove a list element by it's index
# || WE DO ||


# || YOU DO ||
# what is the difference between using the pop method on a to remove a list item vs the del statement?

# appending / extending list are related but different methods to add values to the end of a list
topics = ['Statistics', 'Biology', 'Architecture', 'Microeconomics', 'Computational Complexity', 'Art', 'Composition']

# append takes the value you pass it and adds it as the next index in the list
# || WE DO ||

# extend takes the value you pass it as an array, and adds the contents of that array to the end of the list
# || WE DO ||

# || YOU DO ||
# what happens when you run this? why?
topics.extend('World History')

# || YOU DO ||
# replace the colors 'Red' and 'Orange' from 'colors' with 'Red-Orange' and add 'Ultraviolet' and 'X-Ray' to the end of
# the list


# - UNPACKING -
# you can get the values from a list and set them declare multiple vars with those values simultaneously
# || WE DO ||



'''
> TUPLES <
'''
# tuples are just list lists except they are a fixed length and the values are immutable. this makes them more
# computationally efficient at scale than lists, which can be dynamically sized

# || WE DO ||

# none of these will work since tuples are immutable and fixed length
my_tuple[0] = 'Oui'
my_tuple.append('Sort of')

# we can see that tuples are more efficient if we run the following to
# see how long declaring either type takes when run 10 million times

import timeit
timeit.timeit("x=(1,2,3,4,5,6,7,8)", number=10000000)
timeit.timeit("x=[1,2,3,4,5,6,7,8]", number=10000000)

# see how many operations each requires when the commands are disassembled into assembly
import dis
def a():
   x=(1,2,3,4,5,6,7,8)
def b():
   x=[1,2,3,4,5,6,7,8]
dis.dis(a)
dis.dis(b)



'''
> DICTS <
'''
# dictionaries store key value pairs, where the key must be a string, and the value can be any var type. The keys are
# ambiguously ordered, unlike list indices


# - DECLARATION -
# dicts use curly braces to enclose key value pairs, where the key is a quotation enclosed string, and the value is
# written however the type you'd like to assign to the key is normally written. instead of using '=' to assign values,
# dicts use ':', and the key value pairs are separated with a comma.

# || WE DO ||


# - PRETTY PRINTING A DICT -
# JSON (JavaScript Object Notation) is a nearly universal data format that uses key value pairs. Python dicts are
# interconvertible to this data type which is essentially a string that other language can parse back into data objects.
# JSON tools also allow us to print out data structures in more readable ways

# || WE DO ||


# - INDEXING -

# dictionary values are selected by their key name
# || WE DO ||

# dictionaries can be nested inside of dictionaries
# || WE DO ||


# - LISTING KEYS AND VALUES -

my_dict.keys()
my_dict.values()

# || YOU DO ||
# make a dictionary with a bunch of keys in non alphabetical order called 'test'
# look at output from 'test.keys()'. what do you notice?


# - ADDING / REMOVING / CHANGING KEY VALUES -

# changing a prexisting key value
# || WE DO ||

# adding a new key value pair
# || WE DO ||

# removing a key value pair with pop
# || WE DO ||


# removing a key value pair with del
# || WE DO ||


# || YOU DO ||
# rename 'alive' key in 'my_dict' to 'hungry;
# HINT: you aren't actually renaming the key. Think about the add/remove methods above


# - JSON TO DICT -
# you can easily load JSON data directly into a python dictionary as the two data structures are interconvertible

json_string = \
'''{
   "id": "0001",
   "type": "donut",
   "name": "Cake",
   "ppu": 0.55,
   "batters":
       {
           "batter":
               [
                   { "id": "1001", "type": "Regular" },
                   { "id": "1002", "type": "Chocolate" },
                   { "id": "1003", "type": "Blueberry" },
                   { "id": "1004", "type": "Devil's Food" }
               ]
       },
   "topping":
       [
           { "id": "5001", "type": "None" },
           { "id": "5002", "type": "Glazed" },
           { "id": "5005", "type": "Sugar" },
           { "id": "5007", "type": "Powdered Sugar" },
           { "id": "5006", "type": "Chocolate with Sprinkles" },
           { "id": "5003", "type": "Chocolate" },
           { "id": "5004", "type": "Maple" }
       ]
}'''
cake_dict = json.loads(json_string)
print cake_dict['batters']['batter'][0]

# || YOU DO ||
# pretty print the 'topping' key array within 'cake_dict' with an indent of 5



'''
> BOOLEANS <
'''
# booleans are simply True and False values. when you use a logical operator for a set of expressions, it will return a
# boolean value


# - LOGICAL OPERATORS -

# ==           equal in value
# is           identity
# !== and <>   not equal in value
# <            less than
# >            greater than
# <=           less than or equal to
# >=           greater than or equal to
# and          and operator
# or           or operator
# not          inverse modifier
# in           membership operator


# - EQUALITY VS IDENTITY -
# equality '==' compares the values of the two statements, whereas identity 'is' compares whether or not the two
# statements refer to the same object

a = [1, 2, 3]

# this does not make a copy of 'a', but actually sets 'b' to point to 'a'
b = a

# both of these statements will be True
# || WE DO ||

# you can see that a and b are actually the same list as modifications of 'a' modify 'b' as well
# || WE DO ||

# to make a copy of a list, you can do
# || WE DO ||

# while the list have equality, they don't share identity
# || WE DO ||

# this point is further emphasized by the fact that modifications of 'a' are not reflected in 'c'
# || WE DO ||


# || YOU DO ||
# make the following comparisons
# 1) 4 is greater than 5
# 2) 5 is not equal to 4
# 3) 5 is greater than or equal to 4 and 4 is greater than or equal to 6
# 4) list 'a' shares identity with list 'b' or list 'a' shared identity with list 'c'


# - LOGICAL COMBINATIONS -

# statements joined with 'and' are all required to be True to return True, otherwise they return False
True and True
True and False
False and False
True and True and True and True and False

# statements joined with 'or' require any of the statements to be True to return True, otherwise they return False
True or False
False or False
False or False or False or False or True

# when you combine 'or', 'and', 'not', the following precedence is followed:
# more info on logical operator precedence: https://docs.python.org/2/reference/expressions.html#operator-precedence

# HIGHEST PRECEDENCE
# - not
# - and
# - or
# LOWEST PRECEDENCE

True and False or False
# equivalent to
(True and False) or False

not True and False or False
# equivalent to
(not (True and False)) or False


# - IN OPERATOR -
# the 'in' operator can be used to check if a value exists within a enumerable var
# enumerable vars include strings, lists, tuples, and dicts

# || WE DO ||

# || YOU DO ||
# try running this clever python easter egg and explain why it works
import this
love = this
this is love
love is True
love is False
love is not True or False
love is love



'''
> CONTROL FLOW <
'''
# control flow is a way of breaking up the flow of execution in a program based on logical conditions
# the main control flow statements are 'for', 'if/elif/else', and 'while'


# - IF STATEMENTS -
# if statements allow us to evaluate whether a logic statement is True, and if so, it will run the indented code block

if some_logic_statement_is_True:
   # do something

# || WE DO ||


# || YOU DO ||
# try running the statement below. why doesn't it work? Why not?
if 5 > 4:
print '5 is greater than 4'

# you can chain multiple conditions using 'elif' (else if) statements after an 'if'. the program will try each condition
# until it reaches one that evaluated to True, and only run the indented code block for that condition. if it passes
# through all 'if' and 'elif' conditions without a True evaluation, it will run the indented code block within the
# 'else' statement, if it is provided

# || WE DO ||

# || YOU DO ||
# write an if/elif/else block that will check if a string var called 'my_val2'
# 1) contains the letter 'a' -> print 'contains the letter a'
# 2) is greater than 5 characters long --> print 'is greater than 5 characters long'
# 3) else --> print 'oh well'
my_val2 = 'hello my name is'

# || YOU DO ||
# reverse the order of the first two conditions. what happens? why?

# - FOR -
# for loops are used when you have a known number of loops you want to perform
# you can use for loops to iterate through all of the elements in a list or other iterable type
# iterate through a range of numbers

for n in range(0,200):
   print n

# iterate through values in a list
our_list = ['hi', 'there', 'how', 'are', 'you?']
# || WE DO ||
   
# iterate through indices and values in a list
# || WE DO ||

# || YOU DO ||
# how might we iterate through the first 4 items in a list of length 8?

our_dict = {
   'robots': 0,
   'ninjas': 1
}

# iterate through keys in dict
# || WE DO ||

# iterate through keys and values in dict
# || WE DO ||

# iterate through string
# || WE DO ||

# you can break out of a for loop using 'break'
# || WE DO ||

# you can go to the next iteration without executing the rest of the code in the block using 'continue'
# || WE DO ||

# || YOU DO ||
# this is a famous programming interview question called FizzBuzz that was designed to filter out "the 99.5% of
# programming job candidates who can't seem to program their way out of a wet paper bag". Give it a shot!
# write a program that prints the numbers from 1 to 100. But for multiples of three print “Fizz” instead of the number
# and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five print “FizzBuzz”.



# - WHILE -
# 'while' loops should be used when you want to wait for some process that takes an unknown amount of time to finish.
# if you know how many loop iterations you want, consider using a 'for' loop instead. 'while' loops keep looping as long
# as the condition following the 'while' statement remains True.

# we will create a process that takes a (pseudo) random amount of time to finish
# || WE DO ||

# you can use 'break' and 'continue' with 'while' statements just like with 'for' statements



'''
> FUNCTIONS <
'''
# functions define blocks of code which take in arguments, perform some logical operations on those argument
# and then return something
# functions use the 'def' statement followed by a '()' containing comma separated parameters.
# all of the vars the function needs to execute should be passed in as parameters.
# evaluating a function definition does not run the function, simply creates the function object.
# the functions must be called using '[function name]([function arguments])' in order to run it.
# a function block execution finishes when it reaches the end of it's indented code block, or it hits a 'return'
# statement, which ends function execution and returns a value.

# || WE DO ||

# you can set default function parameters
# || WE DO ||

# functions can take a variable number of arguments as a list, after all of the individual named arguments
# || WE DO ||

# functions can also take a dictionary as arguments, after all of the individual named arguments, and list argument
# || WE DO ||


# || YOU DO ||
# write a function called 'print_if_key_in_list' that takes a 'prefix' argument with a default value of '\t', a list
# argument as '*args' and a dict arguments as '**kwargs'. for every key in kwargs, if the key is also in args, print
# the prefix and the key value.


# - SCOPE -
# the indented block of code inside a function 'def' statement is scoped to the function. this means that if you
# declare new variables inside of the function block, they will not be accesible outside the function block. However,
# you can access values of prexisting variable from the outer scope from within the function

# you can access the outer scope from inside the function, but you cannot modify it
# || WE DO ||



# you cannot change the var in the outer scope
# || WE DO ||



# the outer scope cannot access variables declared within the funciton
# || WE DO ||



# ADDITIONAL TOPICS

'''
> TRY, CATCH AND EXCEPTION HANDLING
'''

'''
> ADVANCED ENUMERABLE METHODS
'''
# map
# list comprehensions

'''
> CLASSES
'''
# classes and instances
# constructor
# class methods and properties
# instance methods and properties
# private methods/vars
# inheritance

'''
> READING AND WRITING FILES
'''

'''
> INSTALLING PACKAGES
'''
# get pip
# pip install
# pip list

'''
> EXAMPLE USEAGE: TEMPLATED EMAILER SCRIPT <
'''

'''
> EXAMPLE USEAGE: BASIC DATA ANALYTICS <
'''