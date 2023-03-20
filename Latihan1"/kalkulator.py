class kalkulator:
    @staticmethod
    def add(x, y):
        return x + y
    
    @staticmethod
    def subtract(x, y):
        return x - y
    
    @staticmethod
    def multiply(x, y):
        return x * y
    
    @staticmethod
    def divide(x, y):
        if y == 0:
            raise ValueError('tidak dapat membagi nol!')
        return x / y 
    
    @staticmethod
    def mod(x, y):
        return x % y
    
    @staticmethod
    def floordivision(x, y):
        return x // y
    
print(f'Pertambahan\t= {kalkulator.add(5,3)}')
print(f'Pengurangan\t= {kalkulator.subtract(9,3)}')
print(f'Perkalian\t= {kalkulator.multiply(6,9)}')
print(f'Pembagian\t= {kalkulator.divide(8,10)}')
print(f'Modulus\t\t= {kalkulator.mod(8,80)}')
print(f'Floor Division\t= {kalkulator.floordivision(14,11)}')