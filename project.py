num = input("enter your number: ");
print num;
if num == 'x':
    print("closing game");
try:
    num = int(num)
    if num % 2 == 0:
        print("even")
    else:
        print("odd") 
except ValueError:
    print("please enter a valied number")               