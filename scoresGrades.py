'''
Score: 60 - 69; Grade - D
Score: 70 - 79; Grade - C
Score: 80 - 89; Grade - B
Score: 90 - 100; Grade - A
    expected output example: 
    Score: 87; Your grade is B
'''
def scores(num):
    print 'Scores and Grades'
    import random
    while num > 0:
        random_num = random.randint(60, 100)
        if random_num < 70:
            grade = 'D'
        elif random_num < 80:
            grade = 'C'  
        elif random_num < 90:
            grade = 'B'   
        elif random_num <= 100:
            grade = 'A'              
        print 'Score: {}; Your grade is {}'.format(random_num, grade)
        num -= 1
    print 'End of program. Bye!' 
scores(10)   