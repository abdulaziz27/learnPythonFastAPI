""" Comprehensions
Comprehension adalah cara singkat dan ekspresif untuk membuat struktur data baru dari struktur data yang sudah ada.
"""

####### List Comprehension #######
# Dasar list comprehension
angka = [1, 2, 3, 4, 5]
kuadrat = [x**2 for x in angka]
print(kuadrat)  # Output: [1, 4, 9, 16, 25]

# Dengan kondisional
angka_genap = [x for x in range(1, 11) if x % 2 == 0]
print(angka_genap)  # Output: [2, 4, 6, 8, 10]

# Dengan if-else
hasil = ["genap" if x % 2 == 0 else "ganjil" for x in range(1, 6)]
print(hasil)  # Output: ['ganjil', 'genap', 'ganjil', 'genap', 'ganjil']

# Nested list comprehension
matriks = [[i*j for j in range(1, 4)] for i in range(1, 4)]
print(matriks)  # Output: [[1, 2, 3], [2, 4, 6], [3, 6, 9]]


####### Set Comprehension #######
# Set comprehension
teks = "hello world"
huruf_unik = {char for char in teks if char.isalpha()}
print(huruf_unik)  # Output: {'h', 'e', 'l', 'o', 'w', 'r', 'd'}

# Dengan transformasi
angka = [1, 2, 2, 3, 3, 3, 4, 4, 5]
kuadrat_unik = {x**2 for x in angka}
print(kuadrat_unik)  # Output: {1, 4, 9, 16, 25}

####### Dictionary Comprehension (Ulasan) #######
# Membuat dictionary dari dua list
nama = ["Andi", "Budi", "Citra"]
nilai = [85, 90, 78]
hasil_ujian = {nama[i]: nilai[i] for i in range(len(nama))}
print(hasil_ujian)  # Output: {'Andi': 85, 'Budi': 90, 'Citra': 78}

# Filtering dengan comprehension
nilai_siswa = {"Andi": 85, "Budi": 90, "Citra": 78, "Dodi": 60, "Eka": 95}
lulus = {nama: nilai for nama, nilai in nilai_siswa.items() if nilai >= 70}
print(lulus)  # Output: {'Andi': 85, 'Budi': 90, 'Citra': 78, 'Eka': 95}


