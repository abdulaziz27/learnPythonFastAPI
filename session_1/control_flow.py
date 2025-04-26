# If-Else Conditional Statements
# Digunakan untuk mengeksekusi kode berdasarkan kondisi tertentu.

print("\n================ If-Else Conditional Statements ====================")

nilai = 20

if nilai >= 80:
    print("Your Score A")
elif nilai >= 70:
    print("Your Score B")
elif nilai >= 50:
    print("Your Score C")
else:
    print("Not Passed")
    

# Looping Statements
# Digunakan untuk iterasi melalui urutan (seperti list, tuple, string).

print("\n================ Looping Statements====================")

# For Loop
for i in range(0, 3):
    print(i)
    
    
# Perulangan melalui rentang angka
for i in range(3):  # 0, 1, 2
    print(i, end=" ")  # Output: 0 1 2 

print()

# Perulangan melalui list
buah = ["apel", "jeruk", "mangga"]
for i in buah:
    print(i, end=" ")  # Output: apel jeruk mangga
print()

# Perulangan dengan enumerate (get index dan value)
for index, value in enumerate(buah, start=1):
    print (f"Index: {index}, Value: {value}", end=" ")  # Output: Index: 1, Value: apel Index: 2, Value: jeruk Index: 3, Value: mangga
print()

# While Loop
# Digunakan untuk mengeksekusi kode selama kondisi tertentu benar.
print("\n================ While ====================")

# hitung maju dari 5
hitungan = 5

while hitungan <= 10:
    print(hitungan, end=" ")  # Output: 5 6 7 8 9 10
    hitungan += 1
print() 


# Hitung mundur dari 5
n = 5

while n >= 0:
    print(n, end=" ")    # Output: 5 4 3 2 1 0
    n -= 1
print()

# Break and Continue Statement
print("\n================ Break and Continue ====================")

# break: Keluar dari perulangan
# continue: Lanjut ke iterasi berikutnya

print("\n Contoh break:")
for i in range (10):
    if i == 5:
        break # Keluar dari loop saat i = 5
    print(i, end=" ") 
    

print("\n Contoh continue:")
for i in range(10):
    if i % 2 == 0:
        continue    # lewati angka genap 
    print(i, end=" ")
print()

