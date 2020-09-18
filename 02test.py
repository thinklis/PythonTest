#!/usr/bin/env python
# coding=utf-8
'''
 Author       : lishuo
 Date         : 2020-08-17 22:14:07
 LastEditors  : lishuo
 LastEditTime : 2020-09-18 22:49:44
 Description  : 测试git
 FilePath     : \\python_code\\02test.py
'''

from random import randint
""" print('测试自动保存功能')
print('测试编辑器失去焦点时自动保存功能') """

""" # python面向对象编程练习 """

""" print(chr(50))
print(ord('2'))

f = float(input('请输入华氏摄氏'))
c = (f - 32) / 1.8
print('{:.1f}华氏度 = {:.1f}摄氏度'.format(f, c))
print(f'{f:.1f}华氏度 = {c:.2f}摄氏度') """

""" sum = 0
for x in range(2, 101, 2):
    sum += x
print(sum) """


""" sum = 0
for x in range(1, 101):
    if x % 2 == 0:
        sum += x
print(sum) """

""" answer = random.randint(1, 100)
counter = 0
while True:
    counter += 1
    number = int(input('请输入：'))
    if number < answer:
        print('大一点')
    elif number > answer:
        print('小一点')
    else:
        print('猜对了')
        break
print('你一共猜了{}次'.format(counter))
if counter > 7:
    print('你的智商余额明显不足') """


""" for i in range(1, 10):
    for j in range(1, i + 1):
        print('%d*%d=%d' % (i, j, i * j), end='\t')
    print() """

""" row = int(input('请输入行数: '))
for i in range(row):
    for _ in range(row - i - 1):
        print(' ', end='')
    for _ in range(2 * i + 1):
        print('*', end='')
    print() """

""" # 寻找水仙花
for num in range(100, 1000):
    low = num % 10
    mid = num // 10 % 10
    high = num // 100
    if num == low ** 3 + mid ** 3 + high ** 3:
        print(num) """


""" for x in range(0, 20):
    for y in range(0, 33):
        z = 100 - x - y
        if 5 * x + 3 * y + z / 3 == 100:
            print('公鸡: %d只, 母鸡: %d只, 小鸡: %d只' % (x, y, z))
 """

""" m = int(input('m = '))
n = int(input('n = '))
fm = 1
for num in range(1, m + 1):
    fm *= num
fn = 1
for num in range(1, n + 1):
    fn *= num
fm_n = 1
for num in range(1, m - n + 1):
    fm_n *= num
print(fm // fn // fm_n)
 """

""" total = 0
for _ in range(2):
    total += randint(1, 6)
    print('第{}次total，为{}'.format(_, total))
print(total) """
""" # 在参数名前面的*表示args是一个可变参数


def add(*args):
    total = 0
    for val in args:
        total += val
    return total


# 在调用add函数时可以传入0个或多个参数
print(add())
print(add(1))
print(add(1, 2))
print(add(1, 2, 3))
print(add(1, 3, 5, 7, 9)) """

