# Первое задание
def create_n_dim_array_recursive(n, size, level=1):
    if n == 1:
        return [f"level {level}"] * size
    return [create_n_dim_array_recursive(n-1, size, level+1) for _ in range(size)]

def create_n_dim_array_iterative(n, size):
    array = [f"level {n}"] * size
    for level in range(n-1, 0, -1):
        array = [array.copy() for _ in range(size)]
    return array

# Второе задание
def calculate_recursive(k, x, y_prev=1, b_prev=None):
    if b_prev is None:
        b_prev = 1 / (2 * x)
    if k == 0:
        return y_prev
    b_k = b_prev - x**2
    return calculate_recursive(k - 1, x, y_prev * b_k, b_k)


def calculate_iterative(k, x):
    y = 1
    b = 1 / (2 * x)
    for _ in range(k):
        b -= x**2
        y *= b
    return y


print(create_n_dim_array_recursive(2, 3))
print(create_n_dim_array_iterative(2, 3))

x = 2  # Пример значения
k = 5  # Число шагов
print(calculate_recursive(k, x))
print(calculate_iterative(k, x))
