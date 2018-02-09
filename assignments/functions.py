'''
ODD/EVEN
def odd_even(num):
    count = 1
    print count, num
    while count <= num:
        if count % 2 == 0:
            print 'Number is', count,'. This is an even number.'
            count += 1
        else:
            print 'Number is', count,'. This is an odd number.'
            count += 1
#odd_even(2000)

MULTIPLY
family = [2,4,10,16]
def multiply(family, num):
    new_gen = []
    for people in family:
        new_gen.append(people * num)
        #print 'new_gen is', new_gen
    print new_gen
#multiply(family, 5)

MULTIPLY v.2
a = [2,4,10,16]
def multiply(a, num):
    new_a = []
    for parts in a:
        new_a.append(parts * num)
    return new_a
b = multiply(a, 5)
print b, 'b'
'''
#HACKER
def multiply(a, num):
    print a, num
    arr = []
    for parts in a:
        arr.append(parts * num)
    return arr 

def layered_multiples(arr):
    print arr
    new_array = []
    i = 0
    while i < 3:
        new_array.append(arr[i] * '1')
        i += 1    
    print new_array

x = layered_multiples(multiply([2,4,5],3))
    
    
'''
    for parts in arr:
        #multiplying each number in list by num
        #storing results in new array
        new_array.append(len.arr[0], 1)
        #print new_array
    print new_array

    
     
    x = layered_multiples(multiply([2,4,5],3))
    print x
# expected output
#[[1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
'''