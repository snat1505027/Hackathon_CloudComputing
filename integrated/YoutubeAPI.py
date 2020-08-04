def youtube_search_by_word(option, maxR=5):
    from apiclient.discovery import build

    DEVELOPER_KEY = 'AIzaSyDxj1aDZcbvNLbG4vjOAfZuCZoLy5FHly4'
    YOUTUBE_API_SERVICE_NAME = 'youtube'
    YOUTUBE_API_VERSION = 'v3'

    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                    developerKey=DEVELOPER_KEY)

    # Call the search.list method to retrieve results matching the specified
    # query term.
    option = option+" song"
    search_response = youtube.search().list(part='snippet', q=option, maxResults=maxR, type='song').execute()
    i = 1
    strURL = "https://www.youtube.com/watch?v="
    list = []
    dict = {}
    print(option)
    print()
    for i in range(maxR):
        # print(strURL+search_response['items'][i]['id']['videoId'])
        try:
            print(strURL + search_response['items'][i]['id']['videoId'])
            list.append(strURL + search_response['items'][i]['id']['videoId'])
            dict.update(
                {search_response['items'][i]['snippet']['title']: strURL + search_response['items'][i]['id']['videoId']})
        except:
            i-=1
            continue
    return dict


def getLatLong(ip):
    import geocoder
    g = geocoder.ip(ip)
    return g.latlng


def youtube_search_by_loaction(option, ip, radius, maxS):
    """
    option='sad'
    ip='199.7.157.0'
    radius='5km'
    maxS=5 
    """
    from apiclient.discovery import build
    DEVELOPER_KEY = 'AIzaSyAiqn6NGZ-_GSTFiNEi43oitT-P9c_NpvM'
    YOUTUBE_API_SERVICE_NAME = 'youtube'
    YOUTUBE_API_VERSION = 'v3'

    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                    developerKey=DEVELOPER_KEY)

    # Call the search.list method to retrieve results matching the specified
    # query term.
    latlong = ""
    latlong = latlong + str(getLatLong(ip)[0])
    latlong = latlong + ","
    latlong = latlong + str(getLatLong(ip)[1])

    search_response = youtube.search().list(
        q=option,
        type="video",
        location=latlong,
        locationRadius=radius,
        part="id,snippet",
        maxResults=maxS
    ).execute()

    i = 1
    strURL = "https://www.youtube.com/watch?v="
    list = []
    for i in range(maxS):
        # print(strURL+search_response['items'][i]['id']['videoId'])
        list.append(strURL + search_response['items'][i]['id']['videoId'])
    return list
    # return search_response