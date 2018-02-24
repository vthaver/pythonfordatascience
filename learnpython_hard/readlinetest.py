file = open("ex16_Sample.txt")
for x in [0,1,2,3]:
	data = file.readline()
	print(data, end = "")
	
file.close()