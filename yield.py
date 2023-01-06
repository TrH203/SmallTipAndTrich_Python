# Diff between return and yield

# Return in def
def ReturnDef(n: int) -> int:
  for i in range(n):
    return i 
  
# input n=5
# output => 0, because when def return, it break!!!!

# Yield in def
def YieldDef(n: int) -> int:
  for i in range(n):
    yield i
    
# input n=5
# Return object, When you parse YieldDef(n) -> list(YieldDef(n)), you got [0,1,2,3,4]

# More about yield
def simpleGeneratorFun():
    yield 1
    yield 2
    yield 3
 
 
for value in simpleGeneratorFun():
    print(value)
# output
#1
#2
#3


# Finally return will break and return the value whenever it active, but yield NOT break, it'll return all.
