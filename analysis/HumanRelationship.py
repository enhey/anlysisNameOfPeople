import numpy as np
import pandas as pd


with open('rmdmy_dict.txt', encoding='utf-8') as f1:
    data1 = f1.readlines()
# 社交网络关系（共现矩阵）
f2 = open('rmdmy_content.txt', 'r', encoding='utf-8')
word = f2.readlines()
name = data1
# name=data1[1:]
# 总人数
wordcount = len(name)
# 初始化128*128值全为0的共现矩阵
cormatrix = [[0 for col in range(wordcount)] for row in range(wordcount)]  # 生成wordcount*wordcount的数组
# 遍历矩阵行和列
for colindex in range(wordcount):
    for rowindex in range(wordcount):
        cornum = 0
        # 如果两个人名字在同一句话出现，那么出现矩阵中两个人对应的值加1
        for originline in word:
            if name[colindex].strip() in originline and name[rowindex].strip() in originline:
                cornum += 1
        cormatrix[colindex][rowindex] = cornum

cor_matrix = np.matrix(cormatrix)
for i in range(len(name)):
    cor_matrix[i, i] = 0
social_cor_matrix = pd.DataFrame(cor_matrix, index=name, columns=name)
# 把共现矩阵存入excel
social_cor_matrix.to_csv('social_cor_matrix.csv')

social_contact = pd.DataFrame(columns=['name1', 'name2', 'frequency'])
# 共现频率
for i in range(0, len(name)):
    for j in range(0, len(name)):
        if i < j and cormatrix[i][j] > 0:
            social_contact.loc[len(social_contact), 'name1'] = name[i]  # 加一行
            social_contact.loc[len(social_contact) - 1, 'name2'] = name[j]  # 上面加了一行，所以总行数已经加一，所以-1
            social_contact.loc[len(social_contact) - 1, 'frequency'] = cormatrix[i][j]


social_contact.to_excel('social_contact.xlsx', index=False)
