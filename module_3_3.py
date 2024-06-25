def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(3, 5 , 6)
print_params(1, 4)
print_params(b = 25)
print_params(c = [1,2,3])
    #Работают

values_list = [1, True, 'str']
values_dict = {'a' : 1, 'b' : 'str', 'c' : True}
values_list_2 = ['str', 5]

print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 42)