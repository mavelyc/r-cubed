import cv2
import json
from ibm_watson import VisualRecognitionV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from menu import make_menu
from start import start_camera

def main():
    #start_camera()
    make_menu()

    
    
if __name__ == "__main__":
    main()