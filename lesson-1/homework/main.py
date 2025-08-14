# 1. Kvadratning tomoni berilgan. Perimetri va yuzasini topish.
tomon = float(input("Kvadratning tomon uzunligini kiriting: "))
perimetr = 4 * tomon
yuza = tomon ** 2
print("Kvadratning perimetri:", perimetr)
print("Kvadratning yuzasi:", yuza)

# 2. Doiraning diametri berilgan. Uning uzunligini topish.
diametr = float(input("\nDoiraning diametrini kiriting: "))
pi = 3.14159
uzunlik = pi * diametr
print("Doira uzunligi (aylana uzunligi):", uzunlik)

# 3. Ikki a va b son berilgan. O‘rtacha qiymatini topish.
a = float(input("\nBirinchi sonni kiriting (a): "))
b = float(input("Ikkinchi sonni kiriting (b): "))
ortacha = (a + b) / 2
print("O‘rtacha qiymat:", ortacha)

# 4. Ikki a va b son berilgan. Ularning yig‘indisi, ko‘paytmasi va har birining kvadratini topish.
a = float(input("\nBirinchi sonni kiriting (a): "))
b = float(input("Ikkinchi sonni kiriting (b): "))
yigindi = a + b
kopaytma = a * b
a_kvadrat = a ** 2
b_kvadrat = b ** 2

print("Yig‘indisi:", yigindi)
print("Ko‘paytmasi:", kopaytma)
print("a sonining kvadrati:", a_kvadrat)
print("b sonining kvadrati:", b_kvadrat)
