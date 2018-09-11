# This will briefly describe the syntax for different types of things in Python
# like lists, dictionaries, functions, statements etc.

# This is written for Python 2.7 - NOT Python 3. I know zero Python 3 ):

# Keep in mind that all indents are a must-have - it's more or less how Python implies the memory management

# __________________________________________________________________


# This is how you define a list:

your_new_list = []

# You define the name of the list (it is "your_new_list" here) and then its contents.
# Lists are ordered, meaning exactly what you input is exactly what you get out. For example:

your_new_list = [
	"Hello",
 	"World"
]

print your_new_list[0] # this gets into string indexing, very useful. I can write a separate doc for this if you want.
print your_new_list[1]

# That would print the string "Hello", then the string "World".

# That's enough about lists, now dictionaries.


# __________________________________________________________________


# Dictionaries work like a real-world dictionary. There are "keys" and "values".
# The key is to the left of the colon, the value is to the right:

your_new_dictionary = {} # empty dictionary (just to show what operator to use)

your_new_dictionary = {
	"Synonym": "A word that has ",
	"World": "Earth"
}

# Dictionaries are great for data structures


# __________________________________________________________________


# Let's get into functions:

def your_new_function():
	print "Hello World"
	# This is the EXACT syntax for a function without arguments. Adding arguments is a whole 'nother document :)


# __________________________________________________________________


# "If" statements:

x = 1
if x > 0:
	print "x is greater than 0"
else:
	print "x is not greater than 0"


# __________________________________________________________________


# "For" loops:

# I created a list (lists are iterable) to loop over

some_iterable_object = [
	"hey",
	"hello"
]

for item in some_iterable_object:
	print item
# this for loop will print "hey" then "hello"
# NOTE: dictionaries are not iterable meaning you cannot loop over them.


# _________________________________________________________________


# "While" loops (these are used for exit conditions mostly)

x = 1
while x != 2: 
	print "hello world"
	x += 1

# this is an awful while loop (functionally speaking), but the syntax is good

# _________________________________________________________________


# Classes:

class Some_Class:

	def __init__(self, argument): # the initialize function (defines what the object does/has when it is created, ALL classes have this initialize function)
		self.argument = argument # this is a generic parameter, but again all classes have the intialize function that looks very close to this

	def your_method(self):
		# some block of code

	def other_method(self):
		# some other block of code

# Notes: within classes, functions are called "methods". You would say "this class has these methods"


# _________________________________________________________________


# some super quick stuff you probably already picked up on:

"string", 'string' # both are strings (in a general sense there's no need to define str("string") or int(3) or float(4.5) - python implies this 9 out of 10 times)

variable_name = "some variable" # defining variables; simply name the variable, no other syntax needed

= # the = operator means "is assigned to", so in the code above, variable_name IS ASSIGNED TO the string "some variable".

== # this means "actually equals". Very specific operator, a Google search would probably get you the best description

function_name() # this is how you call a function you wrote. You would apply whatever parameters you've assigned within those parentheses.