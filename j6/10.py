l1 = [1, 2, 3, 4, 5, 2, 4, 5, 1]
l2 = []

#حذف اعضای تکراری 
for item in l1 : 
    if item not in l2:
        l2.append(item)

print(l2)