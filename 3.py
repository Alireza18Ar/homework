def factorial(number):
    if number < 0 :
       return 'it is not correct'
    
    result = 1
    for i in range (1, number + 1):
        result *= i 
    return result

num = int(input())
print(factorial(num))