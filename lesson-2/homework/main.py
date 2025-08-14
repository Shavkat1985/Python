# 1. Mashina nomlarini ajratib olish
txt = 'MsaatmiazD'
# Faraz qilamiz, bu satr ichida "Matiz" va "Damas" so‘zlari bor
car1 = txt[1:6]   # "Matiz"
car2 = txt[0] + txt[6:]  # "Damas"
print("Mashinalar:", car1, "va", car2)

# 2. Yashash joyini ajratish
txt2 = "I'am John. I am from London"
joy = txt2.split("from ")[1]
print("Yashash joyi:", joy)

# 3. Matnni teskari chiqarish
matn = input("\nMatn kiriting: ")
teskari = matn[::-1]
print("Teskari ko‘rinishi:", teskari)

# 4. Palindrom so‘zni tekshirish
soz = input("\nSo‘z kiriting (palindrom tekshirish uchun): ")
if soz.lower() == soz[::-1].lower():
    print("Bu so‘z palindrom!")
else:
    print("Bu so‘z palindrom emas.")

# 5. Mevalar ro‘yxati va uchinchi mevani chiqarish
mevalar = ["olma", "banan", "gilos", "shaftoli", "anjir"]
print("Uchinchi meva:", mevalar[2])

# 6. Ikki ro‘yxatni birlashtirish
sonlar1 = [1, 2, 3]
sonlar2 = [4, 5, 6]
yangi_royxat = sonlar1 + sonlar2
print("Birlashtirilgan ro‘yxat:", yangi_royxat)

# 7. Ro‘yxatdan birinchi, o‘rta va oxirgi elementlarni olish
raqamlar = [10, 20, 30, 40, 50]
yangi = [raqamlar[0], raqamlar[len(raqamlar)//2], raqamlar[-1]]
print("Birinchi, o‘rta va oxirgi elementlar:", yangi)

# 8. Shaharlar ro‘yxatida "Paris" borligini tekshirish
shaharlar = ["Toshkent", "Paris", "London", "New York"]
if "Paris" in shaharlar:
    print("Paris ro‘yxatda mavjud!")
else:
    print("Paris ro‘yxatda yo‘q.")

# 9. Ro‘yxatni takrorlash (loop ishlatmasdan)
sonlar = [1, 2, 3]
takrorlangan = sonlar * 2
print("Takrorlangan ro‘yxat:", takrorlangan)

# 10. Birinchi va oxirgi elementni almashtirish
nums = [5, 10, 15, 20, 25]
nums[0], nums[-1] = nums[-1], nums[0]
print("Birinchi va oxirgi element almashtirilgan:", nums)
