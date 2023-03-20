class Persegi:
    def __init__(self, panjang, lebar):       
        self.panjang = panjang
        self.lebar = lebar

    def Luas(self):
        L = self.panjang*self.lebar
        return L
    
    def Keliling(self):
        K = (2* self.panjang) + (2*self.lebar)
        return K
    
pj = float(input("Masukan Nilai Panjang:"))
lb = float(input("Masukan Nilai Lebar:"))
A = Persegi(pj, lb)
Luas = A.Luas()
Keliling = A.Keliling()
print("Luas Adalah",str(Luas))