"""
Konsep perulangan WHILE, menggunakan flowchart baca buku

infinite loop: perulangan yang ga berujung
"""

jumlah_buku = 17
print('Perintah Ibu, "Baca semua bukumu."')

jumlah_buku_yang_dibaca = 0

while jumlah_buku_yang_dibaca < jumlah_buku:
    jumlah_buku_yang_dibaca = jumlah_buku_yang_dibaca + 1
    print(f"Buku ke {jumlah_buku_yang_dibaca} sudah dibaca")

print(f"Jumlah buku yang sudah dibaca {jumlah_buku_yang_dibaca}")
