class Negara:
    def __init__(self, nama):
        self.nama = nama


class Universitas:
    def __init__(self, nama, negara_asal):
        self.nama = nama
        self.negara_asal = negara_asal
        negara_asal.universitas = self


negara1 = Negara("Indonesia")
universitas1 = Universitas("Universitas Gadjah Mada", negara1)

print(universitas1.nama)  # Output: Universitas Gadjah Mada
print(universitas1.negara_asal.nama)  # Output: Indonesia
