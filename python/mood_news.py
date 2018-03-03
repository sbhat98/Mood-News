import bing_test as bt
import Parser


def get_happy_articles():
    a = Parser.get_urls_with_threshold(bt.overall(), "Joy")
    b = set()
    if len(a) < 5:
        b = Parser.get_urls_with_threshold(bt.health(), "Joy", 5 - len(a))
    return set(a).union(b)


def get_sad_articles():
    a = Parser.get_urls_with_threshold(bt.overall(), "Sadness")
    b = set()
    if len(a) < 5:
        b = Parser.get_urls_with_threshold(bt.business(), "Sadness", 5 - len(a))
    return set(a).union(b)


def get_angry_articles():
    a = Parser.get_urls_with_threshold(bt.overall(), "Anger")
    b = set()
    if len(a) < 5:
        b = Parser.get_urls_with_threshold(bt.business(), "Anger", 5 - len(a))
    return set(a).union(b)


def get_fear_articles():
    a = Parser.get_urls_with_threshold(bt.overall(), "Fear")
    b = set()
    if len(a) < 5:
        b = Parser.get_urls_with_threshold(bt.business(), "Fear", 5 - len(a))
    return set(a).union(b)


def get_curious_articles():
    a = Parser.get_urls_with_threshold(bt.overall(), "Analytical")
    b = set()
    if len(a) < 5:
        b = Parser.get_urls_with_threshold(bt.business(), "Analytical", 5 - len(a))
    return set(a).union(b)


def get_article_image(url):
    from newspaper import Article
    a = Article(url)
    a.download()
    a.parse()
    return a.top_image
