import bing_test as bt
import Parser


def get_happy_articles():
    a = Parser.get_urls_with_threshold(bt.overall(), "Joy")
    if len(a) < 5:
        b = Parser.get_urls_with_threshold(bt.health(), "Joy", 5 - len(a))


def get_sad_articles():
    return Parser.get_urls_with_threshold(bt.overall(), "Sadness")


def get_angry_articles():
    return Parser.get_urls_with_threshold(bt.overall(), "Anger")


def get_fear_articles():
    return Parser.get_urls_with_threshold(bt.overall(), "Fear")


def get_curious_articles():
    return Parser.get_urls_with_threshold(bt.overall(), "Analytical")

def