splited_news = []
list_for_words = []
dict_for_words = {}
import xml.etree.ElementTree as ET
parser = ET.XMLParser(encoding = 'utf-8')
tree = ET.parse('newsafr.xml', parser)
root = tree.getroot()

news_list = root.findall('channel/item')
for news in news_list:
  descript = news.find('description').text
  splited_news.append(descript.split())

for news in splited_news:
   for element in news:
    list_for_words.append(element)

for words in list_for_words:
    if len(words) > 6:
      dict_for_words[words] = (list_for_words.count(words), 'раз встречается слово')
words_number_of_words = zip(dict_for_words.values(), dict_for_words.keys())
print(sorted(list(words_number_of_words), reverse=True)[0:11])