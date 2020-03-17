print('weeee')
print('aaliyan kapadia')

answer = input('Name?')  # Asks for name
print("hello " + answer)  # Will print out the name

# DATA TYPES SECTION

# int - Represents all WHOLE numbers
# float - Represents decimal numbers
print(2 + 4)  # Will output 6
print(2 - 4)  # this will be type int because output is whole number
print(2 * 4)
print(type(2 / 4))  # the type of 6 will output "class float" because output is NOT whole number

print(2 ** 2)  # 2 raised to 2
print(2 // 4)  # returns an integer rounded down
print(5 % 4)  # returns the remainder of the division 5/4 = 1*1/4 - 1 is the remainder

# MATH FUNCTIONS
print(round(3.1))
print(abs(-23))

# VARIABLES
user_iq = 190
print(user_iq)  # will output 190

user_age = user_iq / 4  # operation with variable
# EXPRESSION IS PIECE OF CODE THAT OUTPUTS VALUE
# Statement is entire line of code

# AUGMENTED ASSIGNMENT OPERATOR

somevalue = 5
somevalue = somevalue + 2  # This will give us 7, but we can do it like below
somevalue += 2  # This is augmented assignment operator, can also do this with - / *
print(somevalue)  # answer will be 9

# STRINGS!!!
print('This is a string')
username = 'gang'
password = 'ganggang'
print(username)

# Different way - MAYBE for text pictures stuff:
long_string = ''''
WOW
O_O
'''
first_name = 'aaliyan'
last_name = 'kapadia'
full_name = first_name + " " + last_name
print(full_name)

# TYPE CONVERSION
print(str(100))  # this number is now a string due to the str(100)

# ESCAPE SEQUENCE!!
weather = 'It\'s funny'  # USE BACKSLASH WHEN apostrophe is used
yo = 'It\'s \"kind of funny\" lool'
hey = '\t Its pretty funny'  # \t ADDS A TAB!
LOL = 'yes you are \n CORRECT!'  # \N Adds a NEW LINE!

# Formatted STRINGS!!!
name = 'aaliyan'
age = 55
print('hello ' + name + ' you are ' + str(age) + ' years old')  # need to convert nums to str in string
print(f'hi {name} you are {age} years old')  # USE "f" BEFORE STRING TO MAKE THINGS EASIER

# STRING INDEXING IMPORTANT
# [start:stop:step]
selfish = 'me me me'
print(selfish[0:3])  # Grab selfish from index 0 up to BUT NOT INCLUDING 3
print(selfish[0:6:2])  # step by 2
print(selfish[2:])  # start at index 2 go all the way to the end
print(selfish[:5])  # start at the beginning and go up to but not including 5 index
print(selfish[-1])  # start at the end of the string
print(selfish[::-1])  # will reverse the string

# IMMUTABILITY - strings in python cannot be changed

selfish = 100  # strings CAN be reassigned, but cannot be indexed and changed
# We have to reassign the value to something else
selfish = '01234567'
selfish = selfish + '8'  # Will create a new string with '8' added to the 01234567
print(selfish)

# BUILT IN FUNCTIONS/METHODS
print(len('helllloooooo'))  # calculates the length of the string (12) - IT DOES NOT START FROM 0

quote = 'to be or not to be'
print(quote.upper())  # will uppercase the entire string
print(quote.capitalize())  # Capitalizes first words
print(quote.find("be"))  # will return the index of the first occurance where "be" is
print(quote.replace('be', 'me'))  # ('what you are replacing','replacement')
quote2 = quote.replace('be', 'me')  # Need to assign the quote to a new variable to ensure that it changes
print(quote2)

# BOOLEANNS
# will be True or False
name = 'Andrei'
is_cool = False
is_cool = True
print(bool(0))  # False
print(bool(1))  # True

# TYPE CONVERSION Exercise
birth_year = input('What is your birth year?')
age = 2019 - int(birth_year)
print(f'Your age is {age}')  # The main thing here was to convert the input string to an integer to do the calc

# PASSWORD CHECKER EXERCISE
username = input('What is your username?')
password = input('what is your password?')
fpass = '*' * len(password)
print(f'{username}, your password {fpass} is {len(password)} letters long')

# LISTS!!!!! - Store datatypes

li = [1, 2, 3, 4, 5]
li2 = ['a', 'b', 'c']
li3 = [1, 2, 'a', True]
amazon_cart = ['Notebooks', 'Sunglasses', 'toys', 'grapes']  # To access these we need to index them
print(amazon_cart[0])  # Will return Notebooks

# LIST SLICING [start:stop (NOT INCLUDING):step] - DOES NOT MAKE PERMANENT CHANGES - need to reassign
print(amazon_cart[:])  # Returns all
print(amazon_cart[0:2])  # Returns first 2
print(amazon_cart[0::2])  # Will skip every 2

amazon_cart[0] = 'laptop'  # We can reassign list items to something else
print(amazon_cart)

# CREATING A COPY OF A LIST:
amazon_cart[0] = 'laptop'
new_cart = amazon_cart[:]  # Will create 2 different lists (copy of a list)
new_cart[0] = 'gum'
print(new_cart)  # WILL HAVE "GUM"
print(amazon_cart)  # WILL HAVE "LAPTOP" BECAUSE COPY WAS CREATED

# MATRIX!!

matrix = [
    [1, 2, 3],
    [2, 4, 6],
    [7, 8, 9]
]  # a 3x3 matrix

print(matrix[0][1])  # This will print the matrix value in the first array (1,2,3) and the second position (2)

# LIST ACTIONS/FUNCTIONS

basket = [1, 2, 3, 4, 5]

print(len(basket))  # WIll output 5
basket.append('yay')  # will add it to the end of the  - cannot print this
print(basket)
basket.insert(2, 100)  # Insert a value (index, the value)
print(basket)
basket.extend([100, 1001])  # Extends our list with the two values
print(basket)

basket.pop()  # Will remove the last entry in the list (1001 will be removed) - CAN SAVE IT
print(basket)

basket.pop(0)  # Removes entry in 0 index (removes 1 from array) - POP WILL SAVE THE VALUE YOU POP
print(basket)

basket.remove(4)  # use this to remove an actual VALUE and not INDEX
print(basket)

basket2 = ['a', 'b', 'c', 'd', 'd', 'e']
print(basket2.index('c'))  # Will return the index where the value is in!

# FIND OUT IF SOMETHING IS IN A LIST/DICTIONARY/TUPLE
print('d' in basket2)  # Will return a True or False
print('i' in 'Hi my name is aaliyan')

print(basket2.count('d'))  # returns a count of how many times the item repeats itself

basket2.sort()  # Will sort the list for me
print(basket2)

newbasket = basket.copy()  # copies it for us
newbasket

basket2.reverse()
print(basket2)  # reverses the basket order

# COMMON LIST PATTERNS

print(list(range(1, 10)))  # use LIST to create a list from 1 - 10

new_sent = " ".join(['hi', 'my', 'name', 'is', 'jojo'])  # create a string out of list using JOIN
print(new_sent)

# LIST UNPACKING
a, b, c, *other = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # Will output "other" as 4-9
print(a)
print(b)
print(c)
print(other)

# DICTIONARIES - can contain lists and everything
diction = {
    'a': ['gang', 'sw'
                  'eet', 'woo'],
    'b': 'bumba',
    'x': 3
}  # has KEYS and VALUES
print(diction['b'])  # can extract the value by indexing the KEY
print(diction['a'][1])  # we choose the first key, and then index "1" to extract the value "sweet"

my_list = [{
    'a': [1, 2, 3],
    "yo": 'gang'
}, 'not a dict']
print(my_list[0]['a'][1])  # goes into first index, selects "KEY" "a" THEN SELECTS INDEX "1" - RETURNS 2

# Data structures: Use list when you need order, use dictionary when you dont need order - holds more info.

Imm = {
    123: ['gang', 'sweet', 'woo'],
    True: 'bumba',
    '[100]': True
}
# Dictionaries must be immutable, so you cannot make a key a list
# There can only be one key

# DICTIONARY METHODS
user = {
    'basket': [1, 2, 3],
    'greet': 'hello',
    'age': 20
}
print(user['basket'])

print(user.get('greet'))  # use this to check if a specific KEY exists - returns none or the value
print('basket' in user)  # Will return TRUE if KEY exists
print(user.get('bumba', 55))  # if the KEY bumba doesn't exist, assign it to VALUE 55

print('basket' in user.keys())  # will check the keys and return true/false
print('hello' in user.values())  # Will check the values and return true/false

print('hello' in user.values())
user2 = user.copy()  # will copy the dictionary

print(user.pop('greet'))  # removes 'greet'

print(user.update({'age': 55}))  # will update "age" from 20 to 55
print(user)

# TUPLES - lists but not modifiable
my_tuple = (1, 2, 3, 4, 5, 6)
print(my_tuple[1])
print(5 in my_tuple)

x, y, z, *other = (1, 2, 3, 4, 5, 6, 7)
print(x)
print(y)
print(z)
print(other)

print(my_tuple.count(4))  # count repititions of a value
print(my_tuple.index(6))  # what index is "6" in?

# SETS - unordered collections of unique objects
my_set = {1, 2, 3, 4, 5, 5, 5, 5}  # sets will remove any repeating values
print(my_set)
