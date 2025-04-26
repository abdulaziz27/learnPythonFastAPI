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




