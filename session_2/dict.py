""" Dictionaries (Kamus)
Dictionary adalah struktur data yang menyimpan pasangan key-value. Dictionary sangat berguna untuk pemetaan dan
pencarian data berdasarkan kunci.
"""

####### Membuat Dictionary #######

# Dictionary kosong
dict_kosong = {}
dict_kosong2 = dict()

# Dictionary dengan elemen
siswa = {
    "nama": "Andi",
    "umur": 20,
    "jurusan": "Informatika",
    "lulus": True
}

# Membuat dengan dict()
pegawai = dict(
    nama="Budi", 
    posisi="Manager", 
    gaji=10000000
)

# Membuat dari list pasangan tuple
item_harga = dict([("apel", 5000), ("jeruk", 7000), ("anggur", 15000)])


####### Mengakses dan Memodifikasi Dictionary #######

siswa = {
    "nama": "Andi",
    "umur": 20,
    "jurusan": "Informatika",
    "nilai": {
        "matematika": 85,
        "pemrograman": 90,
        "database": 78
    }
}

# Mengakses nilai dengan kunci
print(siswa["nama"])     # Output: Andi

# Alternatif dengan get() (lebih aman)
print(siswa.get("alamat"))         # Output: None
print(siswa.get("alamat", "Tidak ada"))  # Output: Tidak ada (nilai default)

# Mengakses nested dictionary
print(siswa["nilai"]["pemrograman"])  # Output: 90

# Menambah atau mengubah elemen
siswa["semester"] = 3              # Menambah entry baru
siswa["umur"] = 21                 # Mengubah nilai
siswa["nilai"]["database"] = 85    # Mengubah nilai nested

# Menghapus elemen
del siswa["jurusan"]               # Menghapus entry
nilai_mat = siswa["nilai"].pop("matematika")  # Menghapus dan mengembalikan nilai
item = siswa.popitem()             # Menghapus dan mengembalikan (key, value) terakhir

# Membersihkan dictionary
siswa.clear()                      # Dictionary kosong

####### Metode Dictionary Lainnya #######

pegawai = {
    "id": "E001",
    "nama": "Sinta",
    "departemen": "IT",
    "gaji": 8500000
}

# Mendapatkan semua kunci
keys = pegawai.keys()
print(list(keys))  # Output: ['id', 'nama', 'departemen', 'gaji']

# Mendapatkan semua nilai
values = pegawai.values()
print(list(values))  # Output: ['E001', 'Sinta', 'IT', 8500000]

# Mendapatkan semua pasangan (key, value)
items = pegawai.items()
print(list(items))  # Output: [('id', 'E001'), ('nama', 'Sinta'), ('departemen', 'IT'), ('gaji', 8500000)]

# Menyalin dictionary
pegawai_copy = pegawai.copy()

# Memperbarui dictionary dengan dictionary lain
update_info = {"gaji": 9000000, "status": "Tetap"}
pegawai.update(update_info)
print(pegawai)  # 'gaji' diupdate dan 'status' ditambahkan


####### Dictionary Comprehension #######

# Membuat dictionary dengan dictionary comprehension
angka_kuadrat = {x: x**2 for x in range(1, 6)}
print(angka_kuadrat)  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Dengan kondisional
angka_genap_kuadrat = {x: x**2 for x in range(1, 11) if x % 2 == 0}
print(angka_genap_kuadrat)  # Output: {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}

# Transformasi dictionary
harga = {"apel": 5000, "jeruk": 7000, "pisang": 3000}
harga_diskon = {item: harga * 0.9 for item, harga in harga.items()}
print(harga_diskon)  # Output: {'apel': 4500.0, 'jeruk': 6300.0, 'pisang': 2700.0}
