import jieba
import re

jieba.load_userdict('rmdmy_dict.txt')  # 自定义词典

# 简体中文停用词
stopword = [line.strip() for line in open('StopwordsCN.txt', encoding='utf-8').readlines()]

fr = open('rmdmy.txt', 'r', encoding='utf-8')
con = fr.readlines()

'''
分词，并去掉特殊字符、词语
'''
fw = open('rmdmy_content.txt', 'w', encoding='utf-8')
for i in con:
    if len(i) <= 10:  # if len(i.decode('utf-8'))<=10:
        pass
    else:
        w1 = i.split("。")  # 按句号分句
        for j in w1:
            w2 = re.sub(r'，|。|？|“|”|！', '', j.strip())  # 去符号,吧，。？等用"替代
            # w1 = re.sub(name1,name2,w1) #实体对齐,用name1（正则表达式）代替name2   re.sub(pattern, repl, string, count=0, flags=0)
            w3 = list(jieba.cut(w2))  # 分词
            w4 = [w for w in w3 if w not in stopword]  # 去停用词
            outstr = ''
            for word in w4:
                outstr += word
                outstr += ' '
            fw.write(outstr.strip().encode('utf-8').decode())
            fw.write('\n')
fw.close()

