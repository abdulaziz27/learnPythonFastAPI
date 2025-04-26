""" Sets (Himpunan)
Set adalah kumpulan item unik dan tidak berurutan. Set sangat berguna untuk menghilangkan duplikasi dan operasi
matematika seperti irisan, gabungan, dan selisih.

"""
####### Membuat Set #######

# Set kosong
set_kosong = set()  # Tidak bisa menggunakan {}, karena itu dictionary kosong

# Set dengan elemen
buah = {"apel", "jeruk", "mangga", "apel"}  # Duplikat akan dihapus otomatis
print(buah)  # Output: {'mangga', 'apel', 'jeruk'} (urutan tidak menentu)

# Set dari iterable lain
huruf = set("mississippi")  # {'s', 'p', 'i', 'm'}
angka = set([1, 2, 2, 3, 3, 3, 4])  # {1, 2, 3, 4}


####### Operasi Dasar Set #######
warna = {"merah", "kuning", "hijau"}

# Menambah elemen
warna.add("biru")
print(warna)  # {'kuning', 'merah', 'hijau', 'biru'}

# Menambah beberapa elemen
warna.update(["ungu", "jingga"])
print(warna)  # {'ungu', 'jingga', 'merah', 'kuning', 'biru', 'hijau'}

# Menghapus elemen
warna.remove("kuning")  # Error jika elemen tidak ada
warna.discard("coklat")  # Tidak error jika elemen tidak ada
item = warna.pop()  # Menghapus dan mengembalikan elemen acak

# Membersihkan set
warna.clear()  # set kosong

####### Math Operations #######
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# Gabungan (Union)
print(A | B)         # {1, 2, 3, 4, 5, 6, 7, 8}
print(A.union(B))    # Sama dengan di atas

# Irisan (Intersection)
print(A & B)         # {4, 5}
print(A.intersection(B))  # Sama dengan di atas

# Selisih (Difference)
print(A - B)         # {1, 2, 3}
print(A.difference(B))  # Sama dengan di atas

# Selisih Simetris (Symmetric Difference)
print(A ^ B)         # {1, 2, 3, 6, 7, 8}
print(A.symmetric_difference(B))  # Sama dengan di atas

# Subset dan Superset
C = {1, 2}
print(C.issubset(A))      # Output: True (C ⊆ A)
print(A.issuperset(C))    # Output: True (A ⊇ C)


####### Operasi Lainnya #######

# Mengecek disjoint (tidak ada elemen yang sama)
X = {1, 2, 3}
Y = {4, 5, 6}
print(X.isdisjoint(Y))  # Output: True

# Membuat salinan set
Z = X.copy()

""" 
Frozen Set
Frozen set adalah versi set yang tidak dapat diubah (immutable).
"""

fs = frozenset([1, 2, 3, 4])
# fs.add(5)  # Error: AttributeError (frozen set tidak bisa diubah)

# Bisa digunakan sebagai kunci dictionary
preferences = {
    frozenset(["apel", "pisang"]): "buah",
    frozenset(["wortel", "bayam"]): "sayur"
}