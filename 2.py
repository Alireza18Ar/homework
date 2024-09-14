def safar(sf):
    """مسافرمون مشتیه؟ یا کربلایی ؟ شایدم حاجی باشه!"""
    # وضعیتشو بررسی میکنیم
    Haji = sf[0]
    Karbalaee = sf[1]
    Mashti = sf[2]
    
    # باید بهش چی بگیم
    if Haji:
        return "Haji"
    elif Karbalaee:
        return "Karbalaee"
    elif Mashti:
        return "Mashti"
    
# ورودی میگیریم
koja = input().strip()
if koja == "NNN":
    print("Agha")

print(safar(koja))
