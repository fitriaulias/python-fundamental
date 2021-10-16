"""
Program perulangan membaca buku dengan FOR
"""
jumlah_buku = 10
print('Perintah Ibu, "Baca semua bukumu"')

jumlah_buku_yang_dibaca = 0
print(f'Jumlah buku yang dibaca {jumlah_buku_yang_dibaca}')

for jumlah_buku_yang_dibaca in range(1, jumlah_buku+1):
    print(f"Buku ke {jumlah_buku_yang_dibaca} sudah dibaca")

print(f'Jumlah buku yang sudah dibaca {jumlah_buku_yang_dibaca}')