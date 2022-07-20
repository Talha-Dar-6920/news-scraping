import re
from scrapingHelperFunctions import saveJson, fetchAndFormatArticlesData, fetchLinks, fetchMenuLinks


def geoNews(url, className, fileName):
    saveJson(fetchAndFormatArticlesData(fetchLinks(url, 'div', className), {'element': 'h1', 'className': ''}, {'element': 'p', 'className': 'post-date-time'}, {
             'element': 'div', 'className': 'medium-insert-images ui-sortable'}, {'element': 'p', 'className': ''}), f'./news/GEO/{fileName}.json')


def fetchGeoNews():
    geoURLs = fetchMenuLinks('https://www.geo.tv/', 'ul',
                             'menu')

    for i in range(1, len(geoURLs)):
        if(len(geoURLs[i]) > 10):
            if(i == 1):
                geoNews(geoURLs[i], 'heading', 'main')
            else:
                geoNews(geoURLs[i], 'list', re.sub('/', '', re.sub(r'category/', '', re.sub(
                    r'https://www.geo.tv/', '', geoURLs[i]))))
