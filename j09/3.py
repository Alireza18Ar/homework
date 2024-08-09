def number(x):
    if x <= 1:
        return False
    for i in range(2, int(x ** 0.5) + 1):
         if x % i == 0 :
             return False
    return True          
# receive a number from user 
x = float(input("enter a number: "))

if number(x):
    print("yes it is")
else:
    print("no it is not")