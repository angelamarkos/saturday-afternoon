import copy
a = 1
b = a = 2
print(a)
print(b)

b = 4
print(a)
print(b)
list_1 = [1, 3, 5]
# list_2 = list_1[:]
list_2 = list_1.copy()
# list_2 = copy.copy(list_1)
print(list_1)
print(list_2)

list_2[1] = 0

print(list_1)
print(list_2)

list_1 = [1, 3, [1, 2]]
list_2 = copy.deepcopy(list_1)

print(list_1)
print(list_2)

list_2[2][0] = 0

print(list_1)
print(list_2)

class Template:
    def __init__(self, first_element: int, last_element: int, elements: list, private_elements: list):
        self.first_element = first_element
        self.last_element = last_element
        self.elements = elements
        self.__private_elements = private_elements

    def __str__(self):
        return f'{self.first_element} - {self.last_element}, {self.elements}, {self.__private_elements}'

    def __copy__(self):
        private_prefix = f'_{self.__class__.__name__}'
        copy_dict = {}
        for k, v in self.__dict__.items():
            if private_prefix in k:
                continue
            copy_dict[k] = v

        return Template(private_elements=[], **copy_dict)

    def __deepcopy__(self, memo={}):
        private_prefix = f'_{self.__class__.__name__}__'
        copy_dict = {}
        for k, v in self.__dict__.items():
            if private_prefix in k:
                k = k.split(private_prefix)[-1]
            copy_dict[k] = copy.deepcopy(v)

        return Template(**copy_dict)

    def clone(self, **kwargs):
        private_prefix = f'_{self.__class__.__name__}__'
        new_temp = self.__deepcopy__()
        for k, v in kwargs.items():
            if new_temp.__dict__.get(private_prefix + k):
                del kwargs[k]
                k = private_prefix + k
                kwargs[k] = v
        new_temp.__dict__.update(**kwargs)

        return new_temp

class CloneManager:
    """ data_dict : {instance1: [kwargs1, kwargs2, ..., kwargs3], instance2: [kwargs21, kwargs22, ..]}"""
    def __init__(self, data_dict={}):
        self.data_dict = data_dict

    def add_clone_info(self, instance, **kwargs):
        pass

    def clone_instances(self):
        for instance, kwargs_list in self.data_dict.items():
            for kwargs in kwargs_list:
                yield instance.clone(**kwargs)



temp = Template(1, 2, [1, 2, [3, 5]], [1, 2, [2, [2]]])
temp_clone = temp.clone(private_elements=[1, 2, 4])

clone_manager = CloneManager({temp: [{'first_element': 10, 'private_elements': [1, 2]},
                                     {'last_element': 45}]})


for temp_cl in clone_manager.clone_instances():
    print(temp_cl)


# temp_1 = temp
# temp_copy = copy.copy(temp)
# print(temp_copy)
# temp_deepcopy = copy.deepcopy(temp)
# print(temp_deepcopy)
# print(temp)
# print(temp_1)
# print(temp_copy)
# print(temp_deepcopy)
#
# temp.first_element = 1
# temp.elements[1] = 0
# temp.last_element = 3
# temp.elements[2][0] = 0
# print('Assigned')
# print(temp_1)
#
# print('Copy')
# print(temp_copy)
# print('Deepcopy')
# print(temp_deepcopy)
# print(temp)
#
#
