def separator(ls):
    even_numbers = [num for num in numbers if num % 2 == 0]
    odd_numbers = [num for num in numbers if num % 2 != 0]
    result_touple = (even_numbers, odd_numbers)
    print((numbers, even_numbers, odd_numbers) )


numbers = [-3, -2, -1, 0, 1, 2, 3]
separator(numbers)