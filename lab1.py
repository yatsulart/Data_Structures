from time import time

print('090301-ПОВа-о24 Яцула Артем Романович')

def test(N):
    if N == 0:
        return "NO"

    seen = [False] * N
    rem = 0
    start_time = time()

    for i in range(1, N + 1):
        rem = (rem * 10 + 1) % N
        if seen[rem]:
            end_time = time()
            print(f"Затрачено {end_time - start_time:.6f} секунд")
            return "NO"
        seen[rem] = True
        if rem == 0:
            end_time = time()
            print(f"Затраченое {end_time - start_time:.6f} секунд")
            return '1' * i

    end_time = time()
    print(f"Затрачено {end_time - start_time:.6f} секунд")
    return "NO"

N = int(input("Введите N: "))
print(test(N))
