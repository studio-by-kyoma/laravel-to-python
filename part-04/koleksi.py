# Membuat list
buah = ["apel", "mangga", "pisang"]

print(buah)
print(buah[0])
print(buah[-1])

# Mengubah list
buah.append("jeruk")
buah[1] = "durian"
buah.remove("apel")

print(buah)

# Mengiris, menghitung, dan mengecek isi
angka = [10, 20, 30, 40, 50]

print(angka[1:3])
print(len(angka))
print(30 in angka)

# Tuple: seperti list tapi tidak bisa diubah
koordinat = (-8.65, 115.21)

print(koordinat)
print(koordinat[0])