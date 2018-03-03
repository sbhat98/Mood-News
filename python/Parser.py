import json
from watson_developer_cloud import ToneAnalyzerV3
from newspaper import Article


def get_json(url):
    tone_analyzer = ToneAnalyzerV3(
        username='6e9d0618-f7c3-4475-b0a9-05cbf221b341',
        password='auet7FNIoLwZ',
        version='2017-09-26')

    article = Article(url)
    article.download()
    article.parse()
    if len(article.text) < 20:
        return None
    return tone_analyzer.tone(article.text,
                              content_type="text/plain",  # CHANGE THIS IF CHANGING tone_input
                              sentences=False,
                              content_language='en',
                              accept_language='en')


def get_tone_num(some_json, category):
    # returns a list of urls
    for s in some_json["document_tone"]["tones"]:
        if s["tone_name"] == category:
            return s["score"]
    return 0


def get_urls_with_threshold(url_list, category, threshold=0.5, num_articles=5):
    return_list = list()
    i = 0
    for url in url_list:
        json_from_url = get_json(url)
        if json_from_url is None:
            continue
        if get_tone_num(json_from_url, category) >= threshold:
            return_list.append(url)
            i = i + 1
            if i == num_articles:
                return return_list
    return return_list


if __name__ == '__main__':
    a = Article('http://www.bellinghamherald.com/news/article203293519.html')
    a.download()
    a.parse()
    print(a.text)