def alone_number(n):
    while n >= 10:
        n = sum(int(num)for num in str(n))
        return n 



number = int(input())

if number < 0:
    print("enter another number")
else:
    result = alone_number(number)
    print(result)
