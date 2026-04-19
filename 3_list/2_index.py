list1 = ['apple', 'HTML', 23, 56, 'Y', 34.44]
print(list1)

list1.append('help')
print(list1)

list1.insert(2,'help')
print(list1)

list1.pop()
print(list1)

list1.append('help')
print(list1)


list1.remove('help')
print(list1)

print(list1.count('HTML'))

print(len(list1))


list2 = list1.copy()
print(list2)

list2 = list1.clear()
print(list2)


