class Calculator:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def add(self):
        return self.a + self.b 

# create object 
s1 = Calculator(10,10)
print (s1.add())        

#inhertance 
class mul(Calculator):
    pass
# 
i1 = mul(10,10)
print("From sub-class:", i1.add())