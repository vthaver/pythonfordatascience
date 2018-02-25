#Exercise 32 LPTHW: Loops and Lists

#Learn how to tell python to do things repetitively and store the output in lists

the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

#This first type of for-loop goes through a list
#number is a created variables that takes the value of the item in the list that the for loop as iterated to
for number in the_count:
	print(f"This is count {number}")

#Same as above

for fruit in fruits:
	print(f"A fruit of type: {fruit}")
	
#Also, we can go through mixed lists too
for i in change:
	print(f"I got {i}")

#We can also build lists, first start with an empty one
elements = []

#Then us the range function to do 0 to 5 counts
for i in range(0,6):
	print(f"Adding {i} to the list.")
	#Append is a function that lists understand
	elements.append(i)
	
#Now we can print them out too

for i in elements:
	print(f"Elements was: {i}")
	
