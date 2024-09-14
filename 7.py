def mahdi(H, K):
    """بررسی زوج یا فرد بودن اعداد"""

    # بررسی اعداد
    if (H - K)% 2 == 0:
        print("YES")
    else:
        print("NO")

# گرفتن اعداد
H = int(input())
K = int(input())

mahdi(H, K)
