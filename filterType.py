# Given arguments
sI = 45
mI = 100
bI = 455
eI = 0
spI = -23
sS = "Rubber baby buggy bumpers"
mS = "Experience is simply the name we give our mistakes"
bS = "Tell me and I forget. Teach me and I remember. Involve me and I learn."
eS = ""
aL = [1,7,4,21]
mL = [3,5,7,34,3,2,113,65,8,89]
lL = [4,34,22,68,9,13,3,5,7,9,2,12,45,923]
eL = []
spL = ['name','address','phone number','social security number']
'''
Write a program that, given some value, tests that value for its type.
Integer
If the integer is greater than or equal to 100, print "That's a big number!" 
If the integer is less than 100, print "That's a small number"
String
If the string is greater than or equal to 50 characters print "Long sentence." 
If the string is shorter than 50 characters print "Short sentence."
List
If the length of the list is greater than or equal to 10 print "Big list!" 
If the list has fewer than 10 values print "Short list."
'''
number = spI
my_string = eS
my_list = lL
if isinstance(number, int):
    if number >= 100:
        print "That's a big number!"
    elif number < 100:
        print "That's a small number"  
if isinstance(my_string, str):
    if len(my_string) >= 50:
        print "long sentence" 
    elif len(my_string) < 50:
        print "short sentence"
if isinstance(my_list, list):          
    if len(my_list) >= 10:
        print "Big list!"
    elif len(my_list) < 10:
        print "Short list"    