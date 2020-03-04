import cv2
import json
import configparser
from ibm_watson import VisualRecognitionV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from tkinter import *
from PIL import ImageTk, Image
#from menu import make_menu

config = configparser.RawConfigParser()
config.read('config.properties')

ss_fps = int(config.get('API', 'ss_fps'))
api_key = config.get('API', 'vr_key')
api_url = config.get('API', 'vr_url')

def parse_json(json):
    score = 0
    category = ""
    probabilities = json["images"][0]["classifiers"][0]["classes"]
    if len(probabilities) == 0:
        print("human")
    elif len(probabilities) > 1:
        for obj in probabilities:
            if obj['score'] > score:
                score = obj['score']
                category = obj['class']
    else:
        score = probabilities[0]['score']
        category = probabilities[0]['class']

    print(category, score)
    return category


def start_camera():

    m=Tk()
    m.title('R-cubed')
    
    m.attributes("-fullscreen", True)


    screen_w = m.winfo_screenwidth()
    screen_h = m.winfo_screenheight()


    top_frame = Frame(m)

    label = Label(top_frame, text='Let us organize your waste!', font=("Helvetica", 30), bg='limegreen')
    label.pack(fill=X)
    top_frame.pack(fill=X)

    img = ImageTk.PhotoImage(Image.open("recycle_vs_organic.jpg").resize(
        (screen_w, screen_h - 250), Image.ANTIALIAS))
    img_panel = Label(m, image = img)
    img_panel.pack(fill = X, expand = "yes")

    windowName = "Live Video Feed"
    cv2.namedWindow(windowName)
    cap = cv2.VideoCapture(0)
    count = 0
    flag = 0
    
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

            visual_recognition.set_service_url(api_url)

            with open('./frame.jpg', 'rb') as image:
                classes = visual_recognition.classify(
                    images_file=image,
                    threshold='0.6',
                    classifier_ids='DefaultCustomModel_663415636').get_result()
                category = parse_json(classes)

                if category == 'Organic':
                    img = ImageTk.PhotoImage(Image.open("organic.png").resize(
                        (int(screen_w/2.5), screen_h - 250), Image.ANTIALIAS))
                    img_panel.configure(image=img)
                    img_panel.image = img
                elif category == 'Recyclable':
                    img = ImageTk.PhotoImage(Image.open("recyclable.png").resize(
                        (int(screen_w/2.5), screen_h - 250), Image.ANTIALIAS))   
                    img_panel.configure(image=img)
                    img_panel.image = img
                elif category == 'Garbage':
                    img = ImageTk.PhotoImage(Image.open("garbage.png").resize(
                        (int(screen_w/2.5), screen_h - 250), Image.ANTIALIAS))   
                    img_panel.configure(image=img)
                    img_panel.image = img
                m.update()
        
        cv2.imshow("Original Webcam Feed", frame)
        
        if cv2.waitKey(1) == 27: # exit on ESC
            break

        flag += 1
        flag = flag%ss_fps

    cv2.destroyAllWindows()
    cap.release()
    m.mainloop()
    
#make_menu()