def print_params(a=1, b='строка', c=True):
    print(f'a: {a}, b: {b}, c: {c}')

print_params()
print_params(b=25)
print_params(c=[1, 2, 3])
print_params(10, 'Новая строка')

values_list = [3.14, 'пример', False]
values_dict = {'a': 42, 'b': 'тест', 'c': None}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [5.5, 'другой пример']
print_params(*values_list_2, 42)
