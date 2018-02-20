#Exercise 14 LPTHW: Prompting and Passing

from sys import argv

script, user_name = argv
prompt = '> '

# this code uses both argv and input together

print(f"Hi {user_name}, I'm the {script} script.") #Pulls from the argv passed in the initiation of the python script
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt) #Asks on new line started with '> '

print(f"Where do you live {user_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print(f'''
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
''')



