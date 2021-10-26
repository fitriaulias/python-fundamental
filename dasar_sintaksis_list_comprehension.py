print('\nPerintah del')
daftar_buku = ['The Alchemist', 'Habits', 'Pulang', 'The Second Sex']
del daftar_buku[0]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPerintah del dengan list comprehension')
daftar_buku = ['The Alchemist', 'Habits', 'Pulang', 'The Second Sex']
del daftar_buku[:] # START:END # kalo tidak menjelaskan start dan stopnya berarti menghapus semuanya
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPerintah del dengan list comprehension start')
daftar_buku = ['The Alchemist', 'Habits', 'Pulang', 'The Second Sex']
del daftar_buku[0:-1] # index tetap dimulai dari 0, kalo jumlah dimulai dari 1
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPerintah del dengan list comprhension start end step')
daftar_buku = ['The Alchemist', 'Habits', 'Pulang', 'The Second Sex']
del daftar_buku[0::2] # START:END:STEP # step artinya langkah, jadi kaya lompat gitu(?)
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

# Gunanya hal di atas adalah untuk menciptapkan list elemen baru dari list elemen yang sudah ada

print('\nMembuat list baru')
daftar_buku = ['The Alchemist', 'Habits', 'Pulang', 'The Second Sex']
daftar_buku_baru = daftar_buku[:]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nMembuat list baru')
del daftar_buku[:]
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print('\nMembuat list baru dengan comprehension: ganjil')
daftar_buku = ['1 The Alchemist', '2 Habits', '3 Pulang', '4 The Second Sex']
daftar_buku_baru = daftar_buku[0::2]
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print('\nMembuat list baru dengan comprehension: genap')
daftar_buku = ['1 The Alchemist', '2 Habits', '3 Pulang', '4 The Second Sex']
daftar_buku_baru = daftar_buku[1::2]
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print('\nMembuat list baru dengan comprehension: hanya buang di ujung')
daftar_buku = ['1 The Alchemist', '2 Habits', '3 Pulang', '4 The Second Sex']
daftar_buku_baru = daftar_buku[0:-1:2]
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])