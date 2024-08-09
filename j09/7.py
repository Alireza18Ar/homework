def prime_numbers(num):
    if num <= 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
        return True
    
num1 = int(input())
num2 = int(input())

if num1 > num2 : 
    num1, num2 = num2, num1

for num in range(num1, num2 + 1):
    if prime_numbers(num):
        print(num)


