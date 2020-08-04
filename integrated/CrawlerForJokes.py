def extractJoke():
    import requests
    import bs4
    url = 'http://jokes.cc.com/'
    #print(url)
    # read the page
    try:
        response = requests.get(url)
    except (requests.exceptions.MissingSchema,
            requests.exceptions.InvalidSchema):
        print("*FAILED*:", url)
        return
    if not response.headers['content-type'].startswith('text/html'):
        print("not html. skipping..")

    soup = bs4.BeautifulSoup(response.text, "html.parser")
    return soup.body.find_all('span', attrs={'class':'fulltext'})[0].text


def extractMeme():
    import requests
    import bs4
    url = 'https://memebase.cheezburger.com/'
    #print(url)
    # read the page
    try:
        response = requests.get(url)
    except (requests.exceptions.MissingSchema,
            requests.exceptions.InvalidSchema):
        print("*FAILED*:", url)
        return
    if not response.headers['content-type'].startswith('text/html'):
        print("not html. skipping..")

    soup = bs4.BeautifulSoup(response.text, "html.parser")
    return soup.body.find_all('div', attrs={'class':'resp-media-wrap'})[0].find_all('img', attrs={'class':'resp-media'})[0].get('src')
