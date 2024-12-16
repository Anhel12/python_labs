from itertools import product

# Первое задание
letters = "ABCDE"
count = 0
for i in product(letters, repeat=5):
    if i[0] != "Е" and i[4] != "А":
        count += 1;
print("Кол-во слов:", count)
# Второе задание
print(str(bin(4 ** 511 + 2 ** 511 - 511)).count("1"))

# Третье задание
def smallest_prime_factors(n):
    spf = list(range(n + 1))  # Изначально каждый элемент сам себе делитель
    for i in range(2, int(n ** 0.5) + 1):
        if spf[i] == i:  # Если i — простое число
            for j in range(i * i, n + 1, i):
                spf[j] = min(spf[j], i)  # Обновляем наименьший простой делитель
    return spf

def calculate_M(N):
    spf = smallest_prime_factors(N)
    factors = sorted({spf[N]})
    return factors

results = [(N, calculate_M(N)) for N in range(200000002, 200000002 + 5)]

for N, M_N in results:
    print(f"N = {N}, M(N) = {M_N}")