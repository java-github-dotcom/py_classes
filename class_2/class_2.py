# Number Data Type
# 1
def round_float(f=float):
    return round(f, 2)
# 2
def l_and_s():
    nums = []
    nums.append(int(input('First number: ')))
    nums.append(int(input('Second number: ')))
    nums.append(int(input('Third number: ')))
    nums = sorted(nums)
    return f'''The largest number: {nums[-1]}
    The smallest number: {nums[0]}'''
# 3
def convert_km(n):
    return f'{n} km = {n*1**3} m = {n*1**6} cm'
# 4
def division(n=int, m=int):
    return f'The result of division of {n} by {m} is {int(n/m)} and the remainder is {n//m}'
# 5
def convert_cel_to_far():
    c = int(input('Enter a temperature in degrees C: '))
    f = c*(9/5)+32
    print(f'{c} degrees in C = {round(f, 2)} degrees in F')
# 6 
def last_digit(n):
    return int(list(str(n))[-1])
# 7
def odd_even(n):
    if n//2 == 0:
        return 'Even'
    else:
        return 'Odd'
# 8
def swap_values(k, l):
    i = k
    k = l
    l = i
    return 'Done'

# String Data Type
# 1
def capitalize(word=str):
    for i in list(word):
        print(i.capitalize(), end='')
# 2
def remove_vowels(word=str):
    vowels = ['a', 'e', 'o', 'u', 'i']
    for i in word:
        if i in vowels:
            pass
        else:
            print(i, end='')
# 3
def reverse_string(a=str):
    for i in a:
        print(a[-(int(list(a).index(i))+1)], end='')
        
# 4 
def replace_spaces_with_underscores(a=str):
    for i in a:
        if i == ' ':
            print('_', end='')
        else:
            print(i, end='')
# 5
def is_palindrome(word=str):
    for i in range(len(word)):
        if word[i] == word[-(i+1)]:
            continue
        elif word[i] != word[-(i+1)]:
            return 'The given word is not palindrome'
            break
    return 'The given word is palindrome'
# 6
def replace_a_with_o(word=str):
    for i in word:
        if i == 'a':
            print('o', end='')
        else:
            print(i, end='')
# 7 
def get_username_from_email(email=str):
    return email.split('@')[0]
# 8 
def title_case(s=str):
    s = s.split(' ')
    for i in s:
        print(i.capitalize(), end=' ')
# 9
def remove_first_last_ch(word=str):
    return word.split(word[0])[1].split(word[-1])[0]
# 10
def is_word_in_sentence(word=str, sentence=str):
    sentence = sentence.split(' ')
    if word in sentence:
        print('The word is in the sentence')
    else:
        print('The word is not in the sentence')
# 11
def first_occurrence(ch=str, sentence=str):
    for i in sentence:
        if i == ch:
            return sentence.index(i)
        else:
            continue
# 12
def last_three_ch(word: str):
    return word[len(word)-3:]
# 13
def for_loop_string(word: str, i):
    for a in range(i-1):
        print(word)

# 14 
def return_each_w_sep(sentence: str):
    for i in sentence.split(' '):
        print(i)

# 15
def return_even(word: str):
    for i in range(len(word)):
        if i%2 == 0:
            print(word[i], end='')

# 16
def title_case2(sentence: str):
    mask = ''
    for i in sentence.split(' '):
        mask += i.capitalize() + ' '
    return f'Title: {mask}'
# 17
def reverse_sentence(sentence: str):
    for i in range(len(sentence)):
        print(sentence[-(i+1)], end='')
# 18 
def length_diff(string1: str, string2: str):
    print(f'len of 1st string: {len(string1)}')
    print(f'len of 2nd string: {len(string2)}')
    print(f'The difference is {abs(len(string1) - len(string2))}')

# Boolean Data Type
# 1
def login():
    username = input('Username: ')
    password = input('Password: ')
    if username and password:
        return True
    else:
        return False
# 2
def are_2_int_equal(int1: int, int2: int):
    return True if int1 == int2 else False
# 3
def check_if_pos_and_even(n):
    return True if n>=0 and n//2==0 else False
# 4 
def are_3_int_diff(
    int1: int, int2: int, int3: int
):
    return True if int1 != int2 and int1 != int3 and int2 != int3 else False

# 5
def is_len_equal(string1: str, string2: str):
    return True if len(string1) == len(string2) else False
# 6 
def is_div_by_three_n_five(n: int):
    return True if n//3==0 and n//5==0 else False

# 7 
def is_sum_greater_than_50(int1: int, int2: int):
    return False if int1+int2>=50 else False
# 8
def is_between_10_and_20(n=int):
    return True if n in range(10,21) else False
 
