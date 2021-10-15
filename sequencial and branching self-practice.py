# Sequencial

print('Ibu memberi perintah, "Beli 1 botol susu"')
print('Anak menjawab, "Oke"')
print("Anak pergi ke toko")

# Branching

jumlah_susu_botol = 173
jumlah_telur = 500
print(f"Jumlah susu {jumlah_susu_botol} botol")
print(f"Jumlah telur {jumlah_telur} butir")

if jumlah_susu_botol > 0:
    print("Anak mengecek harganya, cukup")
    print("Anak membeli 1 botol susu")
    if jumlah_telur == 0:
        print("Anak tidak membeli telur")
    else:
        print("Anak membeli 6 telur")

else:
    print("Anak tidak jadi membeli susu")

print("Anak pulang ke rumah")
print("Anak menyerahkan hasil belanja dan atau uang yang tersisa kepada ibu")
print("Anak belajar dengan rajin")


