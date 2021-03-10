import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

f2 = open('rmdmy_content.txt', 'r', encoding='utf-8')
word = f2.readlines()
# 大风厂（感兴趣的关键字，可能需要加入到词典中）
text = []
# 遍历每句话
for line in word:
    if '大风厂' in line:
        text.append(line)

# 词频统计
# dict_dz = {}
# for i in text:
#     dz1 = i.split(' ')
#     for w in dz1:
#         w1 = w.strip()
#         if dict_dz.__contains__(w1):
#             dict_dz[w1] += 1
#         else:
#             dict_dz[w1] = 1

# 生成text
text1 = ''
for i in text:
    dz2 = i.split(' ')
    for w in dz2:
        text1 = text1 + ' ' + w

# 生成词云图


# 读取背景图片信息保存为array
background_Image = plt.imread('c1.jpg')
font = r'C:\Windows\Fonts\simfang.ttf'

# 设置字体格式路径，不然显示不了中文，
# 可以改成r'C:\Windows\Fonts\xxxx.ttf'来切换其他字体，这边我们把文件放在默认文件夹中。
# 选择已经有的字体，根据词频否则生成图片的时候会报错：OSError: cannot open resource

wc = WordCloud(background_color='white', mask=background_Image,
               max_words=2000, stopwords=STOPWORDS, font_path=font,
               max_font_size=80, random_state=42, scale=1.5).generate(text1)

# 这种方法和上面直接generate()的结果相同，但是传入的数据格式不同，
# 这个函数传入的是要给字典，key（键）为词，value(值)为出现频率。
# wc.generate_from_frequencies(dict_dz)

# 根据图片生成词云颜色，这里选择显眼的颜色
# 如果需要黑白灰的词云颜色就把'#'删除
# image_colors = ImageColorGenerator(background_Image)
# wc.recolor(color_func = image_colors)
plt.imshow(wc)
plt.axis('off')
plt.show()
wc.to_file('c2.jpg')  # 保存图片

from jieba import analyse

# import jieba
# jieba.load_userdict('rmdmy_dict.txt')

tfidf = analyse.extract_tags
# analyse.set_stop_words('stop_words.txt') #使用自定义停用词集合

text_dz = ''
for l in text:
    text_dz += l
    text_dz += ' '
keywords = tfidf(text_dz, topK=20)
print(keywords)
