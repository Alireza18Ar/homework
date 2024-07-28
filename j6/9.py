start = int(input("enter first number: "))
end = int(input("enter first number: "))
# درست کردن لیست برای اعدادی که به پانزده بخش پذیر هستند
D = []
for i in range(start, end + 1):
    if i % 15 == 0 :
        D.append(i)

# نمایش نتیجه ها 
print(D)
print(len(D))