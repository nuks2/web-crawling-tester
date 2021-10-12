s = 'show how to index into sequences'.split()

# list indexing
print(s)
print(s[0])
print(s[5])
print(s[-1])
print(s[-2])
print(s[-6])

# list slice
print(s[1:4])
print(s[1:-1])
print(s[:3])
print(s[3:])
print(s[:3] + s[3:] == s)

full_slice = s[:]
print(full_slice)
print(full_slice == s)
print(full_slice is s)

u = s.copy()
v = list(s)
print(u)
print(v)

print(s[::2])
print(s[::-1])