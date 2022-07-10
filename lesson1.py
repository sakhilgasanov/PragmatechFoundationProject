"""soz='kitab'

print(soz.lstrip('k'))

print(soz.rstrip('b'))

print(soz.index('t'))

print(soz[2])

print(soz[-1])

print(soz[1:3])

print(soz[1:4:2])

print(soz.replace('k', 'h'))

print(soz.find('i'))

print(soz[-3])"""


"""l=['car', 'phone', 'name', 'surname', 'city']

#print(l, type(l))

#print(l[0])

l.append('Baku')

l.insert(2, 'sahil')

l.append([24, 1998])

#print(l[-1][0])

l.extend([15,23])

del l[-3]

l.remove('phone')

s=l.pop(-2)

print(l.count('sahil'))

print(l.count('amil'))

print(l)
print(s)"""


s1={2, 3, 4, 5}
s2={4, 5, 6, 7}

print(s1.intersection(s2))

print(s1.union(s2))

print(s1.difference(s2))

print(s2.difference(s1))

print(s1-s2)