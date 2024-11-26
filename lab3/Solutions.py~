# Первое задание
def create_n_dim_array(n, size, level = None):
    if level is None:
        level = n

    if level == 1:
        return [f'level {n}'] * size

    return [create_n_dim_array(n, size, level - 1) for a in range(size)]

def create_n_dim_array2(n, size):
    result = [f'level {n}'] * size
    for _ in range(n - 1):
        new_result = []
        for _ in range(size):
            new_result.append(result)
        result = new_result
    return result
# Примеры использования
print(create_n_dim_array(3, 2))
print(create_n_dim_array(2, 3))

print(create_n_dim_array2(3, 2))
print(create_n_dim_array2(2, 3))

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

def calculate_y_k2(x, k, b = None):
    if x == 0:
        raise ValueError("x must not be zero")

    if k == 0:
        return 1

    if b is None:
        b = 1 / (2 * x)

    return b * x**2 * calculate_y_k(x, k - 1, b * x**2)


x = 2
k = 3
print(f"y={k} for x={x}: {calculate_y_k(x, k)}")
print(f"y={k} for x={x}: {calculate_y_k2(x, k)}")

x = 3
k = 2
print(f"y={k} for x={x}: {calculate_y_k(x, k)}")
print(f"y={k} for x={x}: {calculate_y_k2(x, k)}")