try:
    a = [0]* (10 ** 8)
except MemoryError:
    print("Kesalahan memori terdeteksi. Coba kurangi jumlah memori yang digunakan.")
