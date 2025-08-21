# Stringlar

txt = input("Matn kiriting: ")

natija = ""
i = 0
while i < len(txt):
    natija += txt[i:i+3]
    if i+3 < len(txt):
        natija += "_"
    i += 3

print(natija)



# Kvadrat chiqarish

n = int(input("Son kiriting: "))

for i in range(n):
    print(i**2)



# Loop lar

# 1

i = 1
while i <= 10:
    print(i)
    i += 1


# 2

for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end=" ")
    print()


# 3

n = int(input("Son kiriting: "))
print("Yig'indi:", sum(range(1, n+1)))


# 4

n = int(input("Son kiriting: "))

for i in range(1, 11):
    print(n * i)


# 5 

numbers = [12, 75, 150, 180, 145, 525, 50]

for num in numbers:
    if num > 500:
        break
    if num % 5 == 0 and num <= 150:
        print(num)


# 6 

n = int(input("Son kiriting: "))
print("Raqamlar soni:", len(str(n)))


# 7 

for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()


# 8

list1 = [10, 20, 30, 40, 50]

for x in reversed(list1):
    print(x)


# 9

for i in range(-10, 0):
    print(i)


# 10

for i in range(5):
    print(i)
print("Tugadi!")


# 11

a = 25
b = 50
print(f"{a} dan {b} gacha tub sonlar:")

for num in range(a, b+1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)


# 12

a, b = 0, 1
for _ in range(10):
    print(a, end=" ")
    a, b = b, a+b


# 13

n = int(input("Son kiriting: "))
fact = 1
for i in range(1, n+1):
    fact *= i
print(f"{n}! =", fact)


# Listlar

list1 = [1, 1, 2, 3, 4, 2]
list2 = [1, 3, 4, 5]

natija = []

for x in list1:
    if x not in list2:
        natija.append(x)

for y in list2:
    if y not in list1:
        natija.append(y)

print(natija)
