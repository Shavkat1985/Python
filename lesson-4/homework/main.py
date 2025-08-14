# ======== Dictionary mashqlari ========

# 1. Lug‘atni qiymatlari bo‘yicha saralash (o‘sish va kamayish tartibida)
dict1 = {1: 40, 2: 10, 3: 30}
print("O‘sish tartibida:", dict(sorted(dict1.items(), key=lambda x: x[1])))
print("Kamayish tartibida:", dict(sorted(dict1.items(), key=lambda x: x[1], reverse=True)))

# 2. Lug‘atga yangi kalit qo‘shish
sample_dict = {0: 10, 1: 20}
sample_dict[2] = 30
print("Yangi lug‘at:", sample_dict)

# 3. Bir nechta lug‘atlarni birlashtirish
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
yangi_lugat = {}
for d in (dic1, dic2, dic3):
    yangi_lugat.update(d)
print("Birlashtirilgan lug‘at:", yangi_lugat)

# 4. Kvadrat qiymatlar bilan lug‘at yaratish (1 dan n gacha)
n = 5
kvadratlar = {x: x**2 for x in range(1, n+1)}
print("1 dan", n, "gacha kvadratlar lug‘ati:", kvadratlar)

# 5. 1 dan 15 gacha kvadratlar lug‘ati
kvadratlar_15 = {x: x**2 for x in range(1, 16)}
print("1 dan 15 gacha kvadratlar:", kvadratlar_15)


# ======== Set mashqlari ========

# 1. Set yaratish
mevalar = {"olma", "banan", "gilos"}
print("Set:", mevalar)

# 2. Set ichida aylanib chiqish
print("Set elementlari:")
for meva in mevalar:
    print(meva)

# 3. Setga element qo‘shish
mevalar.add("shaftoli")
print("Yangi element qo‘shildi:", mevalar)

# Bir nechta element qo‘shish
mevalar.update(["anor", "anjir"])
print("Bir nechta element qo‘shildi:", mevalar)

# 4. Setdan element o‘chirish
mevalar.remove("banan")  # Agar element bo‘lmasa, xato beradi
print("'banan' o‘chirildi:", mevalar)

# 5. Agar mavjud bo‘lsa elementni o‘chirish
mevalar.discard("uzum")  # Agar element bo‘lmasa, xato bermaydi
print("Agar bo‘lsa o‘chirildi:", mevalar)
