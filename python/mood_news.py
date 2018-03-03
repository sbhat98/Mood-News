import news_reader as bt
import Parser


def get_happy_articles():
    a = Parser.get_urls_with_threshold(bt.overall(), "Joy", threshold=0.55)
    b = list()
    if len(a) < 5:
        b = Parser.get_urls_with_threshold(bt.sports(), "Joy")
    return __merge_lists(a, b)[:5]


def get_sad_articles():
    a = Parser.get_urls_with_threshold(bt.overall(), "Sadness")
    b = list()
    if len(a) < 5:
        b = Parser.get_urls_with_threshold(bt.business(), "Sadness")
    return __merge_lists(a, b)[:5]


def get_angry_articles():
    a = Parser.get_urls_with_threshold(bt.overall(), "Anger")
    b = list()
    if len(a) < 5:
        b = Parser.get_urls_with_threshold(bt.business(), "Anger")
    return __merge_lists(a, b)[:5]


def get_fear_articles():
    a = Parser.get_urls_with_threshold(bt.overall(), "Fear")
    b = list()
    if len(a) < 5:
        b = Parser.get_urls_with_threshold(bt.business(), "Fear")
    return __merge_lists(a, b)[:5]


def get_curious_articles():
    a = Parser.get_urls_with_threshold(bt.overall(), "Analytical")
    b = list()
    if len(a) < 5:
        b = Parser.get_urls_with_threshold(bt.business(), "Analytical")
    return __merge_lists(a, b)[:5]


def get_article_image(url):
    from newspaper import Article
    a = Article(url)
    a.download()
    a.parse()
    return a.top_image


def __merge_lists(list_a, list_b):
    for x in list_b:
        if x not in list_a:
            list_a.append(x)
    return list_a


if __name__ == '__main__':
    print(get_curious_articles())