# Exercise 6 LPTHW: Strings and Text

types_of_people = 10
# create fstring with variable placeholder
x = f"There are {types_of_people} types of people"

binary = "binary"
do_not = "don't"

y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

# fstrings can call on variables that are f strings themselves (which also call on variables)
print(f"I said: {x}")
print(f"I also said: '{y}'")

hilarious = False

joke_evaluation = "Isn't that joke so funny?! {}"

# .format inserts its argument into the variable space of the string
print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)


# extra try and break items
# can you add two fstrings together?
print(y + x)

# can you have multiple arguments with .format?
vish_identification = "Vishnu is {} feet tall, with {} eyes, and {} hair"
my_eyes = "Dark Brown"
my_height = 6
my_hair = "Black"

print(vish_identification.format(my_height, my_eyes, my_hair))

