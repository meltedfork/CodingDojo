'''Compare the two objects x and y and return an integer according to the outcome. The return value is negative if x < y, zero if x == y and strictly positive if x > y.'''

list_one = [1,2,5,6,2]
list_two = [1,2,5,6,2]
print cmp(list_one, list_two)
# returns 0, meaning exactly equal to each other

list_one = [1,2,5,6,5]
list_two = [1,2,5,6,5,3]
print cmp(list_one, list_two)
# returns -1, meaning not equal

list_one = [1,2,5,6,5,16]
list_two = [1,2,5,6,5]
print cmp(list_one, list_two)
# returns 1, meaning not equal

list_one = ['celery','carrots','bread','milk']
list_two = ['celery','carrots','bread','cream']
print cmp(list_one, list_two)
# returns 1, meaning not equal
