#For in python to add to arr
#Way1
arr = []
for i in range(10):
  arr.append(i)
  
#Way2
arr = [i for i in range(10)]

#You can use if in for way2

arr = [i for i in range(10) if i%2 ==0]
# output [0,2,4,6,8]
