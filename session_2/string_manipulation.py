""" Manipulasi String
String adalah urutan karakter dan memiliki banyak metode bawaan untuk manipulasi.
"""


####### String Dasar #######
teks = "Belajar Python itu Menyenangkan"

# Mengubah huruf besar/kecil
print(teks.upper())      # BELAJAR PYTHON ITU MENYENANGKAN
print(teks.lower())      # belajar python itu menyenangkan
print(teks.title())      # Belajar Python Itu Menyenangkan
print(teks.capitalize()) # Belajar python itu menyenangkan
print(teks.swapcase())   # bELAJAR pYTHON ITU mENYENANGKAN

# Pencarian
print(teks.count("a"))                # Output: 3
print(teks.find("Python"))            # Output: 8 (indeks posisi awal)
print(teks.find("Java"))              # Output: -1 (tidak ditemukan)
print("Python" in teks)               # Output: True
print(teks.startswith("Belajar"))     # Output: True
print(teks.endswith("Menyenangkan"))  # Output: True

# Pemeriksaan karakter
print("123".isdigit())    # Output: True
print("abc".isalpha())    # Output: True
print("abc123".isalnum()) # Output: True
print("  ".isspace())     # Output: True


####### Pemformatan String #######
# Menggabungkan string (concatenation)
nama = "Budi"
sapaan = "Halo " + nama + "!"
print(sapaan)  # Output: Halo Budi!

# Format method
umur = 25
pesan = "Nama saya {}, umur {} tahun".format(nama, umur)
print(pesan)  # Output: Nama saya Budi, umur 25 tahun

# Format dengan posisi
pesan = "Saya {1} berumur {0} tahun".format(umur, nama)
print(pesan)  # Output: Saya Budi berumur 25 tahun

# Format dengan nama
pesan = "Nama: {nama}, Umur: {umur}".format(nama=nama, umur=umur)
print(pesan)  # Output: Nama: Budi, Umur: 25

# f-string (Python 3.6+, paling disarankan)
pesan = f"Halo, nama saya {nama} dan saya berusia {umur} tahun"
print(pesan)  # Output: Halo, nama saya Budi dan saya berusia 25 tahun

# Memformat angka
pi = 3.14159
print(f"Nilai pi dibulatkan: {pi:.2f}")  # Output: Nilai pi dibulatkan: 3.14

# Padding dan alignment
for i in range(1, 6):
    print(f"{i:2d} {i**2:3d} {i**3:4d}")
# Output:
#  1   1    1
#  2   4    8
#  3   9   27
#  4  16   64
#  5  25  125

####### Memotong dan Membagi String  #######
teks = "Python adalah bahasa pemrograman yang hebat"

# Slicing string (mirip dengan list)
print(teks[0:6])      # Output: Python
print(teks[-5:])      # Output: hebat
print(teks[::-1])     # Output: tabeh gnay naamargormep asahab halada nohtyP

# Pemisahan string
kata = teks.split()
print(kata)  # Output: ['Python', 'adalah', 'bahasa', 'pemrograman', 'yang', 'hebat']

csv = "apel,jeruk,mangga,pisang"
buah = csv.split(",")
print(buah)  # Output: ['apel', 'jeruk', 'mangga', 'pisang']

# Penggabungan string
kalimat = " ".join(kata)
print(kalimat)  # Output: Python adalah bahasa pemrograman yang hebat

daftar_buah = ", ".join(buah)
print(daftar_buah)  # Output: apel, jeruk, mangga, pisang

####### Pemrosesan String Lainnya #######
# Menghapus whitespace
teks = "   Python   "
print(teks.strip())    # Output: Python
print(teks.lstrip())   # Output: Python   
print(teks.rstrip())   # Output:    Python

# Mengganti substring
kalimat = "Saya suka jeruk, jeruk sangat segar"
print(kalimat.replace("jeruk", "apel"))  # Output: Saya suka apel, apel sangat segar
print(kalimat.replace("jeruk", "apel", 1))  # Output: Saya suka apel, jeruk sangat segar (hanya 1 kali)

# Membagi string menjadi baris
teks_baris = "Baris 1\nBaris 2\nBaris 3"
baris = teks_baris.splitlines()
print(baris)  # Output: ['Baris 1', 'Baris 2', 'Baris 3']

# Mengecek awalan dan akhiran untuk setiap item
files = ["document.txt", "image.jpg", "music.mp3", "video.mp4"]
txt_files = [f for f in files if f.endswith(".txt")]
print(txt_files)  # Output: ['document.txt']

""" String sebagai Sequence
String di Python bersifat immutable (tidak dapat diubah) dan dapat diperlakukan sebagai urutan karakter.
 """
 
 # Iterasi melalui karakter
for char in "Python":
    print(char)

# List comprehension dengan string
huruf_kapital = [c.upper() for c in "python"]
print(huruf_kapital)  # Output: ['P', 'Y', 'T', 'H', 'O', 'N']

# String tidak dapat diubah (immutable)
kata = "Python"
# kata[0] = "J"  # Error: TypeError
# Sebagai gantinya, buat string baru
kata = "J" + kata[1:]
print(kata)  # Output: Jython