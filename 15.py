def adad(n):
    n = str(n)
    return n == n[::-1]

num = int(input())

if adad(num):
    print("Yes")
else:
    print("NO")