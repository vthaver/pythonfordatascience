#Exercise 33 LPTHW: While Loops

#While loops keep running the block of code until the boolean statement after the while is false

i = 0
numbers = [] #initializes list

while i < 6:
	print(f"At the top i is {i}")
	numbers.append(i)
	i = i + 1
	print("Numbers now: ", numbers)
	print(f"At the bottom i is {i}")
	
print("The numbers: ")

for num in numbers:
	print(num)