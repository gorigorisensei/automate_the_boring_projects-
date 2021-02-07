import bs4, requests

def getSomethingFromWeb(Url):
    res = requests.get(Url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('div#myModal')
    return elems[0].text.strip()


extracted_data = getSomethingFromWeb('http://testhtml5.vulnweb.com/#/popular')
print('We extracted ' + extracted_data )
