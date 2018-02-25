#Exercise 25 LPTHW: Even More Practice

#Returns a list of words in the sentence
def break_words(stuff):
	"""This function will break up words for us."""
	words = stuff.split(' ') #splits the string into a list of substrings separated by the ' ' in the original string
	return words

#Returns a list of things sorted alphanumerically
def sort_words(words):
	"""Sorts the words"""
	return sorted(words) #sorted sorts words

#Returns the first item in a list
def print_first_word(words):
	word = words.pop(0) #Pop removes the item indicated in a list
	print(word)

#Returns he last item in the list	
def print_last_word(words):
	"""Prints the last word after popping it off"""
	word = words.pop(-1)
	print(word)

#Returns a list of the words in the input sentence sorted alphanumerically
def sort_sentence(sentence):
	"""Takes in a full sentence and returns the sorted words"""
	words = break_words(sentence)
	return sort_words(words)

def print_first_and_last(sentence):
	"""Prints the print first and last words in a sentence"""
	words = break_words(sentence)
	print_first_word(words)
	print_last_word(words)
	
def print_first_and_last(sentence):
	"""Sorts the words then prints the first and last words"""
	words = sort_sentence(sentence)
	print_first_word(words)
	print_last_word(words) 
	


