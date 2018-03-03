import requests


def general():
    url = ('https://newsapi.org/v2/top-headlines?'
           'country=us&'
           'category=general&'
           'apiKey=f3b01ca524d746819e1be1936466410c')
    response = requests.get(url)
    rep = response.json()
    x = rep.get("articles")
    y = []
    for urls in x:
        y.append(urls.get("url"))
    return y


def business():
    url = ('https://newsapi.org/v2/top-headlines?'
           'country=us&'
           'category=business&'
           'apiKey=f3b01ca524d746819e1be1936466410c')
    response = requests.get(url)
    rep = response.json()
    x = rep.get("articles")
    y = []
    for urls in x:
        y.append(urls.get("url"))
    return y


def entertainment():
    url = ('https://newsapi.org/v2/top-headlines?'
           'country=us&'
           'category=entertainment&'
           'apiKey=f3b01ca524d746819e1be1936466410c')
    response = requests.get(url)
    rep = response.json()
    x = rep.get("articles")
    y = []
    for urls in x:
        y.append(urls.get("url"))
    return y


def health():
    url = ('https://newsapi.org/v2/top-headlines?'
           'country=us&'
           'category=health&'
           'apiKey=f3b01ca524d746819e1be1936466410c')
    response = requests.get(url)
    rep = response.json()
    x = rep.get("articles")
    y = []
    for urls in x:
        y.append(urls.get("url"))
    return y


def science():
    url = ('https://newsapi.org/v2/top-headlines?'
           'country=us&'
           'category=science&'
           'apiKey=f3b01ca524d746819e1be1936466410c')
    response = requests.get(url)
    rep = response.json()
    x = rep.get("articles")
    y = []
    for urls in x:
        y.append(urls.get("url"))
    return y


def sports():
    url = ('https://newsapi.org/v2/top-headlines?'
           'country=us&'
           'category=sports&'
           'apiKey=f3b01ca524d746819e1be1936466410c')
    response = requests.get(url)
    rep = response.json()
    x = rep.get("articles")
    y = []
    for urls in x:
        y.append(urls.get("url"))
    return y


def technology():
    url = ('https://newsapi.org/v2/top-headlines?'
           'country=us&'
           'category=sports&'
           'apiKey=f3b01ca524d746819e1be1936466410c')
    response = requests.get(url)
    rep = response.json()
    x = rep.get("articles")
    y = []
    for urls in x:
        y.append(urls.get("url"))
    return y


def overall():
    url = ('https://newsapi.org/v2/top-headlines?'
           'country=us&'
           'apiKey=f3b01ca524d746819e1be1936466410c')
    response = requests.get(url)
    rep = response.json()
    x = rep.get("articles")
    y = []
    for urls in x:
        y.append(urls.get("url"))
    return y
