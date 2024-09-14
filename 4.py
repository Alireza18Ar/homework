def salib():
    # گرفتن ورودی 
    number = input()
    # بررسی عدد
    if len(number) != 2 :
        print(" ")
        return
    

    if not (number[0] >= "0" and number[0] <= "9") or not (number[1]>= "0" and number[1]<= "9"):
        print(" ")
        return
    
    # جدا سازی ارقام عدد 
    num1 = int(number[0])
    num2 = int(number[1])

    # محاسبه و اجرای برنامه
    if num1 > num2:
        result = num1 - num2 
    else:
        result = num2 - num1

    print(result)

salib()    