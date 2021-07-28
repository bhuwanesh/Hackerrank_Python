class A:
    #Magic methods
    def __init__(self, string = "Hello"):
        self.string = string
        
    def __str__(self):
        return "Hello" if self.string else "I am str"
        
    def __add__(self, other):
        return (self.string + other)
    
    def __repr__(self):
        return "I am repr"
    
a = A()
print(a)   #Hello
print(a + " World")  #Hello World
print(repr(a))    # I am repr
print(str(a))   # I am str


#############################
class A():
    def __init__(self):
        self.values = [1, 4, 8, 12]
    
a = A().values
for i in a:
    print(i, end = ' ')
# 1, 4, 8, 12

#############################
class A():
    def __init__(self):
        self.values = dict()

a = A().values
a[10] = "test"
print(a[10])        #test

#############################
class A():
    def __init__(self, value):
        self.value = value
    
    def __int__(self):
        return (int(self.value)*2)
        

class B():
    def __init__(self, value):
        self.value = value
    
    def __int__(self):
        return int(self.value)

a=int(A(1))
b=int(B(2))
print(a==b)  #True


