# Первое задание
def create_n_dim_array_recursive(n, size, level=1):
    if n == 1:
        return [f"level {level} "] * size
    return [create_n_dim_array_recursive(n-1, size, level+1) for _ in range(size)]


def create_n_dim_array_iterative(n, size):
    array = [f"level {n}"] * size
    counter_dep = 0
    counter_lev = 0
    for level in range(n-2):
        print("\t" * counter_dep, "[ ")
        counter_dep += 1

    for i in range(size if size - n < 0 else 1):
        print("\t" * counter_dep, "[ ")
        counter_dep += 1
        for j in range(size):
            print("\t" * counter_dep, end = "")
    # print([array.copy() for _ in range(size)])
            print(array)
        counter_dep -= 1
        print("\t" * counter_dep, "] ")
    # print("]")
    # print(array)
    for level in range(n-2):
        counter_dep -= 1
        print("\t" * counter_dep, "] ")

# Второе задание
def calculate_recursive(k, x, y=1, b=None):
    if b is None:
        b = 1 / (2 * x)
    if k == 0:
        return y
    b_k = b - x**2
    return calculate_recursive(k - 1, x, y * b_k, b_k)


def calculate_iterative(k, x):
    y = 1
    b = 1 / (2 * x)
    for _ in range(k):
        b -= x**2
        y *= b
    return y


print(create_n_dim_array_recursive(2, 3))
create_n_dim_array_iterative(2, 4)

x = 2  # Пример значения
k = 5  # Число шагов
print(calculate_recursive(k, x))
print(calculate_iterative(k, x))
