"""
List adalah struktur data yang paling serbaguna di Python. List dapat menyimpan kumpulan item yang diurutkan dan dapat
diubah (mutable).
"""

##### Membuat List ####

# List kosong
daftar_kosong = []

# List dengan item
buah = ["apel", "jeruk", "mangga", "pisang"]
angka = [1, 2, 3, 4, 5]
campuran = [1, "dua", 3.0, True, [5, 6]] # List bisa berisi berbagai tipe data

# List dengan fungsi list()
karakter = list("Python") # ['P', 'y', 't', 'h', 'o', 'n']


#### Mengakses Elemen List ####

buah = ["apel", "jeruk", "mangga", "pisang", "anggur"]

# Mengakses dengan indeks (dimulai dari 0)
print(buah[0]) # Output: apel
print(buah[2]) # Output: mangga

# Indeks negatif (menghitung dari belakang)
print(buah[-1]) # Output: anggur (elemen terakhir)
print(buah[-2]) # Output: pisang (elemen kedua dari belakang)

# Slicing [start:stop:step]
print(buah[1:3]) # Output: ['jeruk', 'mangga'] (dari indeks 1 hingga 2)
print(buah[1:]) # Output: ['jeruk', 'mangga', 'pisang', 'anggur'] (dari indeks 1 hingga akhir)
print(buah[:3]) # Output: ['apel', 'jeruk', 'mangga'] (dari awal hingga indeks 2)
print(buah[::2]) # Output: ['apel', 'mangga', 'anggur'] (setiap elemen kedua)
print(buah[::-1]) # Output: ['anggur', 'pisang', 'mangga', 'jeruk', 'apel'] (dibalik)


###### Operasi Umum pada List ####

buah = ["apel", "jeruk", "mangga"]

# Menambahkan elemen
buah.append("pisang") # Menambahkan di akhir: ['apel', 'jeruk', 'mangga', 'pisang']
buah.insert(1, "stroberi") # Menyisipkan pada indeks: ['apel', 'stroberi', 'jeruk', 'mangga', 'pisang']

# Menghapus elemen
buah.remove("jeruk") # Menghapus nilai: ['apel', 'stroberi', 'mangga', 'pisang']
buah_terakhir = buah.pop() # Menghapus & mengembalikan elemen terakhir: 'pisang'
print(buah) # Output: ['apel', 'stroberi', 'mangga']
del buah[0] # Menghapus dengan indeks: ['stroberi', 'mangga']

# Menggabungkan list
list1 = [1, 2, 3]
list2 = [4, 5, 6]
gabungan = list1 + list2 # Output: [1, 2, 3, 4, 5, 6]
list1.extend(list2) # list1 sekarang: [1, 2, 3, 4, 5, 6]

# Mengulang list
ulang = [0] * 5 # Output: [0, 0, 0, 0, 0]


####### Fungsi dan Metode List Lainnya ######

angka = [5, 2, 8, 1, 9, 3]
nama = ["Budi", "Ani", "Citra", "Dodi"]

# Panjang list
print(len(angka)) # Output: 6

# Mencari nilai minimum dan maksimum
print(min(angka)) # Output: 1
print(max(angka)) # Output: 9

# Mengurutkan list
angka.sort() # Mengurutkan secara menaik: [1, 2, 3, 5, 8, 9]
nama.sort() # Mengurutkan secara alfabetis: ['Ani', 'Budi', 'Citra', 'Dodi']
angka.sort(reverse=True) # Mengurutkan secara menurun: [9, 8, 5, 3, 2, 1]

# Membalik urutan list
nama.reverse() # ['Dodi', 'Citra', 'Budi', 'Ani']

# Mendapatkan indeks suatu nilai
print(nama.index("Citra")) # Output: 1

# Menghitung kemunculan suatu nilai
data = [1, 2, 3, 2, 4, 2, 5]
print(data.count(2)) # Output: 3 (nilai 2 muncul 3 kali)

# Memeriksa keberadaan suatu nilai
print("Ani" in nama) # Output: True
print("Eko" in nama) # Output: False

# Membersihkan list
data.clear() # data sekarang: []
