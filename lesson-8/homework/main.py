# 1. Nolga bo‘lish
try:
    son = 10 / 0
except ZeroDivisionError:
    print("Xato: Nolga bo‘lish mumkin emas!")

# 2. ValueError
try:
    son = int(input("Butun son kiriting: "))
    print("Siz kiritgan son:", son)
except ValueError:
    print("Xato: Faqat butun son kiritish mumkin!")

# 3. Fayl topilmasa
try:
    with open("malumot.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("Xato: Fayl topilmadi!")

# 4. TypeError
try:
    a = float(input("Birinchi sonni kiriting: "))
    b = float(input("Ikkinchi sonni kiriting: "))
    print("Yig‘indi:", a + b)
except ValueError:
    print("Xato: Faqat raqam kiriting!")

# 5. PermissionError
try:
    with open("/etc/shadow", "r") as f:  # Linux fayli
        print(f.read())
except PermissionError:
    print("Xato: Faylni o‘qishga ruxsat yo‘q!")

# 6. IndexError
try:
    mevalar = ["olma", "banan", "uzum"]
    print(mevalar[5])
except IndexError:
    print("Xato: Bunday indeks yo‘q!")

# 7. KeyboardInterrupt
try:
    son = int(input("Son kiriting: "))
    print("Siz kiritgan son:", son)
except KeyboardInterrupt:
    print("\nXato: Foydalanuvchi kiritishni bekor qildi!")

# 8. ArithmeticError
try:
    natija = 10 / 0
except ArithmeticError:
    print("Xato: Arifmetik xato yuz berdi!")

# 9. UnicodeDecodeError
try:
    with open("test.txt", "r", encoding="ascii") as f:
        print(f.read())
except UnicodeDecodeError:
    print("Xato: Kodlash muammosi!")

# 10. AttributeError
try:
    raqamlar = [1, 2, 3]
    raqamlar.upper()  # listda upper() yo‘q
except AttributeError:
    print("Xato: Bu atribut mavjud emas!")




# 1. Faylni o‘qish
with open("test.txt", "r") as f:
    print(f.read())

# 2. Birinchi n qatorni o‘qish
n = 3
with open("test.txt", "r") as f:
    for i in range(n):
        print(f.readline(), end="")

# 3. Matn qo‘shib yozish
with open("test.txt", "a") as f:
    f.write("\nYangi qator qo‘shildi")
with open("test.txt", "r") as f:
    print(f.read())

# 4. Oxirgi n qatorni o‘qish
n = 2
with open("test.txt", "r") as f:
    qatorlar = f.readlines()
    print("".join(qatorlar[-n:]))

# 5. Faylni listga saqlash
with open("test.txt", "r") as f:
    qatorlar = f.readlines()
print(qatorlar)

# 6. Faylni o‘zgaruvchiga saqlash
with open("test.txt", "r") as f:
    matn = f.read()
print(matn)

# 7. Faylni massivga saqlash
with open("test.txt", "r") as f:
    massiv = [qator.strip() for qator in f]
print(massiv)

# 8. Eng uzun so‘z(lar)ni topish
with open("test.txt", "r") as f:
    sozlar = f.read().split()
    uzun = max(sozlar, key=len)
print("Eng uzun so‘z:", uzun)

# 9. Fayldagi qatorlar soni
with open("test.txt", "r") as f:
    qator_soni = len(f.readlines())
print("Qatorlar soni:", qator_soni)

# 10. So‘zlar chastotasi
from collections import Counter
with open("test.txt", "r") as f:
    sozlar = f.read().split()
    hisob = Counter(sozlar)
print(hisob)

# 11. Fayl hajmini olish
import os
print("Fayl hajmi:", os.path.getsize("test.txt"), "bayt")

# 12. Listni faylga yozish
mevalar = ["olma", "banan", "uzum"]
with open("mevalar.txt", "w") as f:
    for m in mevalar:
        f.write(m + "\n")

# 13. Faylni nusxalash
with open("test.txt", "r") as f1, open("nusxa.txt", "w") as f2:
    f2.write(f1.read())

# 14. Ikki fayldagi qatorlarni qo‘shish
with open("test.txt", "r") as f1, open("nusxa.txt", "r") as f2:
    for q1, q2 in zip(f1, f2):
        print(q1.strip() + " " + q2.strip())

# 15. Tasodifiy qator o‘qish
import random
with open("test.txt", "r") as f:
    qatorlar = f.readlines()
    print("Random qator:", random.choice(qatorlar))

# 16. Fayl yopilganmi yoki yo‘q
f = open("test.txt", "r")
print("Fayl yopilganmi?", f.closed)
f.close()
print("Fayl yopilganmi?", f.closed)

# 17. Newline belgilarini olib tashlash
with open("test.txt", "r") as f:
    toza = [q.strip() for q in f]
print(toza)

# 18. Fayldagi so‘zlar soni
with open("test.txt", "r") as f:
    matn = f.read().replace(",", " ")
    sozlar = matn.split()
print("So‘zlar soni:", len(sozlar))

# 19. Bir nechta fayldan belgilarni olish
fayllar = ["test.txt", "mevalar.txt"]
belgilar = []
for fayl in fayllar:
    with open(fayl, "r") as f:
        belgilar.extend(list(f.read()))
print(belgilar)

# 20. A.txt dan Z.txt gacha fayllar yaratish
import string
for harf in string.ascii_uppercase:
    with open(f"{harf}.txt", "w") as f:
        f.write(f"{harf} harfi fayli")

# 21. Faylga alifboni yozish (har qatorga 5 ta harf)
import string
harflar = string.ascii_uppercase
with open("alifbo.txt", "w") as f:
    for i in range(0, len(harflar), 5):
        f.write(" ".join(harflar[i:i+5]) + "\n")
