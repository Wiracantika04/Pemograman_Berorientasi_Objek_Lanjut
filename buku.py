class Buku:
    def __init__(self, judul, penulis, tahunterbit):
        self.judul = judul
        self.penulis = penulis
        self.tahunterbit = tahunterbit
    def info(self):
        print(f"Judul: {self.judul}\nPenulis: {self.penulis}\nTahun Terbit: {self.tahunterbit}")
bukuA = Buku("Belajar Permograman Python", "Wira Cantika", "terbit tahun 2022")
bukuA.info()