# Membuat string
sapaan = "Halo"
nama = "Kris"

print(sapaan)
print(nama)

# Menggabungkan string pakai tanda plus
pesan = sapaan + ", " + nama
print(pesan)

# Cara yang lebih rapi: f-string
umur = 28
intro = f"Namaku {nama}, umurku {umur} tahun"
print(intro)

# Beberapa metode string yang sering dipakai
kalimat = "Belajar Python Itu Seru"

print(kalimat.upper())
print(kalimat.lower())
print(kalimat.replace("Seru", "Mudah"))
print(len(kalimat))