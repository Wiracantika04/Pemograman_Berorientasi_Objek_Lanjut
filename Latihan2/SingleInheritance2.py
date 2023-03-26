class Manusia:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur
    def berbicara(self):
        print(f"{self.nama} sedang berbicara.")

class Dosen(Manusia):
    def __init__(self, nama, umur, nip):
        super().__init__(nama, umur)
        self.nip = nip
    def mengajar(self):
        print(f"{self.nama} dengan NIP {self.nip} sedang mengajar.")

dosenA = Dosen("Wira Cantika", 21, "210511171")
dosenA.berbicara() # Output: Wira sedang berbicara.
dosenA.mengajar() # Output: Wira dengan NIP 210511171 sedang mengajar.