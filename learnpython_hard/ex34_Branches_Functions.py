#Exercise 34 LPTHW: Branches and Functions

from sys import exit

def gold_room():
	print("This room is full of gold, How much do you take?")
	
	choice = input('> ')
	if "0" in choice or "1" in choice:
		how_much = float(choice)
	else:
		dead("Man, learn to type a number.") #Prints the string + god job, then exits the ....
	
	if how_much < 50:
		print("Nice, you're not greedy, you win!")
		exit(0)
	else:
		dead("You greedy bastard!")
		

def bear_room():
	print("There is a bear here.")
	print("The bear has a bunch of honey.")
	print("The fat bear is in front of another door.")
	print("How are you going to move the bear?")
	bear_moved = False #Initializes the bear as not being moved, so hat some action below will change that
	
	while True:
		choice = input('> ')
		
		if choice == "take honey":
			dead("The bear looks at you then slaps your face off.")
		elif choice == "taunt bear" and not bear_moved: #If you taunt the bear and the bear is not moved (Bear_moved = False)
			print("The bear has moved from the door.")
			print("You can go through it now")
			bear_moved = True
		elif choice == "taunt bear" and bear_moved:
			dead("The bear gets pissed off and chews your leg off.")
		elif choice == "open door" and bear_moved:
			gold_room()
		else:
			print("I got no idea what that means.")


def cthulhu_room():
	print("Here you see the great evil Cthulhu.")
	print("He, it, whatever stares at you and you go insane.")
	print("Do you flee for your life or eat your head?")
	
	choice = input('> ')
	
	if "flee" in choice:
		start() #Starts the door to your left and door to your right prompt
	elif "head" in choice:
		dead("Well that was tasty!")
	else:
		cthulu_room()

def dead(why):
	print(why, "Good Job!") #Prints the argument passed into the initialization of the functions
	exit(0) #Exits the program? Python
	
def start():
	print("You are in a dark room")
	print("There is a door to you right and a door to your left")
	print("Which door do you take?")
	
	choice = input('> ')
	
	if choice == "left":
		bear_room() # Run the bear function
	elif choice == "right":
		cthulhu_room() #Run the cthuhlu function  
	else:
		dead("You stumble around the room until you starve.") #Run the dead function, which prints something and exits the program
		
start() #run the function which eventually leads to running the rest of the functions
	
			
