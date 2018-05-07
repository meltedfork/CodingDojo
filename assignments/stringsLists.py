
words = "It's thanksgiving day. It's my birthday,too!"
words.find('day') # 18
words.replace("day", "month") # "It's thanksgiving month. It's my birthmonth,too!"
# print words

x = [2,54,-2,7,12,98]
print max(x) # 98
print min(x) # -2

my_list = ["hello",2,54,-2,7,12,98,"world"]
print [my_list[0], my_list[-1]] # ['hello', 'world']
len(my_list) # 8

x = [19,2,54,-2,7,12,98,32,10,-3,6]
list.sort(x) # [-3, -2, 2, 6, 7, 10, 12, 19, 32, 54, 98]
print len(x) # 11
print x[0:5] # [-3, -2, 2, 6, 7]
newx = []
newx.append(x[0:5])
print newx
# [[-3, -2, 2, 6, 7]]
print newx[0]
# [-3, -2, 2, 6, 7]

newx.append(x[5:])
print newx
# [[-3, -2, 2, 6, 7], [10, 12, 19, 32, 54, 98]]

x.insert(0, newx)

print x
# [[[-3, -2, 2, 6, 7], [10, 12, 19, 32, 54, 98]], -3, -2, 2, 6, 7, 10, 12, 19, 32, 54, 98]
newx = x[0:5]
# [[-3, -2, 2, 6, 7], [10, 12, 19, 32, 54, 98]], -3, -2, 2, 6]
x = x[5:12]
# [7, 10, 12, 19, 32, 54, 98]
x.insert(0, newx)
print x
# [[[[-3, -2, 2, 6, 7], [10, 12, 19, 32, 54, 98]], -3, -2, 2, 6], 7, 10, 12, 19, 32, 54, 98]
