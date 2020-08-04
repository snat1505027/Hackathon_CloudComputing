import requests
import bs4

def url_in_list(url, listobj):
    """Determine whether a URL is in a list of URLs.
    This function checks whether the URL is contained in the list with either
    an http:// or https:// prefix. It is used to avoid crawling the same
    page separately as http and https.
    """
    http_version = url.replace('https://', 'http://')
    https_version = url.replace('http://', 'https://')
    return (http_version in listobj) or (https_version in listobj)


def find_title_and_artist(soup, base_title, base_url='https://www.lyrics.com', base_artist=None):
    temp = soup.body.find_all('div', attrs={'class':'sec-lyric clearfix'})
    #print(temp)
    for t in temp:
        base = t.find_all('div', attrs={'class':'lyric-meta within-lyrics'})[0]
        title = base.find('p', attrs={'class':'lyric-meta-title'}).text
        artist = base.find('p', attrs={'class':'lyric-meta-artists'}).text
        link = base.find('p', attrs={'class':'lyric-meta-title'}).a.get('href')
        link = base_url + link
        #print(title, " -- " ,base_title)
        if base_artist is not None:
            if base_artist.lower() != artist.lower():
                print(base_artist)
                continue
        if title.lower() == base_title.lower():
            print(title," ", artist, " ", link )
            return [title, artist, link]



def find_lyrics_title_artist(keyword, base_artist=None):
    url = 'https://www.lyrics.com/lyrics/'+keyword.replace(" ", "%20")
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
        return
    soup = bs4.BeautifulSoup(response.text, "html.parser")
    try:
        title, artist, link = find_title_and_artist(soup, base_title=keyword, base_artist=base_artist)
    except:
        return
    lyrics = find_lyric(link)
    return [title, artist, link, lyrics]


def find_lyric(link):
    response = requests.get(link)
    if not response.headers['content-type'].startswith('text/html'):
        print("not html. skipping..")
        #return
    soup = bs4.BeautifulSoup(response.text, "html.parser")
    lyrics = soup.body.pre.text.replace("\r\n",' \n')
    #print(lyrics)
    return lyrics