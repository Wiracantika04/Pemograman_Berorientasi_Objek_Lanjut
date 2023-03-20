class mahasiswa:
    def __init__(self, nama, npm):
        self.nama = nama
        self.npm = npm
    
    def info(self):
        print(f"Nama: {self.nama}\nnpm: {self.npm}")
    
mahasiswaA = mahasiswa("fahmi", "33774419")
mahasiswaA.info()
mahasiswaB = mahasiswa("fahcrul", "22889919")
mahasiswaB.info()