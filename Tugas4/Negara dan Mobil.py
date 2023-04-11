class Negara:
    def __init__(self, nama):
        self.nama = nama


class Mobil:
    def __init__(self, merk, negara_pembuat):
        self.merk = merk
        self.negara_pembuat = negara_pembuat
        negara_pembuat.mobil = self


negara1 = Negara("Jepang")
mobil1 = Mobil("Toyota", negara1)

print(mobil1.merk)  # Output: Toyota
print(mobil1.negara_pembuat.nama)  # Output: Jepang
