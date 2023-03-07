class Bilgisayar:
    def __init__(self,islemci,ekrankarti,ram,anakart):
        self.islemci = islemci
        self.ekrankarti = ekrankarti
        self.ram = ram
        self.anakart = anakart

    def bilgi(self):
        self.obje = self.islemci, self.ekrankarti, self.ram, self.anakart
        for i in self.obje:
            print(i)

class Güclendirilmis(Bilgisayar):
    def __init__(self, islemci, ekrankarti, ram, anakart, kasa):
        super().__init__(islemci, ekrankarti, ram, anakart)
        self.kasa = kasa 

    def bilgi(self):
        super().bilgi()
        print(self.kasa)

    def degis(self):
        while True:
            print('''İşlemler:
1- İşlemci
2- Ekran Karti
3- Ram
4- Anakart
5- Kasa rengi
6- Çıkış''')
            islem = input("Yapmak istediğiniz değişimin kodunu giriniz: ")
            if islem == "1":
                yeniDeger = input("Güçlendirmek istediğiniz işlemci değerini giriniz: ")
                self.islemci = yeniDeger
            elif islem == "2":
                yeniDeger = input("Güçlendirmek istediğiniz ekran kartını giriniz: ")
                self.marka = yeniDeger
            elif islem == "3":
                yeniDeger = input("Güçlendirmek istediğiniz rami giriniz: ")
                self.ram = yeniDeger
            elif islem == "4":
                yeniDeger = input("Güçlendirmek istediğiniz anakart modelini giriniz: ")
                self.anakart = yeniDeger
            elif islem == "5":
                yeniDeger = input("Değiştirmek istediğiniz kasa rengini giriniz: ")
                self.teker = yeniDeger
            elif islem == "6":
                self.bilgi()
                break
            else:
                print("Geçersiz işlem.")


pc1 = Güclendirilmis("2000mhz", "rx5500xt", "2019", "4", "Siyah")
# pc2 = Güclendirilmis("2500mhz", "rx6500xt", "2023", "4", "Beyaz")
pc1.bilgi()
pc1.degis()