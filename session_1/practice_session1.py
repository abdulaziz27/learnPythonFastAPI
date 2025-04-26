print("\n================ #1 ====================")
# Pertanyaan 1: Variabel dan Tipe Data

a = 5
b = "10"
c = a + int(b)

print(c)

print("\n================ #2 ====================")
# Pertanyaan 2: Alur Kontrol
# mencetak angka 1 sampai 10, tetapi hanya angka ganjil saja.

for i in range (1, 10):
    if i % 2 != 0:
        print(i, end=" ")
        
print()

print("\n================ #3 ====================")
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
    
exam_result()
exam_result_simpler()
    

print("\n================ #4 ====================")
# Pertanyaan 4: Fungsi
# Buatlah fungsi bernama hitung_faktorial yang menerima satu parameter bilangan bulat dan mengembalikan nilai faktorial dari bilangan tersebut. (Contoh: faktorial 5 = 5 × 4 × 3 × 2 × 1 = 120)

def hitung_faktorial(bilangan):
    hasil = 1
    
    for i in range(1, bilangan + 1):
        hasil *= i
        print(f"Iterasi {i}: hasil = {hasil}")
        
    return hasil

hitung_faktorial(5)

def process_hitung_faktorial(bilangan):
    hasil = 1
    proses = []
    
    for i in range (bilangan, 0, -1):
        hasil *= i
        proses.append(str(i))
        
    langkah = " × ".join(proses)
    print(f"hasil dari faktorial {bilangan} = {langkah} = {hasil}")
    
    return hasil
    
process_hitung_faktorial(3)

# Atau dengan pendekatan rekursif:
def hitung_faktorial_rekursif(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * hitung_faktorial_rekursif(n-1)
        
    
    
print("\n================ #5 ====================")
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
    
    
        