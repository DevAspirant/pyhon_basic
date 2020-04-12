import os,time,calendar

file = open('test.txt','r')
print("Name of File: ", file.name);
print("close of not: ", file.close);
print("opening mode: ",file.mode);


localeTime = time.localtime(time.time())
print("local time: ",localeTime)


cal = calendar.month(2020,4)
print(cal)

