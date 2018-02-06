'''
NOTES:
determine element data types
if string- concantenate in new string
if number - add to running sum
At end: print the string, the number and an analysis of what the list contains. 
If it contains only one type, print that type, otherwise, print 'mixed       
'''
'''
TEST CASE:
#input
l = ['magical unicorns',19,'hello',98.98,'world']
#output
"The list you entered is of mixed type"
"String: magical unicorns hello world"
"Sum: 117.98"
'''
my_list = ['magical unicorns',19,'hello',98.98,'world']
new_list = []
sum = 0
strcounter = 0
floatcounter = 0
intcounter = 0
for element in my_list:
    if isinstance(element, str):
        strcounter += 1
        new_list.append(element)
        #print strcounter, "is # of strings"
    elif isinstance(element, float):   
        floatcounter += 1
        sum += element
        #print element, "is a number"
    elif isinstance(element, int):   
        intcounter += 1
        sum += element
        #print element, "is a number"   
if strcounter > 0 and floatcounter + intcounter > 0:
    print "The list you entered is of mixed type"    
print "String is:", new_list, "Sum is:", sum
