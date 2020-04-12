print("------ Hello --------")

count = int(input("how many numbers would like to sum: "));

current_count = 0;

sum = 0;

while current_count < count:
    number = float(input("Enter the number: "))
    sum += number
    current_count += 1


print("sum of all numbers:",sum)
print("the avg:" , sum/count)    

for x in range(1,5):
    print x