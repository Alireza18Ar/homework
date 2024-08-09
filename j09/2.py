def fibonacci(x):
    fib1 = 1
    fib2 = 1 
    if number == 1 :
        print(fib1)
    elif number == 2 :
        print(fib1, fib2)
    else:
        print(fib1 , fib2, end="\t")
    i = 1 
    while i < number : 
        fib3 = fib1 + fib2 
        print(fib3, end = "\t")
        fib1 = fib2 
        fib2 = fib3 
        i += 1


number = int(input("Enter a number: "))
fibonacci(number)