def factorial(number):
    """عدد هارو میگیریم فاکتوریلشو میدیم"""
    # مراحل حساب کتاب فاکتوریل
    if number < 0 :
       return 'it is not correct'
    
    result = 1
    for i in range (1, number + 1):
        result *= i 
    return result
# گرفتن ورودی
num = int(input())
# خروجی
print(factorial(num))
