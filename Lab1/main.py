import numpy as np

a = np.zeros(10)
print(a)
print(" ")

b = np.array([5, 5, 5, 5, 5, 5, 5, 5, 5, 5])
print(b)
print(" ")

c = np.arange(10, 51, 1)
print(c)
print(" ")

d = np.arange(0, 9, 1).reshape((3, 3))
print(d)
print(" ")

e = np.eye(3)
print(e)
print(" ")

f = np.random.random((5, 5))
print(f)
print(" ")

g = np.arange(0.01, 1.01, 0.01).reshape((10, 10))
print(g)
print(" ")

h = np.linspace(0, 1, 20)
print(h)
print(" ")

i = np.random.randint(1, 25, 25).reshape((5, 5))
print(i)
print(" ")

print(i.sum())
print(" ")

print(i.mean())
print(" ")

print(i.std())
print(" ")

kMatrix = i.cumsum(0)

k = kMatrix[4, :]

print(k)
print(" ")

l = np.random.randint(0, 100, 25).reshape((5, 5))

print(l)
print(" ")

m = np.median(l)

print(m)
print(" ")

n = np.min(l)

print(n)
print(" ")

o = np.max(l)

print(o)
print(" ")

p = np.random.randint(0, 100, 18).reshape((3, 6))

print(p)
print(" ")

q = np.transpose(p)

print(q)
print(" ")

r = np.random.randint(0, 100, 16).reshape((4, 4))
s = np.random.randint(0, 100, 16).reshape((4, 4))

print(r)
print(" ")

print(s)
print(" ")

print(np.add(r, s))
print(" ")

t = np.random.randint(0, 100, 12).reshape((3, 4))
u = np.random.randint(0, 100, 12).reshape((4, 3))

print(np.multiply(t, 2))
print(" ")

print(np.matmul(t, u))
