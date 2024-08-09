def show_a_name(name):
    return len(name)

number = int(input())

names = []

for i in range(number):
    name = input()
    names.append(name)

max = 0

for name in names:
    count = show_a_name(name)
    if count > max:
        max = count

print(max)