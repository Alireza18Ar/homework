def calculate_floor(string):
    """یک بازی جالب با آسانسور"""

    floor = 0 

    # بالا و پایین رفتن آسانسور
    for i in string:
        # آسانسور برود بالا
        if i == "U":
            floor += 1
        # آسانسور برود پایین
        elif i == "D":
            floor -= 1 

    return floor

tabaghe =input().strip()
result = calculate_floor(tabaghe)
print(f">>> calculate_floor('{tabaghe}')")
print(result)
