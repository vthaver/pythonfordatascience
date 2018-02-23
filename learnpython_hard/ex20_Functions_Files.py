#Exercise 20 LPTHW: Functions and Files

#This script explores the use of functions in reading and printing pars of a file

from sys import argv #argv is a system function that lets vales be passed through the command line when initiating the script

script, input_file = argv #This line unpacks the variable argv that is initialized in the command line

#This function takes its input file and applies the read function to it. ANd then prints the whole file
def print_all(f):
	print(f.read())

#This function sets the pointer in the open file to the first line
def rewind(f):
	f.seek(0)

#This function prints the line of an input file, the line printed is the next line that the file "pointer" is at	
def print_a_line(line_count, f):
	print(line_count, f.readline())

current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)	
		
		
