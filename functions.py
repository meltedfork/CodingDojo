'''
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

family = [2,4,10,16]
def multiply(family, num):
    new_gen = []
    for people in family:
        new_gen.append(people * num)
        #print 'new_gen is', new_gen
    print new_gen
#multiply(family, 5)

a = [2,4,10,16]
def multiply(a, num):
    new_a = []
    for parts in a:
        new_a.append(parts * num)
    return new_a
b = multiply(a, 5)
print b, 'b'
'''
def layered_multiples(arr):
    #arr = multiply(a, num): this doesnt work
    print arr
    
def multiply(a, num):
    #creating new array to hold list * num results
    new_array = []
    for parts in a:
        #multiplying each number in list by num
        #storing results in new array
        new_array.append(parts * num)
        #print new_array
    return new_array
        #new_array expected result [6,12,15]
    multiply([2,4,5],3) #:ran inner function seperately to check for errors
#x = layered_multiples(multiply([2,4,5],3))
#print x
# expected output
#[[1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
'''
def func_1():
    name = input('What is your name?')
    return name
def func_2():
    user_input = func_1()
    print(user_input)

func_2()
'''