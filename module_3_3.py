def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

values_list = [2, False, 'Hello']
values_dict = {'a': 'Urban', 'b': 2, 'c': 'world'}
values_list_2 = [21, 'Title']

print_params()
print_params(b = 25)
print_params(c = [1,2,3])
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 42)