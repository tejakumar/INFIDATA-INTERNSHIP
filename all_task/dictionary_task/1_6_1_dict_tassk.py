def delete_keys_from_dict(dictionary, keys_to_delete):
    for key in keys_to_delete:
        dictionary.pop(key, None)
a = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
keys_to_delete = ['b', 'd']
print('Original dictionary:', a)
delete_keys_from_dict(a, keys_to_delete)
print('Dictionary after deleting keys:', a)