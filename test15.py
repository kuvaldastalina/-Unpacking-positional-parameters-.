def print_params(a=1, b='string', c=True):
    print(a, b, c)


print_params()
print_params(b=25)
print_params(c=[1, 2, 3])

value_list = [4, True, 'bools']
print_params(*value_list)
values_dict = {'a': 7, 'b': True, 'c': "short"}
print_params(**values_dict)
value_list_2 = ['chert', False]
print_params(*value_list_2, 42)