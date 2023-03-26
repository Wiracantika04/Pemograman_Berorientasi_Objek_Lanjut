class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim
    def belajar(self):
        print(self.nama, "sedang belajar")

class Pekerja:
    def __init__(self, nama, pekerjaan):
        self.nama = nama
        self.pekerjaan = pekerjaan
    def bekerja(self):
        print(self.nama, "sedang bekerja")

class MahasiswaPekerja(Mahasiswa, Pekerja):
    def __init__(self, nama, nim, pekerjaan):
        Mahasiswa.__init__(self, nama, nim)
        Pekerja.__init__(self, nama, pekerjaan)
    def bersosialisasi(self):
        print(self.nama, "sedang bersosialisasi")

mhs_pekerja = MahasiswaPekerja("Wira", "210511171", "Programmer python")
mhs_pekerja.belajar() # output: Wira sedang belajar
mhs_pekerja.bekerja() # output: Wira sedang bekerja
mhs_pekerja.bersosialisasi() # output: Wira sedang bersosialisasi