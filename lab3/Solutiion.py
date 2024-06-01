# Первое задание
def create_n_dim_array(n, size, level: int = None):
    if level is None:
        level = n

    if level == 1:
        return [f'level {n}'] * size

    return [create_n_dim_array(n, size, level - 1) for a in range(size)]

# Примеры использования
print(create_n_dim_array(3, 2))
print(create_n_dim_array(2, 3))

# Второе задание
def calculate_y_k(x, k):
    if x == 0:
        raise ValueError("x must not be zero")

    y = 1
    b = 1 / (2 * x)

    for i in range(1, k + 1):
        b = b * x**2
        y = b * y

    return y

x = 2
k = 3
print(f"y_{k} for x={x}: {calculate_y_k(x, k)}")

x = 3
k = 2
print(f"y_{k} for x={x}: {calculate_y_k(x, k)}")


