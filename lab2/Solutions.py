# Первое задание
letters = ['A', 'B', 'C', 'D', 'E']
all_words = itertools.product(letters, repeat=5)

filtered_words = filter(lambda word: word[0] != 'E' and word[-1] != 'A', all_words)
count = len(list(filtered_words))

print("Кол-во слов:", count)
# Второе задание
print(str(bin(4 ** 511 + 2 ** 511 - 511)).count("1"))

# Третье задание
