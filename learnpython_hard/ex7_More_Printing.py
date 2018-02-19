# Exercise 7 LPTHW: More Printing

print("Mary had a little lamb.")
print("It's fleece was white as {}".format('snow')) #format function inserts argument in variable placeholder
print("And everywhere that Mary went.") 
print("." * 10) # what did that do? Added 10 periods to the end....

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch that comma at the end. try and remove it to see what happens
print(end1 + end2 + end3 + end4 + end5 + end6, end=' ') #end is an argument in print that says what to do at the end of the print, default is probably new line
print(end7 + end8 + end9 + end10 + end11 + end12)

