class Produser:
    def __init__(self, nama):
        self.nama = nama


class Film:
    def __init__(self, judul, tahun, produser):
        self.judul = judul
        self.tahun = tahun
        self.produser = produser
        produser.film = self


produser1 = Produser("Joko")
film1 = Film("Bumi Manusia", 2019, produser1)

print(film1.judul)  # Output: Bumi Manusia
print(film1.tahun)  # Output: 2019
print(film1.produser.nama)  # Output: Joko
