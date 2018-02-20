# Exercise 10 LPTHW: Asking Questions

#This code plays around with passing values to variables with input() when prompted by a string being printed to the user. The variables will ultimately be used in an output string with placeholders for the variables

print("How old are you?", end = ' ')
age = input() #This prompts the user to enter something before the next line is processed
print("How tall are you?", end = ' ')
height = input()
print("How much do you weigh?", end = ' ')
weight = input()
mood = input("How do you feel? ") #Automatically prints a prompt for the user to input

print(f"So, you're {age} old, {height} tall and {weight} heavy. Also, you feel {mood}.") #Passes the input initiated variables into he string
