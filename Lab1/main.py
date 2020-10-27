import numpy as np

a = np.zeros(10)
print(a)

b = np.array([5, 5, 5, 5, 5, 5, 5, 5, 5, 5])
print(b)

c = np.arange(10, 51, 1)
print(c)

d = np.arange(0, 9, 1).reshape((3, 3))
print(d)

e = np.eye(3)
print(e)

f = np.random.random((5, 5))
print(f)

g = np.arange(0.01, 1.01, 0.01).reshape((10, 10))
print(g)

h = np.linspace(0, 1, 20)
print(h)

i = np.random.randint(1, 25, 25).reshape((5, 5))
print(i)

print(i.sum())

print(i.mean())

print(i.std())

kMatrix = i.cumsum(0)

k = kMatrix[4, :]

print(k)

l = np.random.randint(0, 100, 25).reshape((5, 5))

print(l)

m = np.median(l)

print(m)

n = np.min(l)

print(n)

o = np.max(l)

print(o)

p = np.random.randint(0, 100, 18).reshape((3, 6))

print(p)

q = np.transpose(p)

print(q)

r = np.random.randint(0, 100, 16).reshape((4, 4))
s = np.random.randint(0, 100, 16).reshape((4, 4))

print(r)
print(s)
print(np.add(r, s))

t = np.random.randint(0, 100, 12).reshape((3, 4))
u = np.random.randint(0, 100, 12).reshape((4, 3))

print(np.multiply(t, 2))

print(np.matmul(t, u))
