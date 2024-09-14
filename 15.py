def adad(n):
    """برعکس کردن عدد دریافتی """
    n = str(n)
    return n == n[::-1]
# گرفتن عدد از کابر
num = int(input())
# اعلام نتیجه
if adad(num):
    print("Yes")
else:
    print("NO") 
