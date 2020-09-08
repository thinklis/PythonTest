#!/usr/bin/env python
# coding=utf-8
'''
 Author       : lishuo
 Date         : 2020-08-17 14:08:22
 LastEditors  : lishuo
 LastEditTime : 2020-08-26 21:30:41
 Description  : 第一天练习python编程
 FilePath     : \\python_code\\01test.py
'''

""" print('1. ', 4.0 == 4)
print('2. ', "4.0" == 4)
print('3. ', bool("1"))
print('4. ', bool('0'))
print('5. ', str(32) == '32')
print('6. ', int(6.26))
print('7. ', float(32))
print('8. ', float("3.21"))
print('9. ', int('434'))  # 字符串类型不能用int转换成整型
# print('10. ', int('3.42'))
# # ValueError invalid literal for int() with base 10: '3.42'
print('11. ', bool(-1))   # 为什么这个时true呢
print('12. ', bool(""))
print('13. ', bool(0))
print('14. ', 'wrqq' > 'acd')
print('15. ', 'ttt' == 'ttt ')
print('16. ', 'wer'*3)
print('17. ', 'wer' + '2222')

print('修改01test.py文件，目的练习git的使用')
print('第二次修改test.py文件')
print('这里是我在dev分支上的修改1')
print('这是我在切换master分支后做的修改2')
print('这是我在feature1分支上做的修改1') """

'''
 description: 将列表里面的数据变为原来的2倍
 param {lst}
 return {type}
'''


''' def double_list(lst):
    for index, item in enumerate(lst):
        if isinstance(item, bool):
            continue
        if isinstance(item, (int, float)):
            lst[index] *= 2
        if isinstance(item, list):
            double_list(item)


if __name__ == '__main__':
    lst = [1, [4, 6], True]
    double_list(lst)
    print(lst) '''

''' print('这里是dev分支')
print('今天学到了1.3.7')
print('元组练习')
 '''

''' dic = {
    'python': 95,
    'java': 99,
    'c': 100
}
print(len(dic))
info = {
    '小明': {
        'fruits': ['苹果', '草莓', '香蕉'],
        'money': 89
    },
    '小刚': {
        'fruits': ['葡萄', '橘子', '樱桃'],
        'money': 87
    }
} '''

''' lst1 = [1, 2, 3, 5, 6, 3, 2]
lst2 = [2, 5, 7, 9]

set1 = set(lst1)
set2 = set(lst2)

# 那些整数既在lst1中，也在lst2中
print(set1.intersection(set2))

# 哪些整数在lst1中，不在lst2中
print(set1.difference(set2))

# 两个列表一共有哪些整数
print(set1.union(set2)) '''

# 2.基础语法篇
# if条件语句
''' value = input('请输入一个整数: ')
i_value = int(value)
if i_value % 2 == 0:
    print('您输入的整数时：{value},它是偶数'.format(value=value))
else:
    print('您输入的整数时：{value},它时奇数'.format(value=value))
 '''

''' # 多条条件分支
value = input('请输入一个整数：')

if value == 'python':
    print(90)
elif value == 'java':
    print(95)
elif value == 'php':
    print(85)
else:
    print(0)
 '''
''' value = input('请输入一个整数：')
if not value.isdigit():
    print('无法使用int函数转换')
else:
    i_value = int(value)
    if i_value % 2 == 1:
        print(i_value*2)
    elif i_value %4 == 0:
        print(i_value / 4)
    elif i_value > 20:
        print(i_value - 20)
    else:
        print(i_value)
 '''
''' print(list(range(3, 20, 4)))
print(list(range(3, 20)))
print(list(range(10, 5)))
print(list(range(2, 12))) '''

''' lst = [1, 3, 5, 2, 7, 9]
for index in range(len(lst)):
    print(lst[index])
print('------')
# 使用range函数，通过下表逆序遍历列表
for index2 in range(len(lst)-1, -1, -1):
    print(lst[index2])

print('\n通过下表逆序遍历1')
for i in lst[::-1]:
    print(i, end=" ")

print("\n通过reversed逆序遍历")
for i in reversed(lst):
    print(i, end=' ')

print('\n遍历输出列表里的所有偶数')
for i in range(len(lst)):
    if lst[i] % 2 == 0:
        print(lst[i])

print('\n遍历列表，输出大约3的奇数')
for i in range(len(lst)):
    if lst[i] > 3 and lst[i] % 2 == 1:
        print(lst[i]) '''

''' # 使用for循环遍历字典
dic = {
    'python': 90,
    'java': 95
}
for key in dic:
    print(key, dic[key])
print('\n第二种方法')
for key, value in dic.items():
    print(key, value) '''

''' lst = [1, 3, 5, 2, 7, 9, 10]
for item in lst:
    if item % 2 == 0:
        print(item)
 '''
''' lst = [3, 6, 1, 8, 1, 9, 2]
max_value = lst[0]
for item in lst:
    if item > max_value:
        max_value = item
print(max_value) '''

''' # 寻找lst列表里面的最小值
lst = [3, 6, 1, 8, 1, 9, 2]
min_value = lst[0]
for item in lst:
    if item < min_value:
        min_value = item
print(min_value) '''

''' # 寻找列表里的最小的偶数
lst = [3, 6, 1, 8, 1, 9, 2]
min_even_value = lst[0]
for item in lst:
    if item % 2 == 0 and item < min_even_value:
        min_even_value = item
print(min_even_value) '''

''' # 寻找列表里面最大的奇数
lst = [3, 6, 1, 8, 1, 9, 2]
max_odd_value = lst[0]
for item in lst:
    if item % 2 == 1 and item > max_odd_value:
        max_odd_value = item
print(max_odd_value)
 '''

# 寻找组合
''' lst1 = [3, 6, 1, 8, 1, 9, 2]
lst2 = [3, 1, 2, 6, 4, 8, 7]

for item1 in lst1:
    for item2 in lst2:
        if item1 + item2 == 10:
            print((item1, item2)) '''

''' # 寻找两个数的差的绝对值等于2的组合

lst1 = [3, 6, 1, 8, 1, 9, 2]
lst2 = [3, 1, 2, 6, 4, 8, 7]

for item1 in lst1:
    for item2 in lst2:
        if item1 - item2 == 2 or item2 - item1 == 2:
            print((item1, item2))
 '''

''' # 计算两个列表里面元素相乘的最大值
lst1 = [3, 6, 1, 8, 1, 9, 2]
lst2 = [3, 1, 2, 6, 4, 8, 7]

max_value = 0
for item1 in lst1:
    for item2 in lst2:
        value12 = item1 * item2
        if value12 > max_value:
            max_value = value12
print(max_value) '''

# while 循环
''' # 奇偶数判断
while True:
    input_str = input('请输入一个正整数，想退出程序请输入quit：')
    if input_str == 'quit':
        break
    number = int(input_str)
    if number % 2 == 0:
        print('你输入的是一个偶数')
    else:
        print('你输入的是一个奇数') '''

''' # for循环与while循环嵌套
lst = [2, 3, 4]

for item in lst:
    while True:
        input_str = input('请输入{number}的倍数，想停止输入时，输入quit；'.format(number=item))
        if input_str == 'quit':
            break
        number = int(input_str)
        if number % item == 0:
            print('输入正确')
        else:
            print('输入错误') '''
''' while True:
    input_str = input('请输入一个正整数，如果想停止程序，输入quit：')
    if input_str == 'quit':
        break
    number = int(input_str)
    if number > 10:
        print('输入大于10，不判断奇偶')
        continue
    if number % 2 == 0:
        print('输入为偶数')
    else:
        print('输入为奇数') '''

# 内置函数篇


''' def my_abs(number):
    if not isinstance(number, (float, int)):
        return number
    if number < 0:
        number *= -1
    return number


if __name__ == '__main__':
    print(my_abs(-3))
    print(my_abs(-3.9))
    print(my_abs(54.3))
    print(my_abs('123')) '''

# sum函数
'''
description: 返回列表里面所有的数据总和，
如果列表里有非数字类型的数据，忽略不管
param {type}
return {type}
'''


''' def my_sum(lst):

    sum_res = 0
    if not isinstance(lst, list):
        return sum_res
    for item in lst:
        if isinstance(item, (float, int)):
            sum_res += item
    return sum_res


if __name__ == '__main__':
    lst = [3, 4, '43', 5.4]
    print(my_sum(lst)) '''

# max函数
'''
 description: 返回序列里的最大值
 param {lst}}
 return {type}
'''


''' def my_max(seq):
    max_value = None
    if not isinstance(seq, (list, tuple)):
        return max_value
    if len(seq) == 0:
        return max_value
    max_value = seq[0]
    for item in seq:
        if not isinstance(item, (float, int)):
            continue
        if item > max_value:
            max_value = item
    return max_value


if __name__ == '__main__':
    lst = [3, 4, '43', 5.4]
    print(my_max(lst)) '''

# min函数
# 返回序列里面的最小值


""" def my_min(seq):
    min_value = None
    if not isinstance(seq, (list, tuple)):
        return min_value
    if len(seq) == 0:
        return min_value
    min_value = seq[0]
    for item in seq:
        if not isinstance(item, (float, int)):
            continue
        if item < min_value:
            min_value = item
    return min_value


if __name__ == '__main__':
    lst = [3, 4, '43', 5.4]
    print(my_min(lst)) """

# int函数
# 将字符串string类型转换为int类型数据
""" str_int_dic = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9
}


def my_int(string):
    res = 0
    for item in string:
        int_value = str_int_dic[item]
        res = res*10 + int_value
    return res


if __name__ == '__main__':
    print(type(my_int('432'))) """

# str函数
""" def my_str(int_value):
    if int_value == 0:
        return '0'
    lst = []
    is_positive = True
    if int_value < 0:
        is_positive = False
        int_value = abs(int_value)
    while int_value:
        number = int_value % 10   # 个位数
        int_value //= 10  # 去除个位数后，还剩下的内容
        str_number = chr(number+48)
        lst.append((str_number))
    if not is_positive:
        lst.append('-')
    lst = lst[::-1]
    return ''.join(lst)


if __name__ == '__main__':
    print(my_str(0))
    print(my_str(123))
    print(my_str(-123))
    print(type(my_str(0))) """

# float函数
""" str_int_dic = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9
}


def my_int(string):
    res = 0
    for item in string:
        int_value = str_int_dic[item]
        res = res*10 + int_value
    return res


def my_float(string):
    arrs = string.split('.')
    int_value = my_int(arrs[0])
    float_value = my_int(arrs[1])
    while float_value > 1:
        float_value *= 0.1
    return int_value + float_value


if __name__ == '__main__':
    print(my_float('34.22'))
    print(type(my_float('34.22'))) """

# len函数

""" from collections import Iterable


def my_len(obj):
    if not isinstance(obj, Iterable):
        return None
    length = 0
    for item in obj:
        length += 1
    return length


if __name__ == '__main__':
    print(my_len('232'))
    print(my_len([3, 4, 2, 1]))
    print(my_len({'a': 4, 'b': 4}))
    print(my_len((3, 5, 6, 6, 3)))
    print(set([3, 5, 6, 6, 3]))  # set会去重 """

""" lst = ['a', 'b', 'c']
for index, item in enumerate(lst):
    print(index, item)
 """

# 实现和enumerate类似的功能


""" def my_enumerate(lst):
    for i in range(len(lst)):
        yield i, lst[i]


lst = ['a', 'b', 'c']
for index, item in my_enumerate(lst):
    print(index, item) """

# 深入理解return和yield


""" def squre(n):
    ls = [i*i for i in range(n)]
    return ls


for i in squre(5):
    print(i, end=' ') """


""" def squre(n):
    for i in range(n):
        yield i*i


for i in squre(5):
    print(i, end=' ') """
# all 函数
""" lst = [True, False, True]
tup = (True, True, True)
print(all(lst))
print(all(tup)) """


""" def my_all(lst):
    for item in lst:
        if not item:
            return False
    return True


if __name__ == '__main__':
    print(my_all([True, False, True])) """

# any函数
""" lst = [True, False, False]
print(any(lst))
 """


""" def my_any(lst):
    for item in lst:
        if item:
            return True
    return False


if __name__ == '__main__':
    print(my_any([True, False, False])) """


# bin函数，可以获取整数的二进制形式
# print(bin(10))
'''
    description: 返回正整数value的二进制形式
    param {value}
    return {type}
'''


""" def my_bin(value):
    lst = []
    while value:
        if value % 2 == 1:
            lst.append('1')
        else:
            lst.append('0')
        value = value >> 1
        print('value====',value)
    lst = lst[::-1]
    return ''.join(lst)


print(bin(10))

if __name__ == '__main__':
    # print(my_bin(3))
    # print(my_bin(8))
    print(my_bin(10)) """

# 字符串方法
'''
 description:返回字符串source中，
 子串target开始的位置，从start索引开始搜索
 param {source, target, start}
 return {type}
'''


""" def my_find(source, target, start=0):
    if not source or not target:
        return -1
    # 不合理的搜索起始位置
    if start < 0 or start >= len(source):
        return -1
    if len(target) > len(source):
        return -1
    for index in range(start, len(source) - len(target)+1):
        t_index = 0
        while t_index < len(target):
            if target[t_index] == source[t_index+index]:
                t_index += 1
            else:
                break
        if t_index == len(target):
            return index
    return -1


if __name__ == '__main__':
    # print(my_find('this is a book', 'this'))
    # print(my_find('this is a book', 'this', start=1))
    print(my_find('this is a book', 'book'))
    print(my_find('this is a book', 'k', start=10))
    print(my_find('this is a book', 'book', start=10))
    print(my_find('this is a book', 'a', start=3)) """


# 字符串中的replace方法

'''
 description: 将字符串里所有的oldsub子串替换成newsub
 param {source, oldsub, newsub}}
 return {type}
'''


''' def my_replace(source, oldsub, newsub):
    if not source or not oldsub:
        return source
    new_string = ''
    start_index = 0
    index = my_find(source, oldsub, start=start_index)
    while index != -1:
        new_string += source[start_index:index] + newsub
        start_index = index+len(oldsub)
        index = my_find(source, oldsub, start=start_index)
    new_string += source[start_index:]
    return new_string '''


'''
 description:返回字符串source中 子串target开始的位置，从start索引开始搜索
 param {source, target, start}
 return {type}
'''


''' def my_find(source, target, start=0):
    if not source or not target:
        return -1
    # 不合理的搜索起始位置
    if start < 0 or start >= len(source):
        return -1
    if len(target) > len(source):
        return -1
    for index in range(start, len(source) - len(target)+1):
        t_index = 0
        while t_index < len(target):
            if target[t_index] == source[t_index+index]:
                t_index += 1
            else:
                break
        if t_index == len(target):
            return index
    return -1


if __name__ == '__main__':
    print(my_replace('this is a book', 'this', 'it'))
    print(my_replace('this is a this book', 'this', 'it'))
    print(my_replace('this is a this bookthis', 't2his', 'it')) '''

# split函数
'''
 description:返回字符串source中 子串target开始的位置，从start索引开始搜索
 param {source, target, start}
 return {type}
'''


''' def my_find(source, target, start=0):
    if not source or not target:
        return -1
    # 不合理的搜索起始位置
    if start < 0 or start >= len(source):
        return -1
    if len(target) > len(source):
        return -1
    for index in range(start, len(source) - len(target)+1):
        t_index = 0
        while t_index < len(target):
            if target[t_index] == source[t_index + index]:
                t_index += 1
            else:
                break
        if t_index == len(target):
            return index
    return -1 '''


'''
 description:以seq分割字符串source
 param {source, seq, maxsplit}
 return {type}
'''


''' def my_split(source, sep, maxsplit=-1):
    if not source or not sep:
        return []
    lst = []
    max_split_count = maxsplit if maxsplit > 0 else len(source)
    split_count = 0
    start_index = 0
    index = my_find(source, sep, start=start_index)
    while split_count < max_split_count and index != -1:
        sep_str = source[start_index:index]
        lst.append(sep_str)
        split_count += 1
        start_index = index + len(sep)
        index = my_find(source, sep, start=start_index)
    sep_str = source[start_index:]
    lst.append(sep_str)
    return lst


if __name__ == '__main__':
    print(my_split('1,3,4', ','))
    print(my_split('abcadae', 'a'))
    print(my_split('abcadae', 'a', maxsplit=2)) '''


