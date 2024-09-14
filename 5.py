def mahdi():

    number = input()

    if number == "":
        print(" ")
        return
    
    a = 0 
    for i in number:
        if i < '0' :
            print(" ")
            return
        
        a = a * 10 + (int(i) - int(0))   

        result = "w" + 'o' * a + "w"
        print(result)

mahdi()