# ToDo List Dasturi

class Vazifa:
    def __init__(self, sarlavha, tavsif, muddat):
        self.sarlavha = sarlavha
        self.tavsif = tavsif
        self.muddat = muddat
        self.holat = "Bajarilmagan"

    def bajarildi(self):
        self.holat = "Bajarildi"

    def __str__(self):
        return f"{self.sarlavha} | {self.tavsif} | Muddat: {self.muddat} | Holat: {self.holat}"


class ToDoList:
    def __init__(self):
        self.vazifalar = []

    def vazifa_qo‘shish(self, vazifa):
        self.vazifalar.append(vazifa)

    def bajarilgan_deb_belgilash(self, index):
        if 0 <= index < len(self.vazifalar):
            self.vazifalar[index].bajarildi()

    def barcha_vazifalar(self):
        for v in self.vazifalar:
            print(v)

    def bajarilmaganlar(self):
        for v in self.vazifalar:
            if v.holat == "Bajarilmagan":
                print(v)


if __name__ == "__main__":
    todolist = ToDoList()

    while True:
        print("\n=== ToDo List Menyu ===")
        print("1. Vazifa qo‘shish")
        print("2. Vazifani bajarilgan deb belgilash")
        print("3. Barcha vazifalarni ko‘rish")
        print("4. Faqat bajarilmagan vazifalar")
        print("5. Chiqish")

        tanlov = input("Tanlang: ")

        if tanlov == "1":
            s = input("Sarlavha: ")
            t = input("Tavsif: ")
            m = input("Muddat: ")
            v = Vazifa(s, t, m)
            todolist.vazifa_qo‘shish(v)
        elif tanlov == "2":
            idx = int(input("Qaysi vazifa raqami bajarildi? (0,1,2...): "))
            todolist.bajarilgan_deb_belgilash(idx)
        elif tanlov == "3":
            todolist.barcha_vazifalar()
        elif tanlov == "4":
            todolist.bajarilmaganlar()
        elif tanlov == "5":
            break





# Blog Dasturi

class Post:
    def __init__(self, sarlavha, matn, muallif):
        self.sarlavha = sarlavha
        self.matn = matn
        self.muallif = muallif

    def __str__(self):
        return f"{self.sarlavha} | {self.muallif}\n{self.matn}"


class Blog:
    def __init__(self):
        self.postlar = []

    def qo‘shish(self, post):
        self.postlar.append(post)

    def barcha_postlar(self):
        for p in self.postlar:
            print(p)
            print("-" * 20)

    def muallif_postlari(self, muallif):
        for p in self.postlar:
            if p.muallif == muallif:
                print(p)
                print("-" * 20)

    def o‘chirish(self, index):
        if 0 <= index < len(self.postlar):
            self.postlar.pop(index)

    def tahrirlash(self, index, yangi_matn):
        if 0 <= index < len(self.postlar):
            self.postlar[index].matn = yangi_matn

    def oxirgi_postlar(self, n=3):
        for p in self.postlar[-n:]:
            print(p)
            print("-" * 20)



if __name__ == "__main__":
    blog = Blog()

    while True:
        print("\n=== Blog Menyu ===")
        print("1. Post qo‘shish")
        print("2. Barcha postlar")
        print("3. Muallif postlari")
        print("4. Postni o‘chirish")
        print("5. Postni tahrirlash")
        print("6. Oxirgi postlar")
        print("7. Chiqish")

        tanlov = input("Tanlang: ")

        if tanlov == "1":
            s = input("Sarlavha: ")
            m = input("Matn: ")
            a = input("Muallif: ")
            blog.qo‘shish(Post(s, m, a))
        elif tanlov == "2":
            blog.barcha_postlar()
        elif tanlov == "3":
            a = input("Muallif nomi: ")
            blog.muallif_postlari(a)
        elif tanlov == "4":
            idx = int(input("Qaysi post raqami o‘chiriladi? (0,1,2...): "))
            blog.o‘chirish(idx)
        elif tanlov == "5":
            idx = int(input("Qaysi post raqami tahrirlanadi?: "))
            yangi = input("Yangi matn: ")
            blog.tahrirlash(idx, yangi)
        elif tanlov == "6":
            blog.oxirgi_postlar()
        elif tanlov == "7":
            break





# Bank Dasturi

class Hisob:
    def __init__(self, raqam, egasi, balans=0):
        self.raqam = raqam
        self.egasi = egasi
        self.balans = balans

    def __str__(self):
        return f"{self.raqam} | {self.egasi} | Balans: {self.balans}"


class Bank:
    def __init__(self):
        self.hisoblar = {}

    def hisob_ochish(self, raqam, ism, balans=0):
        self.hisoblar[raqam] = Hisob(raqam, ism, balans)

    def balans(self, raqam):
        if raqam in self.hisoblar:
            return self.hisoblar[raqam].balans
        return "Hisob topilmadi!"

    def pul_qo‘shish(self, raqam, miqdor):
        if raqam in self.hisoblar:
            self.hisoblar[raqam].balans += miqdor

    def pul_olish(self, raqam, miqdor):
        if raqam in self.hisoblar:
            if self.hisoblar[raqam].balans >= miqdor:
                self.hisoblar[raqam].balans -= miqdor
            else:
                print("Xato: Mablag‘ yetarli emas!")

    def pul_o‘tkazish(self, dan, ga, miqdor):
        if dan in self.hisoblar and ga in self.hisoblar:
            if self.hisoblar[dan].balans >= miqdor:
                self.hisoblar[dan].balans -= miqdor
                self.hisoblar[ga].balans += miqdor
            else:
                print("Xato: Pul yetarli emas!")

    def barcha_hisoblar(self):
        for h in self.hisoblar.values():
            print(h)


if __name__ == "__main__":
    bank = Bank()

    while True:
        print("\n=== Bank Menyu ===")
        print("1. Hisob ochish")
        print("2. Balans ko‘rish")
        print("3. Pul qo‘shish")
        print("4. Pul olish")
        print("5. Pul o‘tkazish")
        print("6. Barcha hisoblar")
        print("7. Chiqish")

        tanlov = input("Tanlang: ")

        if tanlov == "1":
            r = input("Hisob raqami: ")
            i = input("Ism: ")
            b = int(input("Boshlang‘ich balans: "))
            bank.hisob_ochish(r, i, b)
        elif tanlov == "2":
            r = input("Hisob raqami: ")
            print("Balans:", bank.balans(r))
        elif tanlov == "3":
            r = input("Hisob raqami: ")
            m = int(input("Miqdor: "))
            bank.pul_qo‘shish(r, m)
        elif tanlov == "4":
            r = input("Hisob raqami: ")
            m = int(input("Miqdor: "))
            bank.pul_olish(r, m)
        elif tanlov == "5":
            r1 = input("Qaysi hisobdan: ")
            r2 = input("Qaysi hisobga: ")
            m = int(input("Miqdor: "))
            bank.pul_o‘tkazish(r1, r2, m)
        elif tanlov == "6":
            bank.barcha_hisoblar()
        elif tanlov == "7":
            break

