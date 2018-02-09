# Multiples: Part 1
# range from 1-1000; using modulo to find odd numbers; print odd numberd
'''
for number in range(1, 1000):
    if number % 2 != 0:
        print number

# Multiples: Part 2
#range from 5-1000000; use modolo to find multiples of 5; print nums
for fiver in range(5, 1000000):
    if fiver % 5 == 0:
        print fiver

# Sum List
# sum the list and print result
numbers = [1, 2, 5, 10, 255, 3]       
print sum(numbers)
'''
# Average List
# sum list then divide by list length; print result
numbers = [1, 2, 5, 10, 255, 3]
print sum(numbers) / len(numbers)