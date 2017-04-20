#!/usr/bin/env python
__author__ = 'xudazhou'

# ######################### 字典 ##########################
"""
dict1 = {"k1": "v1", "k2": "v2"}
print("dict1['k1']:%s" % dict1['k1'])  # 索引获取记录

dict1['k3'] = 'v3'  # 添加
del dict1['k2']  # 删除
print("dict1 count:%d" % len(dict1))  # 大小
for k, v in dict1.items():  # 遍历
    print("dict1[%s]=%s" % (k, v), end=",")

print("")
if 'k3' in dict1:  # 判断
    print('dict1[k3]:%s' % dict1['k3'])
"""

dict2 = { "k2" : [4, 5, 6], "k3" :[2, 3, 5], "k1" : [1, 2, 3] }
print(dict2)  # {'k3': [2, 3, 5], 'k2': [4, 5, 6], 'k1': [1, 2, 3]} # key的顺序每次执行是随机的
keys = dict2.keys()  # 这个 keys 不是 list，不能直接调用 sort()
print(keys)  # dict_keys(['k3', 'k2', 'k1'])

keys = sorted(dict2.keys())
print(dict2)  # {'k3': [2, 3, 5], 'k2': [4, 5, 6], 'k1': [1, 2, 3]} 原字典的顺序不变
print(keys)  # ['k1', 'k2', 'k3']

print(dict2["k2"][0])  # 4
# 报错 KeyError: 'k3'
# print(dict2["k3"])
print(dict2.items())  # dict_items([('k2', [4, 5, 6]), ('k1', [1, 2, 3])])
