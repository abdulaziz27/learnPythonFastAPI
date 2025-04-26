# Variable and Data Types in Python
name = "Abdul Aziz"
age = 22
ipk = 3.81
is_graduate = False
height = 1.75
weight = "60"
address = """Jl. Pelangi 3, Perumahan Elite Cileungsi Blok Zero No. 1, Jawa Barat, Indonesia"""
girlfriend = None

# Print Variable
print("Name:", name)
print("Age:", age, "Years Old")
print(f"IPK: {ipk}/4.0")
print("Is Graduate:", "Graduated" if is_graduate else "Not Graduated")


# Change Variable Value
age = 23
is_graduate = True

print("2025 Gonna be", age, "Years Old" + " And", "Graduated" if is_graduate else "Still Not Graduated")


# Data Type Conversion

print("\n=============== Data Type Conversion ================")

# Convert int to string
age_str = str(age) 
print("Age as String:", age_str, type(age_str))

print(str(age) + " Years Old")

# Convert string to int
weight_int = int(weight)

print("Weight as Integer:", weight_int, type(weight_int))
print("Weight:", weight_int, "Kg" if weight_int > 50 else "Lightweight")

# Convert float to int
ipk_int = int(ipk)
print("IPK as Integer:", ipk_int, type(ipk_int))
print("IPK:", ipk_int, "Out of 4.0" if ipk_int > 3 else "Not Graduated")

# Convert string to float
weight_float = float(weight)
print("Weight as Float:", weight_float - 5)

# Manipulation

print("\n=============== Manipulation ================")

""" 
Slicing [start:stop:step] (Termasuk [::-1])
Fungsi: Memotong/mengakses elemen string, list, atau array dengan pola tertentu.
Format: [mulai:akhir:langkah]
"""

teks = "Python"
print(teks[::2])    # "Pto" (ambil setiap 2 langkah)
print(teks[::-1])   # "nohtyP" (balik urutan)
print(teks[1:4])    # "yth" (indeks 1 sampai 3)

""" 
Operasi Cepat String (replace(), lower(), dll.)
Fungsi: Memanipulasi string tanpa perlu loop manual.
"""


# Ganti semua 'a' dengan 'x' dan hapus spasi
"anak kambing".replace("a", "x").replace(" ", "")  # "xnkxkmbing"

# Huruf kecil dan hapus karakter non-alphabet
"Hello!123".lower().strip("!123")  # "hello"

""" 
Fungsi range() dengan Step
Fungsi: Membuat deret angka dengan pola tertentu.
"""

list(range(0, 10, 2))  # [0, 2, 4, 6, 8] (loncat 2)
list(range(5, 0, -1))  # [5, 4, 3, 2, 1] (mundur)

""" 
List Comprehension (Shortcut Loop)
Fungsi: Membuat list dengan 1 baris. 
"""

# Kuadrat dari 0 sampai 4
[x**2 for x in range(5)]  # [0, 1, 4, 9, 16]

# Filter bilangan genap
[x for x in range(10) if x % 2 == 0]  # [0, 2, 4, 6, 8]


""" 
Ternary Operator (If-Else Singkat)
Fungsi: Menyingkat pengecekan kondisi. 
"""

status = "Palindrom" if teks == teks[::-1] else "Bukan"
# Setara dengan:
if teks == teks[::-1]:
    status = "Palindrom"
else:
    status = "Bukan"
    
"""     
Fungsi map() dan filter()
Fungsi: Memproses list tanpa loop eksplisit.
"""

# Kalikan semua elemen dengan 2
list(map(lambda x: x*2, [1, 2, 3]))  # [2, 4, 6]

# Filter yang > 2
list(filter(lambda x: x > 2, [1, 2, 3, 4]))  # [3, 4]