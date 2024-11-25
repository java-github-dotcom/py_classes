## Lists
# 1
lst.count(2)
# 2
sum(lst)
# 3
max(lst)
# 4
min(lst)
# 5
print(True if 1 in lst else False)
# 6 
lst[0]
# 7 
lst[-1]
# 8 
lst[:3]
# 9
mask = []
for i in range(len(lst)):
    mask.append(lst[-(i+1)])
mask
# 10
mask = sorted(lst)
# 11
set(lst)
# 12 
new_element = 5
lst.append(new_element)
# 13 
lst.index(5)
# 14 
print(True if lst == [] else False)
# 15 
mask = 0
for i in lst:
    if i // 2 == 0:
        mask += lst.count(i)
mask
# 16 
mask = 0
for i in lst:
    if i // 2 != 0:
        mask += lst.count(i)
mask
# 17
lst1 = [1, 2, 3]
lst2 = [4, 5, 6]
lst1.extend(lst2)
lst1
# 18
lst1 = [1, 2, 3]
lst2 = [4, 5, 6]
lst1.append(lst2)
print(True if lst2 in lst1 else False)
# 19
lst1 = [1, 2, 3]
n = 2
replace_with = 7
lst1[lst1.index(n)] = replace_with
lst1
# 20 
lst1 = [1, 2, 3]
print(sorted(lst1, reverse=True)[1])
# 21
lst1 = [1, 2, 3]
print(sorted(lst1)[1])
# 22
mask = []
for i in lst1:
    if i % 2 == 0:
        mask.append(i)
    else:
        pass
mask
# 23 
mask = []
for i in lst1:
    if i % 2 != 0:
        mask.append(i)
    else:
        pass
mask
# 24 
print(len(lst1))
# 25 
lst1_copy = []
lst1_copy.extend(lst1)
lst1_copy
# 26 
lst1[int(len(lst1)/2)]
# 27 
max(lst1[sublist_index])
# 28 
min(lst1[sublist_index])
# 29
try:
    lst.pop(element_index)
except IndexError:
    pass
# 30 
print(True if lst1 == sorted(lst1) else False)
# 31
n = 2
mask = []
for i in lst1:
    for k in range(n):
        mask.append(i)
mask
# 32
mask = []
lst1 = [1, 2, 3]
lst2 = [4, 5, 6]
mask.extend(lst1)
mask.extend(lst2)
sorted(mask)
# 33
lst
n = 2
for i in range(len(lst)):
    if lst[i] == n:
        print(i, end=' ')
# 34
rotated_list = []
for i in range(1, len(lst)+1):
    rotated_list.append(lst[-i])
rotated_list
# 35 
range_list = []
for i in range(1,10):
    range_list.append(i)
range_list
# 36
lst = [-1, 2, 7, 3, -6, 4, 8, -5]
sum_of_positive_n = 0
for i in lst:
    if i > 0:
        sum_of_positive_n+=i
sum_of_positive_n
# 37
lst = [-1, 2, 7, 3, -6, 4, 8, -5]
sum_of_negative_n = 0
for i in lst:
    if i < 0:
        sum_of_negative_n+=i
sum_of_negative_n
# 38
palindrome_list = [3, 2, 1, 2, 3]
try:
    for i in range(len(palindrome_list)-1):
        if palindrome_list[i] == palindrome_list[-(i+1)]:
            continue
        else:
            print(False)
            break
finally:
    print(True)
# 39
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# 40
mask = []
for i in palindrome_list:
    if palindrome_list.count(i) == 1:
        mask.append(i)
mask

## Tuple
# 1
tuple.count(element)
# 2 
max(tuple)
# 3
min(tuple)
# 4 
print(True if element in tuple else False)
# 5
if tuple == ():
    print('This tuple is empty')
else:
    print(tuple[0])
# 6
if tuple == ():
    print('This tuple is empty')
else:
    print(tuple[-1])
# 7
len(tuple)
# 8 
tuple[:3]
# 9 
tple = tuple1 + tuple2
# 10
print(True if tuple == () else False)
# 11
n = element
for i in range(len(lst)):
    if lst[i] == n:
        print(i, end=' ')
# or
def get_all_indices(tuple, element):
    return [index for index, value in enumerate(tuple) if value == element]
# 12 
sorted(tuple, reverse=True)[1]
# 13 
sorted(tuple)[1]
# 14
single_element_tuple = (1)
# 15
tuple(list)
# 16
print(True if tuple == sorted(tuple) else False)
# 17
max(tuple[subtuple_index])
# 18
min(tuple[subtuple_index])
# 19
# 'tuple' object does not support item assignment
# the original tuple cannot be changed
# 20 
tpl = ((1, 2, 3), (4, 5, 6))
# 21 
tpl = (1, 2, 3)
number = 2
tpl1 = []
for v in tuple:
    for i in range(number):
        tpl1.append(v)
tpl1 = tuple(tpl1)
# 22
tpl1 = []
for i in range(number):
    tpl1.append(i)
tpl1 = tuple(tpl1)
# 23 
tpl = tpl(sorted(tpl, reverse=True))
# 24
try:
    for i in range(len(tuple)-1):
        if palindrome_list[i] == palindrome_list[-(i+1)]:
            continue
        else:
            print(False)
            break
finally:
    print(True)
# 25 
tpl = tpl(list(tpl).extend(new_values))

## Set
# 1
set.count(element)
# 2 
max(set)
# 3
min(set)
# 4 
print(True if element in set else False)
# 5
if set == set():
    print('This set is empty')
else:
    print(list(set)[0])
# 6
if set == set():
    print('This set is empty')
else:
    print(list(set)[-1])
# 7
len(set)
# 8 
list(set)[:3]
# 9
set1 = set2.union(set3)
# 10
set1 = set2.intersection(set3)
# 11
set1 = set2.difference(set3)
# 12
set1 = set2.symmetric_difference(set3)
# 13
set1.add(element)
# 14
set1.remove(element)
# 15
print(True if element in set1 else False)
# 16
set1.clear()
# 17
print(True if set1 == set() else False)
# 18
new_element = 5
set1.add(new_element)
# 19
set1.discard(new_element)
# 20
set1.pop()
# 21 
lst = [1,3,3,2,1,2,3,2,1]
st = set(lst)
lst = list(st)
# 22
st = set()
lst = [x for x in lst if not (x in st or st.add(x))]
# 23
def create_nested_sets(elements, group_size):
    nested_sets = set()
    for i in range(0, len(elements), group_size):
        subset = frozenset(elements[i:i + group_size])
        nested_sets.add(subset)
    return nested_sets
# 24
len(set(lst))
# 25
import random

def generate_random_set(count):
    random_set = set()
    while len(random_set) < count:
        random_set.add(random.randint(0, 100))  # Adjust the range if needed
    return random_set

## Dictionaries
# 1
dict.get(key)
# 2
dict[key]
# 3
dict.keys()
# 4
dict.values()
# 5
dict.items()
# 6
dict.update({key: value})
# 7
del dict[key]
# 8
dict.pop(key)
# 9
dict.clear()
# 10
dict.copy()
# 11
len(dict)
# 12
dict.setdefault(key, default_value)
# 13
key in dict
# 14
key not in dict
# 15
sorted(dict.items(), key=lambda x: x[1])
# 16
dict1 = dict2.copy()
# 17
dict1 = {key: value for key, value in dict2.items()}
# 18
dict1 = {key: value for key, value in dict2.items() if value % 2 == 0}
# 19
dict1 = {key: value for key, value in dict2.items() if value % 2 != 0}
# 20
max(dict, key=lambda x: dict[x])
# 21
min(dict, key=lambda x: dict[x])
# 22
dict1 = dict2 | dict3
# 23
dict1 = {**dict2, **dict3}
# 24
dict1 = {key: dict2.get(key, default_value) for key in dict2}
# 25
dict1.update({key: new_value for key, new_value in new_dict.items() if key in dict1})
