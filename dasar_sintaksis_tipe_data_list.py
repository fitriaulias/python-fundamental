daftar_buku = ['The Alchemist', 'Sapiens', 'Habits']
print('Tampilkan variable daftar_buku')
print(daftar_buku)

"""
Kalo mau ditampilkan satu per satu pake FOR, 'buku' adalah variabel baru
"""

print('\nProses semua dengan for in')
for buku in daftar_buku:
    print(buku)

"""
Kamu juga bisa mengoleh element satu per satu seperti ini
"""

print('\nTampilkan isi daftar_buku pada indeks tertentu')
print(daftar_buku[0])
print(daftar_buku[2])

print('\nTampilkan dengan for in range')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

daftar_buku = [1, 'Kenji Volume 2', -317, 3.14]

print('\nTampilkan dengan for in range, dimana tiap data per element berbeda-beda')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

"""
Jika ingin menambahkan element baru
"""

print('\nKembalikan nilai awal daftar_buku')
daftar_buku = ['The Alchemist', 'Sapiens', 'Habits']
daftar_buku.append('The Warrior of the Light')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])


print('\nClear list')
daftar_buku.clear()
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nGanti elemen pertama')
daftar_buku = ['The Alchemist', 'Sapiens', 'Habits', 'Warrior of the Light']
daftar_buku[0] = 'The Scientist'
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])


print('\nAmbil elemen ke-2')
buku = daftar_buku.pop(1)
for i in range (0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nBuku yang diambil tadi')
print(buku)

print('\nPop')
daftar_buku.pop(-1)
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])