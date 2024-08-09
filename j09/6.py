numbers = {1: 6, 2: 5, 3: 4, 4: 3, 5: 2, 6: 1} # اعداد روی تاس و اعداد مقابلشان

# دریافت عدد ورودی از کاربر
number = int(input())

# نمایش عدد روبروی عدد انتخابی کاربر
if number == 1:
    print("6")
elif number == 2:
    print("5")
elif number == 3:
    print("4")
elif number == 4:
    print("3")
elif number == 5:
    print("2")
elif number == 6:
    print("1")
else:
    print("this number is not available")