'''
list_one = [1,2,5,6,2]
list_two = [1,2,5,6,2]

print cmp(list_one, list_two)
#returns 0, meaning exactly equal to each other

list_one = [1,2,5,6,5]
list_two = [1,2,5,6,5,3]
print cmp(list_one, list_two)
#returns -1, meaning not equal because list_one < list_two

list_one = [1,2,5,6,5,16]
list_two = [1,2,5,6,5]
print cmp(list_one, list_two)
#returns 1, meaning not equal because list_one > list_two
'''
list_one = ['celery','carrots','bread','milk']
list_two = ['celery','carrots','bread','cream']
print cmp(list_one, list_two)
#returns 1, meaning not equal