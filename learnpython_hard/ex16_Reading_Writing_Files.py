#Exercise 16 LPTHW: Reading and Writing Files

#Learn to read write files. remember think of a file as a linear DVD

#Make a text editor

from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you do not want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?") #Does not pass input to a variable. This just allows user to have a chance to cancel the program.

print("Opening the file...")
target = open(filename, 'w') #This puts the DVD into the DVD player, and makes sure the player has write capabilities

print("Truncating the file. Goodbye.")
target.truncate() #Deletes the contents of the file

print("Now I'm going to ask you for three lines.")

line1 = input("Line1: ")
line2 = input("Line2: ")
line3 = input("Line3: ")

print("I am going to write these to a file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

target.close() #Take dvd out of the player

#Open it to see you work!
print(f"And now we get to see {filename}:")
txt = open(filename)
print(txt.read()) 

print("And finally, we close it.")
txt.close()

