"""
Program perulangan membaca buku dengan while sampai paham
"""

jumlah_buku = 10
print('Perintah Ibu, "Baca dan pahami semua bukumu"')

jumlah_buku_yang_dibaca_dan_dipahami = 0
print(f"Jumlah buku yang sudah dibaca dan dipahami {jumlah_buku_yang_dibaca_dan_dipahami}")

total_jumlah_baca = 0

while total_jumlah_baca < jumlah_buku * 2:
    total_jumlah_baca = total_jumlah_baca + 1
    if jumlah_buku_yang_dibaca_dan_dipahami == 9:
        print(f"Buku ke {jumlah_buku_yang_dibaca_dan_dipahami + 1} belum paham")
    else:
        jumlah_buku_yang_dibaca_dan_dipahami = jumlah_buku_yang_dibaca_dan_dipahami + 1
        print(f"Buku ke {jumlah_buku_yang_dibaca_dan_dipahami} sudah dibaca dan dipahami")

print(f"Jumlah buku yang sudah dibaca dan dipahami adalah {jumlah_buku_yang_dibaca_dan_dipahami} buku")
if jumlah_buku_yang_dibaca_dan_dipahami == jumlah_buku:
    print('"Bu, semua buku sudah dibaca dan dipahami."')
else:
    print(f'"Bu, tidak semua buku bisa dipahami, buku yang Budi pahami hanya {jumlah_buku_yang_dibaca_dan_dipahami}" buku')