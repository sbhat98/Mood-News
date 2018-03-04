from newspaper import Article
import json
import unidecode
import mood_news


def homepage():
    return "Hi"


def start_skill():
    welcome_message = "Hello, how are you feeling today?"
    return welcome_message


def share_anger():
    # urls = mood_news.get_angry_articles()
    # headlines = list()
    # for u in urls:
    #     a = Article(u)
    #     a.download()
    #     a.parse()
    #     headlines.append(a.title)
    # headlines = " ... ".join(headlines)
    # out_message = 'Here are some headlines from today that may be related to that feeling: {}'.format(headlines)
    # out_message = unidecode.unidecode(out_message)
    out_message = "this is a test message"
    return out_message


def none_intent():
    out = "Sorry. I don't seem to understand that feeling quite yet. Maybe one day I'll be able to feel like you."
    return out
