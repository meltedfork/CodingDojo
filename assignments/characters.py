'''
Find Characters
# input
word_list = ['hello','world','my','name','is','Anna']
char = 'o'
# output
new_list = ['hello','world']

Write a program that takes a list of strings 
and a string containing a single character, 
and prints a new list of all the strings containing that character.
'''
words = ['hello','world','my','name','is','Anna', 'Montana']
char = 'o'
new_words = []
for word in words:
    if char in word:
        print word
        new_words.append(word)
print new_words        
