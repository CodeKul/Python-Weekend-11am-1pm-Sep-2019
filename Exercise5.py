# Write a function to rmeove numbers from the given list
# E.g. - list = [13, 'ABC', True, 45, 34, 'Red', 'Green', 'Five', 5, 'Six']
# Output: ['ABC', True, 'Red', 'Green', 'Five', 'Six']

def remove_numbers_from_list(l):
    i = 0
    # l = ['A', 'B', 'C', 1, 3, 5, 7]
    length = len(l)
    while i < length:
        if isinstance(l[i], int):
            l.remove(l[i])
            length -= 1
        else:
            i += 1
    return l


list1 = [13, 'ABC', 'True', 45, 34, 'Red', 'Green', 'Five', 5, 'Six', 12.45]
list2 = remove_numbers_from_list(list1)
print(list1)
print(list2)

# a = True
# b = True

# print(a)
# print(b)
# res = a + b
# print(res)