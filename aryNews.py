import re
from scrapingHelperFunctions import saveJson, fetchAndFormatArticlesData, fetchLinks, fetchMenuLinks


def aryNews(url, className, fileName):
    saveJson(fetchAndFormatArticlesData(fetchLinks(url, 'h3', className), {'element': 'h2', 'className': 'tdb-title-text test'}, {'element': 'time', 'className': 'entry-date updated td-module-date'}, {
        'element': 'div', 'className': 'tdb-featured-image-bg'}, {'element': 'p', 'className': ''}), f'./news/ARY/{fileName}.json')


def fetchAryNews():
    aryURLs = fetchMenuLinks('https://arynews.tv/', 'ul',
                             'tdb-block-menu tdb-menu tdb-menu-items-visible')

    for i in range(0, len(aryURLs)):
        if(len(aryURLs[i]) >= 10):
            if(i == 0):
                aryNews(aryURLs[i], 'entry-title td-module-title', 'main')
            else:
                aryNews(aryURLs[i], 'entry-title td-module-title', re.sub('/', '', re.sub(r'category/', '', re.sub(
                    r'https://arynews.tv/', '', aryURLs[i]))))
