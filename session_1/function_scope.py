# Function
print("\n================ Function ====================")

# Fungsi adalah blok kode yang dapat digunakan kembali. Fungsi didefinisikan dengan kata kunci def

# basic func wihout parameter
def greeting():
    print("Hai")
    
greeting()

# func with parameter
def greeting(name):
    print(f"Hai, {name}. Welcome to my page!")
    
greeting("abdul")


# with return value
def total(a, b):
    return a+b

result = total(5, 10)

print(f"5 + 10 = {result}")

# with default parameter

def defaultGreeting(name, domicile="Purwokerto"):
    print(f"Hai, I'am {name} from {domicile}")
    
defaultGreeting("Alenna")
defaultGreeting("Aziz", "Bogor")

# Scope
print("\n================ Scope ====================")
# Variabel di Python memiliki berbagai lingkup (scope) yang menentukan di mana variabel tersebut dapat diakses.

# Variabel global
x = 10

def fungsi_1():
    # Variabel lokal
    y = 5
    print(f"Di dalam fungsi_1: x = {x}, y = {y}")

def fungsi_2():
    # Variabel lokal dengan nama yang sama dengan variabel global
    x = 20
    print(f"Di dalam fungsi_2: x = {x}")

def fungsi_3():
    # Menggunakan keyword 'global' untuk mengubah variabel global
    global x
    x = 30
    print(f"Di dalam fungsi_3: x = {x}")

print(f"Sebelum memanggil fungsi: x = {x}")  # Output: x = 10
fungsi_1()  # Output: x = 10, y = 5
print(f"Setelah fungsi_1: x = {x}")  # Output: x = 10
fungsi_2()  # Output: x = 20
print(f"Setelah fungsi_2: x = {x}")  # Output: x = 10 (tidak berubah)
fungsi_3()  # Output: x = 30
print(f"Setelah fungsi_3: x = {x}")  # Output: x = 30 (berubah)


