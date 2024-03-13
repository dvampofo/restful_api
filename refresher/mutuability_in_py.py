a = 8500
b = 8500

print(id(a))
print(id(b))

a = 8322

print(id(a))
print(id(b))

# ----------------

a1 = "hello"
b1 = a

print(id(a1))
print(id(b1))

a1 += " world"
print(a1)