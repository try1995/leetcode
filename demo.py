a = 1
print(id(a))
a = 2
print((id(a)))

b = [1, 2 ,3]
print((id(b)))
b[0] = 4
print(b)
print((id(b)))

c = "123"
print((id(c)))
c = "124"
print(id(c))

d = (1, 2)
e = set()