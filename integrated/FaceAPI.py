def retrieve_image_data(img_url='face_emo.jpg'):
    import cognitive_face as CF
    KEY = '57a0d5cba06246aab57b9b2bda34f596'  # Replace with a valid Subscription Key here.
    CF.Key.set(KEY)
    BASE_URL = 'https://southeastasia.api.cognitive.microsoft.com/face/v1.0'  # Replace with your regional Base URL
    CF.BaseUrl.set(BASE_URL)
    #img_url = 'https://raw.githubusercontent.com/Microsoft/Cognitive-Face-Windows/master/Data/detection1.jpg'
    #img_url = os.path.join('D:\hackathon csefest2019\face_emo.jpg')
    result = CF.face.detect(img_url,face_id=True,landmarks=True, attributes='smile,emotion,age,gender')
    #print(result)
    return result

def capture_image(img_url='face_emo.jpg'):
    import cv2
    camera = cv2.VideoCapture(0)
    range_limit = 1
    for i in range(range_limit):
        return_value, image = camera.read()
        #cv2.imwrite('opencv'+str(i)+'.png', image)
        cv2.imwrite(img_url, image)
    del(camera)
    return img_url

def emo_detector(img_url = 'face_emo.jpg'):
    #capture_image(img_url=img_url)
    return retrieve_image_data(img_url=img_url)

def face_attributes():
    return emo_detector()[0]['faceAttributes']

