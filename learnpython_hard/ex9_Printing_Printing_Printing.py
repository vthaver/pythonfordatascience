# Exercise 9 LPTHW: Printing Printing Printing
# This code shows two ways to make a string go on multiple lines

#First part of this code just lists the days and months by inserting a variable with the days/months into a string

days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug" # the \n characters will signify a new line I believe

print("Here are the days: ", days) #It will print the days on one line with spaces in between
print("Here are the months: ", months) #Print the months each on a new line

# second part of the code prints each new line on a new line maybe? What it actually does is allows the string to go on multiple lines, because python evaluates each new line as if it isn't a string unless you do the 3 quotes

print("""
	There is something going on here.
	With the three double-quotes.
	We'll be able to type as much as we like.
	Even 4 lines if we want, or 5, or 6.
""") 
