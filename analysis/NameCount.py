import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import pandas as pd

import matplotlib.font_manager as fm

font_yahei_consolas = fm.FontProperties(fname=r"C:\Windows\Fonts\simfang.ttf")  # 引入字体，否则文字显示不出
# python 字符串转列表 list 出现\ufeff的解决方法(网上)
# 文件内容 lisi
# lock = open("lock_info.txt", "r+",encoding="utf-8")
# lock_line = lock.readline()
# lock_list = lock_line.split(",")
# print(lock_list)
#
# y = lock_line.encode('utf-8').decode('utf-8-sig')
# print(y)
#
# 打印结果如下
# ['\ufefflisi']
# lisi
# 自己测试，在notepad++上把编码从UTF-8编码模式改成UTF-8无BOM编码模式，ufeeff就会消失

with open('rmdmy_dict.txt', encoding='utf-8') as f1:
    data1 = f1.readlines()
with open('rmdmy_content.txt', encoding='utf-8') as f2:
    data2 = f2.read()

# 匹配词典里的名字和剧本内容里的名字出现的次数
count = []
for name in data1:
    count.append([name.strip(), data2.count(name.strip())])
count1 = []
for i in count:
    if i not in count1:
        count1.append(i)
count = count1

count.sort(key=lambda x: x[1])  # 对count里的名字次数进行排序 count(x[0]名字,x[1]次数)
ay, ax = plt.subplots()
# count[-10:]取count后10个数据 如果为count[10:0]为去除前10个数据 count[0:10]取前10个数据 count[0:-10]去除后10个数据
numbers = [x[1] for x in count[-10:]]
names = [x[0] for x in count[-10:]]
ax.barh(range(10), numbers, color=['peru', 'coral'], align='center')
ax.set_title('人物出场次数', fontsize=14, fontproperties=font_yahei_consolas)
ax.set_yticks(range(10))
ax.set_yticklabels(names, fontsize=14, fontproperties=font_yahei_consolas)
plt.show()
