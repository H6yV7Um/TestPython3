__author__ = 'xudazhou'

# 格式化
# g
'''
print("%g" % 0.000454)    # 0.000454
print("%g" % 0.0000454)   # 4.54e-05
print("%g" % 0.00000454)  # 4.54e-06
'''

# dict
#print("%(a)s %(b)s" % {"a": "小王", "b": "小李"})  # 小王 小李


# split
# 默认以空白分隔
'''
str1 = "a  b c   d  e"
tuple1 = str1.split()
print(tuple1)  # ['a', 'b', 'c', 'd', 'e']
'''

# 字符串替换
str1 = "http://www.eaipatterns.com/img/ChannelIcon.gif"
# print(str1.replace("eaipatterns", "enterpriseintegrationpatterns"))


# str2_1 = "abc"
# str2_2 = "你好"
# str2_3 = ""
# print(len(str2_1))  # 3
# print(len(str2_2))  # 2
# print(len(str2_3))  # 0

str1 = "aa"
str2 = "bb"
print(str1==str2)