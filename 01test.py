#!/usr/bin/env python
# coding=utf-8
'''
 Author       : lishuo
 Date         : 2020-08-17 14:08:22
 LastEditors  : lishuo
 LastEditTime : 2020-08-22 22:06:39
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


def double_list(lst):
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
    print(lst)

print('这里是dev分支')
