def sin(m):
    items = ["sabze", "samano", "senjed", "sir", "sib", "serke", "somagh"]

    item = []
    count = 0 

    for i in items:
        if count < m:
            item.append(i)
            count += 1 
        else:
            break
    return item 

m = int(input())
item = sin (m)
for i in item :
    print(i)