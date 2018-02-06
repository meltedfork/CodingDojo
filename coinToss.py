'''
x = .23945593
y = .798839238
x_rounded = round(x)
# x_rounded will be rounded down to 0
y_rounded = round(y)
# y_rounded will be rounded up to 1
#expected example output: 
Attempt #1: Throwing a coin... 
It's a head! ... 
Got 1 head(s) so far and 0 tail(s) so far
'''
def toss(num):
    print 'Starting the program...'
    import random
    counter = 1
    headcount = 0
    tailcount = 0
    while num >= counter:
        random_int = random.random()
        coin_side = round(random_int)
        if coin_side == 1:
            side = 'heads'
            headcount += 1
        else:  
            side = 'tails'
            tailcount += 1 
        print 'Attempt #{}: Throwing a coin... It\'s {}! ...Got {} head(s) so far and {} tail(s) so far'.format(counter, side, headcount, tailcount)
        counter += 1 
    print 'End of program. Bye!'        
toss(5000)    