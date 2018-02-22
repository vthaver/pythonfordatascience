#Exercise 17 LPTHW: More Files. But shorter this time

#Python script to copy one file to another

from sys import argv #Importing module (feature) that lets you pass arguments from the command line when starting python/script
#os.path is a library of functions that works with your directory to et information about the path of a file
from os.path import exists #Exists is a function that returns True/False based on if the argument is a file path exists

script, from_file, to_file = argv #Want to initiate the file we are copying from and the file we are creating

indata = open(from_file).read() #Put dvd int the dvd player


out_file = open(to_file, 'w').write(indata) #Open file to write. THis automatically truncates any file with the same name in the wd

view_out_file = open(to_file)
print(view_out_file.read())

view_out_file.close()


