#Stars Part 1
#Create a function called draw_stars() that takes a list of numbers and prints out *.
'''
def draw_stars():
    star_array = [4, 6, 1, 3, 5, 7, 25]
    for index in star_array:
        print index * '*'

draw_stars()    
'''
#Stars Part 2
def draw_stars():
    x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
    i = 0
    #print len(x)
    
    while i < len(x):
        if type(x[i]) is int:
            #print 'i work'
            print x[i] * '*'
            i += 1    
        if type(x[i]) is str:
            #print 'me too'
            x[i] = len(x[i]) * x[i][0]
            print (x[i].lower())
            i += 1     
            
draw_stars() 

