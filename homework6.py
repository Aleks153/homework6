my_dict = {'one': 10, 'two': 20, 'three': 30, 'four': 40}
print('Dict: ', my_dict)
print('Existing value: ', my_dict['two'])
print('Not existing value: ', my_dict.get('twelve'))
my_dict.update({'six': 60,
'seven': 70})
x = my_dict.pop('three')
print('Deleted value: ', x)
print('Modified dictionary: ', my_dict)
print()

my_set = {'Car', 'car', 456, (123,456,789), 45.2, 456}
print('Set: ', my_set)
my_set.add(753)
my_set.add((1,5,3))
my_set.discard('MORE')
my_set.remove('car')
print('Modified set: ', my_set)


