# دریافت اعدادبه صورت لیست 
numbers = []
for i in range(5): 
    num = int(input("enter your number: "))
    numbers.append(num)
# مرتب کردن به صورت نزولی
sort_descending = sorted(numbers, reverse=True)
print(sort_descending)
# مرتب کردن به صورت صعودی 
sort_ascending = sorted(numbers)
print(sort_ascending)