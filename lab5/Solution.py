from typing import List, Union, Generator
from functools import reduce

# Генератор для объединения последовательностей по заданной стратегии
def merge_sequences(sequences: List[Union[str, int, float, list]]) -> Generator:
    str_result = ""
    num_result = 0
    list_result = []

    for item in sequences:
        if isinstance(item, str):
            str_result += item + ' '
        elif isinstance(item, (int, float)):
            num_result += item
        elif isinstance(item, list):
            list_result.extend(item)
        else:
            raise TypeError(f"Unsupported data type: {type(item)}")

    if str_result:
        yield str_result.strip()
    if num_result:
        yield num_result
    if list_result:
        yield list_result

# Исходные данные
sequences = [1, 2, 3, "hi", "hello", "world", 4.5]

# Преобразование чисел в их квадраты с помощью map
squared_sequences = list(map(lambda x: x ** 2 if isinstance(x, (int, float)) else x, sequences))

# Суммирование числовых значений с помощью reduce
sum_of_numbers = reduce(lambda acc, x: acc + x if isinstance(x, (int, float)) else acc, sequences, 0)

# Отфильтровывание строк короче 4 символов с помощью filter
filtered_sequences = list(filter(lambda x: not isinstance(x, str) or len(x) >= 4, sequences))


print("Squared sequences:", squared_sequences)
print("Sum of numbers:", sum_of_numbers)
print("Filtered sequences:", filtered_sequences)

print("\nMerged squared sequences:")
print(list(merge_sequences(squared_sequences)))

print("\nMerged filtered sequences:")
print(list(merge_sequences(filtered_sequences)))

