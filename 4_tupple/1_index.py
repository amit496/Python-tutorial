a = (1, 2,3,)
print(type(a))

a = (1)
print(type(a))

a = (1,)
print(type(a))

a = (12, "Hello", "34", 'true', True)
print(a)

a = (12, "Hello", "34", "343.44", 45.5, 'true', True, 34)
print(type(a[1]))
print(type(a[2]))
print(type(a[3]))
print(type(a[4]))
print(type(a[5]))
print(type(a[6]))
print(a[1])

# a[1] = "Hi"
# print(a)

print(a.count("34"))


print(a.index("343.44"))



