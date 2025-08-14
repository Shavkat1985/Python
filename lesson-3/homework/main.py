# 1. Mevalar ro‘yxati va uchinchi mevani chiqarish
mevalar = ["olma", "banan", "gilos", "shaftoli", "anjir"]
print("Uchinchi meva:", mevalar[2])

# 2. Ikki ro‘yxatni birlashtirish
sonlar1 = [1, 2, 3]
sonlar2 = [4, 5, 6]
yangi_royxat = sonlar1 + sonlar2
print("Birlashtirilgan ro‘yxat:", yangi_royxat)

# 3. Birinchi, o‘rta va oxirgi elementlarni olish
raqamlar = [10, 20, 30, 40, 50]
yangi = [raqamlar[0], raqamlar[len(raqamlar)//2], raqamlar[-1]]
print("Birinchi, o‘rta va oxirgi elementlar:", yangi)

# 4. Ro‘yxatdan tuplega o‘tkazish
filmlar = ["Inception", "Avatar", "Titanic", "Gladiator", "Matrix"]
filmlar_tuple = tuple(filmlar)
print("Filmlar tuple ko‘rinishida:", filmlar_tuple)

# 5. "Paris" ro‘yxatda bormi?
shaharlar = ["Toshkent", "Paris", "London", "New York"]
if "Paris" in shaharlar:
    print("Paris ro‘yxatda bor!")
else:
    print("Paris ro‘yxatda yo‘q.")

# 6. Ro‘yxatni takrorlash (loop ishlatmasdan)
sonlar = [1, 2, 3]
takrorlangan = sonlar * 2
print("Takrorlangan ro‘yxat:", takrorlangan)

# 7. Birinchi va oxirgi elementni almashtirish
nums = [5, 10, 15, 20, 25]
nums[0], nums[-1] = nums[-1], nums[0]
print("Birinchi va oxirgi almashtirilgan:", nums)

# 8. Tuple ichidan slice olish
sonlar_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print("Index 3 dan 7 gacha bo‘lgan qism:", sonlar_tuple[3:8])

# 9. Ro‘yxatda nechta 'blue' borligini sanash
ranglar = ["blue", "red", "blue", "green", "blue", "yellow"]
print("'blue' rangi soni:", ranglar.count("blue"))

# 10. Tuple ichida "lion" indexini topish
hayvonlar = ("tiger", "lion", "elephant", "lion")
print("'lion' indexi:", hayvonlar.index("lion"))

# 11. Ikki tuple ni birlashtirish
t1 = (1, 2, 3)
t2 = (4, 5, 6)
yangi_tuple = t1 + t2
print("Birlashtirilgan tuple:", yangi_tuple)

# 12. Ro‘yxat va tuple uzunligini topish
royxat = [1, 2, 3, 4, 5]
tup = (10, 20, 30)
print("Ro‘yxat uzunligi:", len(royxat))
print("Tuple uzunligi:", len(tup))

# 13. Tuple dan ro‘yxatga o‘tkazish
tup_sonlar = (100, 200, 300, 400, 500)
royxat_sonlar = list(tup_sonlar)
print("Tuple ro‘yxatga o‘tkazildi:", royxat_sonlar)

# 14. Tuple ichidagi eng katta va eng kichik son
sonlar_t = (15, 2, 99, 45, 7)
print("Eng katta son:", max(sonlar_t))
print("Eng kichik son:", min(sonlar_t))

# 15. Tuple ni teskari chiqarish
sozlar = ("salom", "dunyo", "python", "kod")
print("Teskari tuple:", sozlar[::-1])
