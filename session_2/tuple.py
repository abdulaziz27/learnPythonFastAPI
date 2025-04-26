"""
Tuple mirip dengan list, tetapi tidak dapat diubah (immutable) setelah dibuat. Tuple biasanya digunakan untuk data yang
tidak perlu diubah.
"""


# Kapan Menggunakan Tuple vs List

"""
Gunakan tuple ketika data:

Tidak perlu diubah setelah dibuat
Digunakan sebagai kunci dictionary
Perlu digunakan dalam konteks yang memerlukan data yang tidak berubah


Gunakan list ketika data:

Perlu diubah (ditambah, dihapus, dimodifikasi)
Perlu operasi seperti sorting, filtering yang mengubah data asli
"""

####### Membuat Tuple #######

# Tuple kosong
tuple_kosong = ()

# Tuple dengan satu elemen (perhatikan koma)
satu_elemen = (5,) # Harus ada koma untuk tuple dengan satu elemen

# Tuple dengan beberapa elemen
koordinat = (10, 20)
orang = ("Budi", 25, "Jakarta")

# Tanpa tanda kurung juga bisa
hari = "Senin", "Selasa", "Rabu", "Kamis", "Jumat"

# Tuple dengan fungsi tuple()
huruf = tuple("ABCD") # ('A', 'B', 'C', 'D')



####### Akses Element Tuple #######
hari = ("Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu")

# Mengakses dengan indeks
print(hari[0])      # Output: Senin
print(hari[-1])     # Output: Minggu

# Slicing
print(hari[1:4])    # Output: ('Selasa', 'Rabu', 'Kamis')
print(hari[::-1])   # Output: ('Minggu', 'Sabtu', 'Jumat', 'Kamis', 'Rabu', 'Selasa', 'Senin')


####### Operasi pada Tuple #######
# Tuple tidak dapat diubah setelah dibuat
hari = ("Senin", "Selasa", "Rabu")
# hari[0] = "Monday"  # Error: TypeError

# Tetapi kita bisa menggabungkan tuple
awal_minggu = ("Senin", "Selasa", "Rabu")
akhir_minggu = ("Kamis", "Jumat")
akhir_pekan = ("Sabtu", "Minggu")
seminggu = awal_minggu + akhir_minggu + akhir_pekan
print(seminggu)  # ('Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu')

# Mengulang tuple
pola = ("A", "B") * 3
print(pola)  # ('A', 'B', 'A', 'B', 'A', 'B')

# Fungsi umum untuk tuple
print(len(seminggu))         # Output: 7
print(min(awal_minggu))      # Output: Rabu (alfabet)
print("Jumat" in seminggu)   # Output: True

""" 
Unpacking Tuple
Satu keuntungan utama tuple adalah kemampuannya untuk "unpacking" (membongkar nilai).
 """
 
# Unpacking dasar
koordinat = (10, 20)
x, y = koordinat
print(f"x = {x}, y = {y}")  # Output: x = 10, y = 20

# Unpacking dengan banyak nilai
data_orang = ("Budi", 25, "Jakarta", "Programmer")
nama, umur, kota, pekerjaan = data_orang
print(f"{nama} berusia {umur} tahun, tinggal di {kota}, bekerja sebagai {pekerjaan}")

# Unpacking sebagian dengan *
daftar_belanja = ("Apel", "Roti", "Susu", "Telur", "Gula")
item_pertama, *item_tengah, item_terakhir = daftar_belanja
print(f"Item pertama: {item_pertama}")      # Output: Apel
print(f"Item tengah: {item_tengah}")        # Output: ['Roti', 'Susu', 'Telur']
print(f"Item terakhir: {item_terakhir}")    # Output: Gula

