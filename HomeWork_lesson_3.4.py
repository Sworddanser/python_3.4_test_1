import json
import chardet


def get_file(file):
    with open(file, 'rb') as f:
        data = f.read()
        result = chardet.detect(data)
        s = data.decode(result['encoding'])
        data = json.loads(s)
    b = data['rss']
    c = b['channel']
    d = c['items']
    news_words_list = []
    news_words = []
    for news in d:
        news_words_list.append(news['description'].split())
    for item_list in news_words_list:
        for items in item_list:
            if items.isalpha() is True:
                news_words.append(items)
    return news_words


def get_count_dict(news_words):
    q = []
    for words in news_words:
        l = len(words)
        if l > 6:
            q.append(words)
    q2 = []
    for i in q:
        if i not in q2:
            q2.append(i)
    fin = {}
    for i in q2:
        fin[i] = q.count(i)
    return fin


def get_answer(fin):
    answer_name = []
    answer_count = []
    for a, y in fin.items():
        if y == max(fin.values()):
            t = a
            answer_name.append(t)
            answer_count.append(y)
            i = 1
            while i <= 10:  # не могу понять почему ваил не обнуляет максимальное значение что бы максимум столо другое?
                i += 1
                fin[t] = 0
    return answer_name, answer_count


def main():
    file_name = ['newsafr.json', 'newscy.json', 'newsfr.json', 'newsit.json']
    file = input('Выберите фаил(newsafr.json, newscy.json, newsfr.json, newsit.json):')
    if file in file_name:
        news_words = get_file(file)
        fin = get_count_dict(news_words)

        answer = get_answer(fin)

        print('Самые часто повторяющиеся слова:', answer[0], 'значения повторений соответственно:', answer[1])


main()
