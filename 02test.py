#!/usr/bin/env python
# coding=utf-8
'''
 Author       : lishuo
 Date         : 2020-08-17 22:14:07
 LastEditors  : lishuo
 LastEditTime : 2020-09-26 09:28:16
 Description  : 测试git
 FilePath     : \\python_code\\02test.py
'''
from math import sqrt
# from time import sleep
# import random
""" import os
import time """

# from random import randint
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


""" def main():
    content = '北京欢迎为你开天辟地…………'
    while True:
        # 清理屏幕上的输出
        os.system('cls')  # os.system('clear)
        print(content)
        # 休眠200毫秒
        time.sleep(0.2)
        content = content[1:] + content[0]


if __name__ == '__main__':
    main() """


""" def generate_code(code_len=4):
    all_chars = \
        '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    last_pos = len(all_chars) - 1
    code = ''
    for _ in range(code_len):
        index = random.randint(0, last_pos)
        code += all_chars[index]
    return code


if __name__ == '__main__':
    print(generate_code()) """

'''
 description: 获取文件名的后缀
 param {filename, has_dot}
 return {文件后缀名}
'''
""" def get_suffix(filename, has_dot=False):
    pos = filename.rfind('.')
    print('pos为: {}'.format(pos))
    if 0 < pos < len(filename) - 1:
        index = pos if has_dot else pos + 1
        return filename[index:]
    else:
        return ''


if __name__ == '__main__':
    print(get_suffix('12322.txt2')) """


''' # 类
class Test:

    def __init__(self, foo):
        self.__foo = foo

    def __bar(self):
        print(self.__foo)
        print('__bar')


def main():
    test = Test('hello')
    # test.__bar()
    print(test.__foo)


if __name__ == "__main__":
    main()
 '''


''' class Clock(object):
    # 数字时钟

    def __init__(self, hour=0, minute=0, second=0):
        self._hour = hour
        self._minute = minute
        self._second = second

    def run(self):
        # 走字
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0

    def show(self):
        # 显示时间
        return '%02d:%02d:%02d' %  \
            (self._hour, self._minute, self._second)


def main():
    clock = Clock(23, 59, 58)
    while True:
        print(clock.show())
        sleep(1)
        clock.run()


if __name__ == '__main__':
    main() '''


''' class Person(object):

    def __init__(self, name, age):
        self._name = name
        self._age = age

    # 访问器 - getter方法
    @property
    def name(self):
        return self._name

    # 访问器 - getter方法
    @property
    def age(self):
        return self._age

    # 修改器 - setter方法
    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <= 16:
            print('%s正在玩飞行棋.' % self._name)
        else:
            print('%s正在玩斗地主.' % self._name)


def main():
    person = Person('王大锤', 12)
    person.play()
    person.age = 22
    person.play()
    # person.name = '白元芳'  # AttributeError: can't set attribute


if __name__ == '__main__':
    main()
 '''


""" class Person(object):

    # 限定Person对象只能绑定_name, _age和_gender属性
    __slots__ = ('_name', '_age', '_gender')

    def __init__(self, name, age):
        self._name = name
        self._age = age

    # 访问器 - getter方法
    @property
    def name(self):
        return self._name

    # 访问器 - getter方法
    @property
    def age(self):
        return self._age

    # 修改器 - setter方法
    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <= 16:
            print('%s正在玩飞行棋.' % self._name)
        else:
            print('%s正在玩斗地主.' % self._name)


def main():
    person = Person('王大锤', 22)
    person.play()
    person._gender = '男'


if __name__ == '__main__':
    main() """


""" class Triangle(object):

    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    @staticmethod
    def is_valid(a, b, c):
        return a + b > c and b + c > a and a + c > b

    def perimeter(self):
        return self._a + self._b + self._c

    def area(self):
        half = self.perimeter() / 2
        return sqrt(half * (half - self._a)*(half - self._b)*(half - self._c))


def main():
    a, b, c = 3, 4, 5
    if Triangle.is_valid(a, b, c):
        t = Triangle(a, b, c)
        print(t.perimeter())
        print(t.area())
    else:
        print('无法构成三角形')


if __name__ == '__main__':
    main() """


""" class Person(object):
    # 人

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        print('{}正在愉快的玩耍'.format(self._name))

    def watch_av(self):
        if self._age >= 18:
            print('{}正在看动作片'.format(self._name))
        else:
            print('{}只能看熊出没'.format(self._name))


class Student(Person):
    # 学生

    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self._grade = grade

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, grade):
        self._grade = grade

    def study(self, course):
        print('{}的{}正在学习{}'.format(self._grade, self._name, course))


class Teacher(Person):
    # 老师

    def __init__(self, name, age, title):
        super().__init__(name, age)
        self._title = title

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    def teach(self, course):
        print('{}{}正在讲{}'.format(self._name, self._title, course))


def main():
    stu = Student('王大锤', 15, '初三')
    stu.study('数学')
    stu.watch_av()
    t = Teacher('张三', 38, '砖家')
    t.teach('Python程序设计')
    t.watch_av()


if __name__ == '__main__':
    main() """

