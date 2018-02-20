#Exercise 8 LPTHW: Printing, Printing

# Initialize a string variable that has variable placeholders. Use .format as an easy way to create strings

formatter = "{} {} {} {}" # Initialize a string variable that has variable placeholders.

print(formatter.format(1,2,3,4)) #The .format function allows arguments (the numbers) to be passed into the varable placeholders of a string witch is called by the variable formatter
print(formatter.format("one","two","three","four")) #Passing strings rather than numbers into the string with variable placeholders
print(formatter.format(True, False, False, True)) #Pass the type true or false
print(formatter.format(formatter,formatter,formatter,formatter)) # It's going to return nothing (wrong! returns the curly brackets if nothing gets passed) because there were no variables passed into the formatter(2nd degree)
# This will print a sentence by inserting 4 separate strings into the placeholders of the formatter string
print(formatter.format(
	"Try your",
	"Own text here.",
	"Maybe a poem,",
	"Or a song about fear."
))

	

