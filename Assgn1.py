mul16=set()
for x in range(1,11):
  mul16.add(x*16)
print(mul16)
print(type(mul16))

mul12=set()
for x in range(1,11):
  mul12.add(x*12)
print(mul12)

mul16.remove(16)
mul12.remove(12)
print(mul16)
print(mul12)

print(mul12.intersection(mul16))
print(mul12.union(mul16))
print(mul12.difference(mul16))

mul12.update(mul16)
print(mul12)

mul12.clear()
mul16.clear()
print(mul12)
