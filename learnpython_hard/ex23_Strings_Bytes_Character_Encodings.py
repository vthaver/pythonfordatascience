#Exercise 23 LPTHW: Strings, Bytes, and Character Encodings

#This exercise is supposed to teach me how python handles and stores human language
#The functions below go through each line of a txt file and show you the encoded version of what is written and then the decoded version

import sys #Import the functions available in the sys repository/library
script, input_encoding, error = sys.argv #Initialize these three variables from values passed in the command line

#This function iterates through each line of the file and applies the print _line function to it  
#It also passes the variables (initiated at the command line and passed with argv) into the print_line function
def main(language_file, encoding, errors):
	line = language_file.readline() #assigns the latest line in the open file
	
	if line: #If the line exists the following code is run. this iterates through the whole file
		print_line(line, encoding, errors) #runs the print_line function on he latest line
		return main(language_file, encoding, errors) #runs the main funciton again as long as there is a line left

		
def print_line(line, encoding, errors):
	next_lang = line.strip() #Strips leading and trailing white spaces from the line and trailing \n, and assigns it the the next_lang variable
	raw_bytes = next_lang.encode(encoding, errors = errors) #raw_bytes is the line (called next_lang) encoded as "encoding" and specified errors = errors
	cooked_string = raw_bytes.decode(encoding, errors = errors) #cooked_string is raw_bytes line (encoded next_lang) decoded as and specified errors = errors
	
	#each line is printed as raw and cooked
	print(raw_bytes, "<===>", cooked_string)
	
languages = open("languages.txt", encoding = "utf-8")

main(languages, input_encoding, error)