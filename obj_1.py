def introspection_info(obj):
    info = {}

    info['type'] = type(obj)

    info['attributes'] = [attr for attr in dir(obj) if not attr.startswith('__')]

    info['methods'] = [method for method in dir(obj)
                       if callable(getattr(obj, method)) and not method.startswith('__')]

    info['module'] = getattr(obj, '__module__', None)

    if isinstance(obj, str):
        info['length'] = len(obj)
    elif isinstance(obj, list):
        info['length'] = len(obj)
    elif isinstance(obj, dict):
        info['length'] = len(obj)
        info['keys'] = list(obj.keys())

    return info

class MyClass:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f'Привет, {self.name}!')

my_obj = MyClass('Kirill')
my_list = [1, 2, 3]
my_dict = {'name': 'Kirill', 'age': 30}

print(introspection_info(my_obj))
print(introspection_info(my_list))
print(introspection_info(my_dict))

number_info = introspection_info(42)
print(number_info)