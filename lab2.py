import numpy as np
import time
from scipy.linalg.blas import sgemm

size1 = 256
size2 = 2048

np.random.seed(90301)

def make(size):
    return np.random.rand(size, size).astype(np.float32)

a1 = make(size1)
b1 = make(size1)

a2 = make(size2)
b2 = make(size2)

ops1 = 2 * size1**3
ops2 = 2 * size2**3

def timer(f, *x):
    start = time.time()
    res = f(*x)
    end = time.time()
    t = end - start
    ops = ops1 if x[0].shape[0] == size1 else ops2
    mflops = ops / (t * 1e6)
    return res, t, mflops

def mul1(a, b):
    n = a.shape[0]
    c = np.zeros((n, n), dtype=np.float32)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                c[i, j] += a[i, k] * b[k, j]
    return c

print("Яцула Артем Романович, 090301-ПОВа-о24")
print("-" * 30)
print("Вариант 1: обычное умножение")
c1, t1, p1 = timer(mul1, a1, b1)
print(f"Время: {t1:.2f} сек")
print(f"MFLOPS: {p1:.2f}")
print("-" * 30)

def mul2(a, b):
    return sgemm(alpha=1.0, a=a, b=b)

print("Вариант 2: BLAS sgemm")
c2, t2, p2 = timer(mul2, a2, b2)
print(f"Время: {t2:.2f} сек")
print(f"MFLOPS: {p2:.2f}")
print("-" * 30)

def mul3(a, b):
    n = a.shape[0]
    c = np.zeros((n, n), dtype=np.float32)
    s = 128
    for i in range(0, n, s):
        for j in range(0, n, s):
            for k in range(0, n, s):
                c[i:i+s, j:j+s] += a[i:i+s, k:k+s] @ b[k:k+s, j:j+s]
    return c

print("Вариант 3: блочное умножение")
c3, t3, p3 = timer(mul3, a2, b2)
print(f"Время: {t3:.2f} сек")
print(f"MFLOPS: {p3:.2f}")
print("-" * 30)

print("Сравнение:")
print(f"Обычное: {p1:.2f} MFLOPS")
print(f"BLAS: {p2:.2f} MFLOPS")
print(f"Блочное: {p3:.2f} MFLOPS")
print(f"Блочное / BLAS: {p3/p2:.2f}")
