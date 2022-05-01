class Calisan():
    personel=[]
    def __init__(self, isim):
        self.isim=isim
        self.kabiliyyetleri=[]
        self.personel_ekle()


def personel_ekle(self):
    self.personel.append(self.isim)
    print('{} adli kisi personele eklendi'.format(self.isim))


def personeli_goruntule(self):
    print('personel listesi: ')
    for kisi in self.personel:
        print(kisi)


def kabiliyyet_ekle(self, kabiliyyet):
    self.kabiliyyetleri.append(kabiliyyet)


def kabiliyyetleri_goruntule(self):
    print('{} adli kisinin kabiliyyetleri:'.format(self.isim))
    for kabiliyyet in self.kabiliyyetleri:
        print(kabiliyyet)
a=Calisan()