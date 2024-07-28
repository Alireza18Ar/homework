L1 = []  # لیست زوج ها 
L2 = []  # لیست فرد ها


for i in range(1, 101):
    if i % 2 == 0 :
        L1.append(i) #اگر عدد زوج بود به لیست L1 اضافه کن

for i in range(1, 101):
   if i % 2  != 0 :
    L2.append(i) # اگر اعدد فرد بود به لیست L2 اضافه کن

print(L1)
print(L2)