def add (x,y):
    return x+y
def sub (x,y):
    return x-y
def div(x,y):
    return x/y
def multi(x,y):
    return x*y
print("select any one")
print("1. addition")
print("2. subtraction")
print("3. division")
print("4. multiplecation")

choice = input("Enter any options(1/2/3/4):")

num1 = int(input("Enter your number1: "))
num2 = int(input("Enter your number2: "))

if choice == '1':
    print(num1,"+",num2,"=",add(num1,num2))
elif choice == '2':
    print(num1,"-",num2,"=",sub(num1,num2))
elif choice == '3':
    print(num1,"/",num2,"=",div(num1,num2))
elif choice == '4':
    print(num1,"*",num2,"=",mul(num1,num2))
else:
    print("this is not accept!")
    
