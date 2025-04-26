print("\n================ #1 Variabel dan Tipe Data ====================")
# Pertanyaan 1: Variabel dan Tipe Data

a = 5
b = "10"
c = a + int(b)

# print(c)

print("\n================ #2 Alur Kontrol ====================")
# Pertanyaan 2: Alur Kontrol
# mencetak angka 1 sampai 10, tetapi hanya angka ganjil saja.

for i in range (1, 10):
    if i % 2 != 0:
        print(i, end=" ")
        
# print()

print("\n================ #3 Pengkondisian ====================")
# Pertanyaan 3: Pengkondisian
# Buatlah program yang menerima input nilai ujian (0-100) dan mencetak "Lulus" jika nilai minimal 70, dan "Tidak Lulus" jika nilai di bawah 70.


def exam_result():
    input_score = int(input("Input your score (1-100): "))
    if input_score >= 70:
        print(f"Nilai {input_score} = Lulus")
    else:
        print("Nilai {input_score} = Tidak Lulus")

def exam_result_simpler():
    input_score = int(input("Input your score (1-100): "))
    print(f"Lulus" if input_score >= 70 else "Tidak Lulus") 
    
# exam_result()
# exam_result_simpler()
    

print("\n================ #4 Fungsi ====================")
# Pertanyaan 4: Fungsi
# Buatlah fungsi bernama hitung_faktorial yang menerima satu parameter bilangan bulat dan mengembalikan nilai faktorial dari bilangan tersebut. (Contoh: faktorial 5 = 5 × 4 × 3 × 2 × 1 = 120)

def hitung_faktorial(bilangan):
    hasil = 1
    
    for i in range(1, bilangan + 1):
        hasil *= i
        print(f"Iterasi {i}: hasil = {hasil}")
        
    return hasil

# hitung_faktorial(5)

def process_hitung_faktorial(bilangan):
    hasil = 1
    proses = []
    
    for i in range (bilangan, 0, -1):
        hasil *= i
        proses.append(str(i))
        
    langkah = " × ".join(proses)
    print(f"hasil dari faktorial {bilangan} = {langkah} = {hasil}")
    
    return hasil
    
# process_hitung_faktorial(3)

# Atau dengan pendekatan rekursif:
def hitung_faktorial_rekursif(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * hitung_faktorial_rekursif(n-1)
        
    
    
print("\n================ #5 Program Lengkap ====================")
# Pertanyaan 5: Program Lengkap
""" Buatlah program yang:

Meminta input nama dan umur dari pengguna
Memiliki fungsi kategori_umur yang menentukan kategori umur:

"Anak-anak" jika umur < 13
"Remaja" jika umur 13-17
"Dewasa" jika umur 18-59
"Lansia" jika umur >= 60


Mencetak pesan "Halo [nama], Anda termasuk kategori [kategori]"
"""

def kategori_umur(umur):
    if umur < 13:
        return "Anak-anak"
    elif 13 <= umur <= 17:
        return "Remaja"
    elif 18 <= umur <= 59:
        return "Dewasa"
    else:
        return "Lansia"

# Input dari pengguna
nama = input("Masukkan nama Anda: ")
umur = int(input("Masukkan umur Anda: "))

# Mendapatkan kategori
kategori = kategori_umur(umur)

# Output
print(f"Halo {nama}, Anda termasuk kategori {kategori}")
    
    
# Additional Questions

print("\n================ #6 Kalkulator ====================")
# 6
# Buatlah program kalkulator sederhana yang dapat melakukan operasi penjumlahan, pengurangan, perkalian, dan pembagian.
def kalkulator():
    print("Kalkulator Sederhana")
    print("Operasi yang tersedia: +, -, *, /")
    
    # user input
    angka1 = float(input("Masukkan angka pertama: "))
    operasi = input("Masukkan operasi (+, -, *, /): ")
    angka2 = float(input("Masukkan angka kedua: ")) 
    hasil = None
    
    # Melakukan operasi sesuai input
    if operasi == "+":
        hasil = angka1 + angka2
        print(f"Hasil {angka1} + {angka2} = {hasil}")
    elif operasi == "-":
        hasil = angka1 - angka2
        print(f"Hasil {angka1} - {angka2} = {hasil}")
    elif operasi == "*":
        hasil = angka1 * angka2
        print(f"Hasil {angka1} * {angka2} = {hasil}")
    elif operasi == "/":
        if angka2 == 0:
            print("Error: Pembagian dengan nol tidak diperbolehkan")
        else:
            hasil = angka1 / angka2
            print(f"Hasil {angka1} / {angka2} = {hasil}")
    else:
        print("Operasi tidak valid")
        
    return hasil

# kalkulator()

print("\n================ #7 Table Multiplication ====================")
# 7 : Table Multiplication
# Buatlah program yang menerima input angka dan mencetak tabel perkalian untuk angka tersebut dari 1 sampai 10.
def tabel_perkalian(angka):
    print(f"Tabel Perkalian untuk {angka}:")
    print("-" * 20)
    
    for i in range(1, 11):
        hasil = angka * i
        print(f"{angka} x {i} = {hasil}")

# Input dari pengguna
angka = int(input("Masukkan angka untuk tabel perkalian: "))
tabel_perkalian(angka)
    

print("\n================ #8 Palindrom Check ====================")
# 8 Palindrom Check

def check_palindrom(text):
    
    # hapus spasi ubah ke lowercase
    text = text.replace(" ", "").lower()
    
    if text == text[::-1]:
        return True
    else:
        return False
    
input_text = input("Masukan teks: ")

if check_palindrom(input_text):
    print(f'"{input_text}" adalah palindrom')
else:
    print(f'"{input_text}" bukan palindrom')
