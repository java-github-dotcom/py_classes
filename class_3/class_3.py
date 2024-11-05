## List Tasks
lst = [1,2,3,2,1,2,3,1,2,3]
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
tuple = tuple1 + tuple2
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










