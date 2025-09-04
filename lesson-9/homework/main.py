# 1. Aylana klassi

import math

class Aylana:
    def __init__(self, radius):
        self.radius = radius

    def yuza(self):
        return math.pi * (self.radius ** 2)

    def perimetr(self):
        return 2 * math.pi * self.radius

aylana = Aylana(5)
print("Aylana yuzi:", aylana.yuza())
print("Aylana perimetri:", aylana.perimetr())


# 2. Inson klassi

from datetime import date

class Inson:
    def __init__(self, ism, davlat, tugilgan_yil):
        self.ism = ism
        self.davlat = davlat
        self.tugilgan_yil = tugilgan_yil

    def yosh(self):
        bugun = date.today().year
        return bugun - self.tugilgan_yil

inson = Inson("Ali", "O‘zbekiston", 2000)
print(f"{inson.ism}ning yoshi:", inson.yosh())



# 3. Kalkulyator klassi

class Kalkulyator:
    def qoshish(self, a, b):
        return a + b

    def ayirish(self, a, b):
        return a - b

    def kopaytirish(self, a, b):
        return a * b

    def bolish(self, a, b):
        if b == 0:
            return "Xato: nolga bo‘lish mumkin emas!"
        return a / b

calc = Kalkulyator()
print("3 + 5 =", calc.qoshish(3, 5))
print("10 / 0 =", calc.bolish(10, 0))


# 4. Shakl va undan vorislar

class Shakl:
    def yuza(self):
        pass

    def perimetr(self):
        pass

class AylanaShakl(Shakl):
    def __init__(self, r):
        self.r = r

    def yuza(self):
        return math.pi * self.r**2

    def perimetr(self):
        return 2 * math.pi * self.r

class Kvadrat(Shakl):
    def __init__(self, a):
        self.a = a

    def yuza(self):
        return self.a**2

    def perimetr(self):
        return 4 * self.a

class Uchburchak(Shakl):
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c

    def perimetr(self):
        return self.a + self.b + self.c

    def yuza(self):
        p = self.perimetr() / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

kv = Kvadrat(4)
print("Kvadrat yuzi:", kv.yuza())



# 5. Ikkilik daraxt (BST)

class Tugun:
    def __init__(self, qiymat):
        self.qiymat = qiymat
        self.chap = None
        self.ong = None

class BST:
    def __init__(self):
        self.kok = None

    def joylashtir(self, qiymat):
        if self.kok is None:
            self.kok = Tugun(qiymat)
        else:
            self._joylashtir(self.kok, qiymat)

    def _joylashtir(self, tugun, qiymat):
        if qiymat < tugun.qiymat:
            if tugun.chap is None:
                tugun.chap = Tugun(qiymat)
            else:
                self._joylashtir(tugun.chap, qiymat)
        else:
            if tugun.ong is None:
                tugun.ong = Tugun(qiymat)
            else:
                self._joylashtir(tugun.ong, qiymat)

    def qidir(self, qiymat):
        return self._qidir(self.kok, qiymat)

    def _qidir(self, tugun, qiymat):
        if tugun is None:
            return False
        if tugun.qiymat == qiymat:
            return True
        elif qiymat < tugun.qiymat:
            return self._qidir(tugun.chap, qiymat)
        else:
            return self._qidir(tugun.ong, qiymat)

daraxt = BST()
daraxt.joylashtir(10)
daraxt.joylashtir(5)
daraxt.joylashtir(15)
print("15 daraxtda bormi?", daraxt.qidir(15))



# 6. Stek (Stack)

class Stek:
    def __init__(self):
        self.stek = []

    def push(self, element):
        self.stek.append(element)

    def pop(self):
        if not self.stek:
            return "Stek bo‘sh!"
        return self.stek.pop()

stek = Stek()
stek.push(1)
stek.push(2)
print("Stekdan olingan:", stek.pop())


# 7. Bog‘langan ro‘yxat (Linked List)

class Node:
    def __init__(self, data):
        self.data = data
        self.keyingi = None

class LinkedList:
    def __init__(self):
        self.bosh = None

    def qo‘shish(self, data):
        yangi = Node(data)
        yangi.keyingi = self.bosh
        self.bosh = yangi

    def chiqarish(self):
        temp = self.bosh
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.keyingi
        print("None")

    def o‘chirish(self, key):
        temp = self.bosh
        if temp and temp.data == key:
            self.bosh = temp.keyingi
            return
        oldingi = None
        while temp and temp.data != key:
            oldingi = temp
            temp = temp.keyingi
        if temp is None:
            return
        oldingi.keyingi = temp.keyingi

ll = LinkedList()
ll.qo‘shish(10)
ll.qo‘shish(20)
ll.qo‘shish(30)
ll.chiqarish()
ll.o‘chirish(20)
ll.chiqarish()



# 8. Savat (Shopping Cart)

class Savat:
    def __init__(self):
        self.tovarlar = {}

    def qo‘shish(self, nom, narx):
        self.tovarlar[nom] = narx

    def o‘chirish(self, nom):
        if nom in self.tovarlar:
            del self.tovarlar[nom]

    def jami(self):
        return sum(self.tovarlar.values())

savat = Savat()
savat.qo‘shish("Olma", 10000)
savat.qo‘shish("Banan", 15000)
print("Jami:", savat.jami())



# 9. Stek + chiqarish

class Stek2:
    def __init__(self):
        self.stek = []

    def push(self, x):
        self.stek.append(x)

    def pop(self):
        if not self.stek:
            return "Bo‘sh stek!"
        return self.stek.pop()

    def chiqarish(self):
        print("Stek:", self.stek)

s2 = Stek2()
s2.push(5)
s2.push(7)
s2.chiqarish()
print("Olingan:", s2.pop())



# 10. Navbat (Queue)

class Navbat:
    def __init__(self):
        self.navbat = []

    def enqueue(self, x):
        self.navbat.append(x)

    def dequeue(self):
        if not self.navbat:
            return "Bo‘sh navbat!"
        return self.navbat.pop(0)

q = Navbat()
q.enqueue("Ali")
q.enqueue("Vali")
print("Navbatdan chiqdi:", q.dequeue())


# 11. Bank klassi

class Bank:
    def __init__(self):
        self.hisoblar = {}

    def ochish(self, ism, balans=0):
        self.hisoblar[ism] = balans

    def hisob(self, ism):
        return self.hisoblar.get(ism, "Hisob topilmadi")

    def pul_qo‘shish(self, ism, miqdor):
        if ism in self.hisoblar:
            self.hisoblar[ism] += miqdor

    def pul_olish(self, ism, miqdor):
        if ism in self.hisoblar and self.hisoblar[ism] >= miqdor:
            self.hisoblar[ism] -= miqdor

bank = Bank()
bank.ochish("Ali", 50000)
bank.pul_qo‘shish("Ali", 20000)
bank.pul_olish("Ali", 10000)
print("Ali hisobida:", bank.hisob("Ali"))
