# Create Multiplication Table
# following code creates a list of lists
multi = []
for numX in range(0,13):
    arr = [numX]
    if numX == 0:
        numX +=1
    for numY in range(1,13):
        # print(numX * numY)
        arr.append(numX * numY)
    multi.append(arr)    
# print multi

for arr in multi:
    # print arr
    print ' '.join(str(element) for element in arr)
