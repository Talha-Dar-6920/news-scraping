from bs4 import BeautifulSoup as bs
import json
import requests


def saveJson(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f)


def fetchHtmlAndParse(url):
    html = requests.get(url, headers={'User-Agent': '*/*'})
    return bs(html.content, 'html.parser')


def removeUnicode(text):
    return text.encode('ascii', 'ignore').decode().replace('\"', '')


def fetchAndFormatArticlesData(urls, title, time, image, description):
    articles = []

    for article in urls:
        bsObj = fetchHtmlAndParse(article)
        temp = {
            'title': '', 'image': '', 'date': '', 'data': ''
        }

        for content in bsObj.find_all(title['element'], class_=title['className']):
            temp['title'] = removeUnicode(content.text)

        for date in bsObj.find_all(time['element'], class_=time['className']):
            temp['date'] = date.text.replace('\n', '')

        for source in bsObj.find_all(image['element'], class_=image['className']):
            if(source.img != None):
                temp['image'] = source.img.get('src')
            else:
                temp['image'] = 'No Image Found'

        for content in bsObj.find_all(description['element'], class_=description['className']):
            if (content.text != None):
                temp['data'] = temp['data'] + removeUnicode(content.text)

        articles.append(temp)

    return articles


def fetchLinks(url, element, className):
    bsObj = fetchHtmlAndParse(url)
    links = []

    for link in bsObj.find_all(element, class_=className):
        if(link.a != None):
            links.append(link.a.get('href'))

    return links


def fetchMenuLinks(url, element, className):
    bsObj = fetchHtmlAndParse(url)
    links = []

    list = bsObj.find(element, class_=className)

    for item in list.find_all('li'):
        if(item.a != None):
            links.append(item.a.get('href'))

    return links
