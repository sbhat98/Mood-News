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

    return tone_analyzer.tone(article.text,
                              content_type="text/plain",  # CHANGE THIS IF CHANGING tone_input
                              sentences=False,
                              content_language='en',
                              accept_language='en')


def get_tone_num(some_json, category):
    # returns a list of urls
    for set in some_json["document_tone"]["tones"]:
        if set["tone_name"] == 'Sadness':
            return set["score"]
    return 0


def get_urls_with_threshold(url_list, category, threshold=0.5):
    return_list = list()
    for url in url_list:
        json_from_url = get_json(url)
        if get_tone_num(json_from_url, category) >= threshold:
            return_list.append(url)
    return return_list


if __name__ == '__main__':
    def p(u):
        print(json.dumps(get_json(u), indent=2))
    a = ['https://www.cnbc.com/2018/03/02/sec-dropped-inquiry-a-month-after-firm-aided-kushner-company.html',
         'http://www.chicagotribune.com/news/local/breaking/ct-james-eric-davis-central-michigan-shooting-20180302-story.html',
         'https://www.washingtonpost.com/news/post-nation/wp/2018/03/02/noreaster-slams-the-east-coast-with-gusting-winds-thousands-lose-power/',
         'http://www.latimes.com/local/lanow/la-me-ln-joshua-tree-couple-20180302-story.html',
         'http://www.latimes.com/business/la-fi-delta-nra-20180302-story.html']
    print(get_urls_with_threshold(a, "Sadness"))
