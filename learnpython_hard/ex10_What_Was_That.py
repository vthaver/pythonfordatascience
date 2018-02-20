# Exercise 10 LPTHW: What was that
#This code is meant to explore the different escape string uses and in string codes"

tabby_cat = "\tI'm tabbed in." #Inserts a tab before the string
persian_cat = "I'm split\non a line" #Inserts a line break
backslash_cat = "I'm \\ a \\ cat" #Allows for the use of a backslash inside the string
experiment_cat = "I'm \v a \v cat" #experiment with different escape sequences

#This code makes a bulleted list: the line breaks are accomplished automatically by using the """ quotes, the tab  is accomplished by \t
#Also shows you can add a line without a literal line break
fat_cat = '''
I'll do a list:
\t* Cat Food
\t* Fishies
\t* Catnip\n\t* Grass 
'''

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)
print(experiment_cat)