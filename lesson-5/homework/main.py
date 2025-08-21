# Ex 1


year = int(input("Yilni kiriting: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Kabisa yili")
else:
    print("Kabisa yili emas")



# Ex 2

n = int(input("Butun son kiriting: "))

if n % 2 == 1:
    print("Tub")
elif n % 2 == 0 and 2 <= n <= 5:
    print("Tub emas")
elif n % 2 == 0 and 6 <= n <= 20:
    print("Tub")
elif n % 2 == 0 and n > 20:
    print("Tub emas")


# Ex 3

a = int(input("a ni kiriting: "))
b = int(input("b ni kiriting: "))

if a % 2 != 0:  
    a += 1

if b % 2 != 0:  
    b -= 1

print(list(range(a, b+1, 2)))
