# Первое задание
def outer(hp):
    def inner(dam):
        nonlocal hp
        hp += dam
        if hp > 100:
            hp = 100
        elif hp < 0:
            hp = 0
        return hp
    return inner

result = outer(100)

print(result(-40))
print(result(20))

# Второе задание
import sys
import io
import functools
def set0(fun):
    def wrapper(*args, **kwargs):
        save_stdout = sys.stdout
        sys.stdout = io.StringIO()

        try:
            result = fun(*args, **kwargs)
        finally:
            sys.stdout = save_stdout
    return wrapper

@set0
def helloWorld():
    print("Hello World")

helloWorld()