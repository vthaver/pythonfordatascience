#Exercise 13 LPTHW: Parameters, Unpacking, Variables

# cover one more input method to pass variables to a script. You can use a python script with custom npouts without having to do user input one a a time for each variable.

from sys import argv #from the sys library import a feature...

# this line unpacks the argv variable
script, first, second, third = argv #The argv is the argument variable and it holds the arguments you pass to you script.
#apparently you have to pass th2nd trough n arguments into argv when you run you script: python script.py arg1 arg2 arg3

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)



