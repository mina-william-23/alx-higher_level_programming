#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for key in list(a_dictionary.keys()):
        if a_dictionary[key] == value:
            del a_dictionary[key]
    return a_dictionary
# def complex_delete(a_dictionary, value):
#     for k, v in filter(lambda p: p[1] == value, list(a_dictionary.items())):
#             del a_dictionary[k]
#     return a_dictionary

# def complex_delete(a_dictionary, value):
# keys=map(lambda x:x[0] if x[1]==value else None, list(a_dictionary.items()))
# for k in keys:
#         if k is not None:
#             del a_dictionary[k]
#     return a_dictionary
