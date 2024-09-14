def kamel(num):
    if num <= 0 :
        return "No"
    
    sums = 0 
    # محاسبه مقسوم علیه ها 
    for i in range(1, num):
        if num % i == 0 :
            sums += i 

    return sums == num 
# دریافت عدد
n = int(input())
# نتیجه 
if kamel(n):
    print("Yes")

else:
    print("No")