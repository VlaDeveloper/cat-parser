import requests
from bs4 import BeautifulSoup as BS

wiki_url = 'https://ru.wikipedia.org/wiki/'

def get_wiki_definition(word = "Кошка"):
    try:
        r = requests.get(wiki_url + word)
        html = BS(r.content, 'html.parser')
        myStr = ''

        for img in html.find_all('img'):
            if (img['src'].find('.jpg') != -1):
                myStr += img['src'] + '\n'
        return myStr
    except ( AttributeError, ConnectionError) as e:
        import sys
        print(word, e, file = sys.stderr)
        return ""

print(get_wiki_definition())