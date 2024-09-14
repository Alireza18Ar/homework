def sin(m):
    """انتخاب سین های سفره هفت سین"""
    items = ["sabze", "samano", "senjed", "sir", "sib", "serke", "somagh"]
    # محاسبات لازمه
    item = []
    count = 0 

    for i in items:
        if count < m:
            item.append(i)
            count += 1 
        else:
            break
    return item 
# دریافت ورودی
m = int(input())
item = sin (m)
for i in item :
    print(i) 
