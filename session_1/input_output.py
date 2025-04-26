# input
print("\n================ Function ====================")

nama = input("Masukkan nama Anda: ")
print(f"Halo, {nama}!")

# Input numerik (konversi ke tipe data yang sesuai)
umur_str = input("Masukkan umur Anda: ")
umur = int(umur_str)
print(f"Tahun depan Anda akan berusia {umur + 1} tahun")

# Output
print("\n================ Function ====================")


# Print sederhana
print("Hello, world!")

# Print dengan format
nama = "Alenna"
umur = 20
print(f"{nama} berusia {umur} tahun")  # f-string (Python 3.6+)
print("{} berusia {} tahun".format(nama, umur))  # format() method
print("%s berusia %d tahun" % (nama, umur))  # format string lama

# Print dengan parameter tambahan
print("Apel", "Mangga", "Jeruk", sep=" - ")  # Menggunakan separator
print("Baris 1", end=" >>> ")  # Mengubah ending (default adalah new line)
print("Masih di baris yang sama")


# Menulis ke file
with open("contoh.txt", "w") as file:
    file.write("Ini adalah baris pertama.\n")
    file.write("Ini adalah baris kedua.")

# Membaca dari file
with open("contoh.txt", "r") as file:
    isi = file.read()
    print(isi)
    
# "a"	Append: Menambahkan teks di akhir file (tanpa menghapus isi lama).
# "r+"	Read + Write: Baca dan tulis (file harus sudah ada).
# "w+"	Write + Read: Hapus isi lama, lalu baca/tulis.
# "a+"	Append + Read: Tambah teks di akhir + baca.