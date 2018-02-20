#Exercise 15 LPTHW: Reading Files

#This code shows two ways we can open anther file specified by input from the user

from sys import argv

script, filename = argv #Pass the first argument as the filename to be opened

txt = open(filename) #Before reading a file, you must open it into a variable

print(f"Here's your file {filename}:" #Uses the argv variable to pass to the string
print(txt.read()) #Prints the read file

#This code does the same thing but uses the explicit user input form the command line
print("Type the filename again:")
file_again = input('> ')

txt_again = open(file_again)

print(txt_again.read())