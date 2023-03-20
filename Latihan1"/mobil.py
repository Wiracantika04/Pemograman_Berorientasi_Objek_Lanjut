class Mobil: 
    def __init__(self, merk, warna):
        self.warna = warna
        self.merk = merk
    def info(self):
        print(f"Mobil {self.merk} berwarna {self.warna}")

MobilA = Mobil("BMW", "Merah")
MobilA.info() 
MobilB = Mobil("Ducati", "Hitam Metalic")
MobilB.info()
