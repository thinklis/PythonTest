#!/usr/bin/env python
# coding=utf-8
'''
 Author       : lishuo
 Date         : 2020-08-17 14:08:22
 LastEditors  : lishuo
 LastEditTime : 2020-08-24 15:08:28
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

