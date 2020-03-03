import cv2
import json
from ibm_watson import VisualRecognitionV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

def start_camera():

    windowName = "Live Video Feed"
    cv2.namedWindow(windowName)
    cap = cv2.VideoCapture(0)
    count = 0
    flag = 0

    with open ("apikey", "r") as apikey_file:
        api_key=apikey_file.readlines()[0]
    
    if cap.isOpened():
        ret, frame = cap.read()
    else:
        ret = False

    while ret:

        ret, frame = cap.read()

        cv2.imwrite("frame.jpg", frame)     # save frame as JPEG file      
        
        #output = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        if flag == 0:
            authenticator = IAMAuthenticator(api_key)
            visual_recognition = VisualRecognitionV3(
                version='2018-03-19',
                authenticator=authenticator
            )

            visual_recognition.set_service_url('https://api.us-south.visual-recognition.watson.cloud.ibm.com/instances/d9ed5d97-8d20-4f96-8fc7-ad2b4e337061')

            with open('./frame.jpg', 'rb') as image:
                classes = visual_recognition.classify(
                    images_file=image,
                    threshold='0.6',
                    ).get_result()
                print(json.dumps(classes, indent=2))

        
        cv2.imshow("Original Webcam Feed", frame)
        
        if cv2.waitKey(1) == 27: # exit on ESC
            break

        flag += 1
        flag = flag%30

    cv2.destroyAllWindows()
    cap.release()
    