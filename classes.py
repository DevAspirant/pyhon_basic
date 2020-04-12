class student:
    def __init__(self,name):
        self.name = name
        self.marks = []
        print("welcome {} to the school".format(name))
    def add_mark(self,mark):
        self.marks.append(mark)
    def avg(self):
        return sum(self.marks) / len(self.marks),"%"
        

s1 = student("ammar")
s1.add_mark(100)
s1.add_mark(90)
print ("the average is:", s1.avg())
#print(s1.show())        