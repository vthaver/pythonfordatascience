#Exercise 17 LPTHW: More Files

#Python script to copy one file to another

from sys import argv #Importing module (feature) that lets you pass arguments from the command line when starting python/script
#os.path is a library of functions that works with your directory to et information about the path of a file
from os.path import exists #Exists is a function that returns True/False based on if the argument is a file path exists

script, from_file, to_file = argv #Want to initiate the file we are copying from and the file we are creating

print(f"Copying from {from_file} to {to_file}")

in_file = open(from_file) #Put dvd int he dvd player
indata = in_file.read() #Only gonna play items

print(f"The input file is {len(indata)} bytes long")

print(f"Does the output file exist? {exists(to_file)}") #Returns True or false if the output file exists in the directory you are working in or specify
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w') #Open file to write. THis automatically truncates any file with the same name in the wd
out_file.write(indata) #Writes the data from the from_file into the out

print("Alright, all done copying.")

out_file.close()
in_file.close()

print(f"Opening {to_file} to view results")
view_out_file = open(to_file)
print(view_out_file.read())

view_out_file.close()

print("Done and closed")

