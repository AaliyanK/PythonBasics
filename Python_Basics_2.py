# IF STATEMENTS

old = False
Licence = True

if old:  # Automatically assume TRUE
    print('bumba')
elif Licence:
    print('weeeee')
else:
    print('yikes')  # yikes will be print out because old is NOT true

# Ternary Operator - conditional expressions
# condition_true if condition else condition_if_else - checks middle first then outputs the sides

is_friend = True
can_message = "message allowed" if is_friend else "not allowed to message"
# if "is_friend" is true - output can_message, otherwise, "not allowed to message"

# Short Circuiting

is_user = True

if is_friend or is_user:  # use "or" when there are two possible conditions
    print("best friends forever")

# LOGICAL OPERATORS

print(4 > 5)  # will return boolean
print(4 == 5)  # boolean return
print(0 != 1)  # NOT EQUAL TO
print(not False)  # we will get the opposite of it

# EXCERSISE
is_magician = False
is_expert = True

if is_magician and is_expert:
    print("You are a master magician")
elif is_magician and not is_expert:
    print("Atleast you're getting there")
else:
    print("You need magic Powers")

# is vs ==

print(True == 1)  # Will return true, will convert both into the same type bool(1)
print(10 == 10.0)  # Will return true - Converts both to same type

# IS checks if the location in memory where value is stored is the same
print(True is 1)
# So in order for "IS" to return "True" it must be the EXACT same value, no type conversions
print('1' is 1)
print([] is 1)
print([] is [])  # LISTS WILL ALWAYS RETURN FALSE

# FOR LOOPS!!

for item in [1, 2, 3, 4, 5]:  # item is a temporary variable, in "iterable"
    for x in ['A', 'b', 'c']:
        print(item, x)  # first the inner parts of the loop are run in nested loops

# Iterables - list, dictionary, tuple, string etc. INTS ARE NOT ITERABLE
# Iterated - one by one check each item in the collection

# ITERATING WITH DICTIONARIES

user = {
    "name": 'Golem',
    "age": 5006,
    "can_swim": False
}

for x in user.items():  # .items() will return the keys/values in a tuple
    key, value = x  # tuple unpacking
    print(key, value)

# same thing as above

for key, value in user.items():
    print(key, value)

for x in user.values():  # .values() will return the values only
    print(x)

for x in user.keys():  # .keys() will return the keys only
    print(x)

# COUNTER EXCERSISE

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
running = 0
for x in my_list:
    running = x + running
print(running)

# RANGE FUNCTION

for number in range(0, 10, 2):  # start stop step - how many times you want to loop
    print(number)  # will print numbers up till 10 BUT NOT INCLUDING 10

for bckwds in range(10, 0, -1):  # reverse the count
    print(bckwds)

for _ in range(2):  # loop twice
    print(list(range(10)))  # print two lists with a range of 10

# ENUMERATE FUNCTION

# RETURNS AN INDEX AND THE ITERABLE IN A TUPLE
for i, char in enumerate("Helloooooo"):
    print(i, char)

print(" ")

for i, char in enumerate([1, 2, 3]):
    print(i, char)  # use when we need an index counter

print(" ")

# to find an index of a specific value
for i, char in enumerate(list(range(100))):
    if char == 50:
        print(i)

print(" ")
# WHILE LOOPS!!!!!!


i = 0  # need to have a starting point for while loops
while i < 10:  # to jump out of a while look either BREAK or make the condition FALSE
    print(i)
    i += 1  # make sure you add this to increase the main condition value - INCREMENT
else:  # will access else after the first condition is met!, else only works when there is no BREAK
    print("done all the work")

# While loops and For Loops - both CAN do the same thing
# USE While loops when we arent sure how many times we would like to loop - maybe use while for emails

my_list = [1, 2, 3]

for item in my_list:
    print(item)

print(" ")

i = 0  # HAVE TO CREATE A VARIABLE THEN INCREMENT IT
while i < len(my_list):
    print(my_list[i])  # indexes the my_list starting at 0
    i += 1  # will output 1,2,3

print(' ')

# MOST USEFUL WAY TO USE WHILE LOOPS - MEMORIZE THIS
while True:
    response = input("Say something ")
    if response == "bye":
        break  # break ONCE the input is "bye"

print(" ")

# BREAK, CONTINUE, PASS Keywords
bum = [1, 2, 3]

for item in bum:
    print(item)
    break  # once the loop happens one time, it will break and not work anymore
    continue  # as soon as program sees continue, it will go back to the top of the loop
    pass  # use it as a placeholder

print(" ")
# MAKING A GUI!

picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]
]

# Iterate over array
# if 0 --> print " "
# if 1 -> print "*"

for row in picture:
    for number in row:
        if number == 1:
            print("*", end=" ")  # everytime you print, it creates a new line
        else:
            # use end when you want it on the same lines (HORIZONTAL
            print(" ", end=" ")
    print(" ")  # this adds spacing to every ROW or X (VERTICALLY)

print(" ")
# DUPLICATES EXERCISE

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
emptylist = []
for x in some_list:
    if some_list.count(x) > 1:
        emptylist.append(x)

for x in emptylist:
    if emptylist.count(x) > 1:
        emptylist.remove(x)
print(emptylist)

print(" ")


# FUNCTIONS - keeping your code dry - PARAMETERS

def say_hello(name, emoji):  # defining the function
    print(f'helloo {name} {emoji}')


# call the function - arguments will be passed into function
say_hello('Andrew', 'cry')
# These were positional arguments because they had to be in the specific position to work

# KEYWORD ARGUMENTS - dont worry about position

say_hello(emoji="bumba", name='gang')  # assign so that position doesnt matter


# DEFAULT PARAMETERS IN A FUNCTION - assigned in the function - use when there is no user input

def say_hello(name='Default', emoji='name'):
    print(f'helloo {name} {emoji}')


say_hello()

print(" ")


# RETURN WITH FUNCTIONS

def add(num1, num2):
    def func(num1, num2):
        return num1 + num2  # FUNCTION EXITS AND RETURN THE EXPRESSION

    return func  # need to return the function if we are dealing with nested functions


# a function should do one thing really well, and a function should return something

total = add(4, 5)  # CAN SAVE THE FUNCTION RETURN INTO A VARIABLE
print(total)


# EXERCISE

def checkDriverAge(age=0):
    # age = input("What is your age?: ")

    if int(age) < 18:
        print("Sorry, you are too young to drive this car. Powering off")
    elif int(age) > 18:
        print("Powering On. Enjoy the ride!")
    elif int(age) == 18:
        print("Congratulations on your first year of driving. Enjoy the ride!")


# 1. Wrap the above code in a function called checkDriverAge(). Whenever you call this function, you will get prompted for age.
# Notice the benefit in having checkDriverAge() instead of copying and pasting the function everytime?
checkDriverAge()

# 2 Instead of using the input(). Now, make the checkDriverAge() function accept an argument of age, so that if you enter:
checkDriverAge(92)
# it returns "Powering On. Enjoy the ride!"
# also make it so that the default age is set to 0 if no argument is given.


# Methods work with .something() - built in objects
'hello'.capitalize()

print(' ')


# DOCSTRINGS WITH FUNCTIONS - for instructions
def test(a):
    '''
    Info about function
    '''
    print(a)


test('bumba')
help(test)  # will output the docstring
print(test.__doc__)


# CLEAN CODE
def odd_even(num):
    if num % 2 == 0:
        return True
        return False  # we dont need a else statement, because True will be skipped if it isnt True


print(odd_even(50))  # with return statements we have to print

print(" ")


# *ARGS **KWARGS

def superfunc(*args, **kwargs):
    total = 0
    for items in kwargs.values():  # accesses all the values (5,10)
        total += items  # total will equal the additive of all the values
    return sum(args) + total  # sum of args is 15


# use args when there are multiple input arguments into the function
print(superfunc(1, 2, 3, 4, 5, num1=5, num2=10))
# kwargs create a dictionary like: {'num1':5, 'num2':10}

# function rules: parameters, *args, default params, **kwargs

print(" ")

# FUNCTION EXERCISE

emlist = []


def highest_even(list):
    print(list)
    for item in list:
        if item % 2 == 0:
            emlist.append(item)
    return max(emlist)


print(highest_even([10, 2, 3, 4, 8, 11]))  # print the highest even number

print(" ")

# SCOPE - what variables do I have access to?
# a variable not inside of a function is a GLOBAL function - we have access
# a variable inside of a function cannot be accessed outside of the function - local scope
# rules - local (inside deep function) - parent local (the outer function) - global (not in a function)

# Referring to a variable inside a function - GLOBAL KEYWORD

total = 0


def count(total):
    total += 1
    return total


# count(1) - count(2) - count(3) - will return 3
print(count(count(count(total))))

# NONLOCAL variable - will use the parent local variable (outer function)

rates = input('Please Enter The Number of Supplier Rates')
rates = int(rates)
