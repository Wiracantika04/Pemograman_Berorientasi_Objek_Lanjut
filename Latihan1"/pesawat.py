class pesawat:
    def __init__(self, maskapai, tujuan, kodekeberangkatan):
        self.maskapai = maskapai
        self.tujuan = tujuan
        self.kodepenerbangan = kodekeberangkatan
    def info(self):
        print(f"Maskapai: {self.maskapai}\nTujuan: {self.tujuan}\nKode Keberangkatan: {self.kodepenerbangan}")
pesawatA = pesawat("lionair", "jakarta - Dubai ", "553507414")
pesawatA.info()
