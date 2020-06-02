# R-cubed

Our application is R-cubed, and our goal is to integrate proper recycling habits into people’s lives.
R-cubed would serve as a waste management assistant that can fit seamlessly into your daily life.

## Overview
In a video feed, our application captures a frame and classifies the object in that frame as organic or recyclable.

![image](https://user-images.githubusercontent.com/46586499/83578634-44729180-a505-11ea-914e-9dd494f615b8.png)


![image](https://user-images.githubusercontent.com/46586499/83578664-5c4a1580-a505-11ea-9ac9-5b8031e75b3a.png)

## IBM Watson

To build our application, we used IBM Watson’s [Visual Recognition API](https://cloud.ibm.com/catalog/services/visual-recognition) and [Text-to-speech API](https://cloud.ibm.com/apidocs/text-to-speech).
We used the Text-to-Speech API to verbally say the resulting category out loud, for an easier user experience.

### Visual Recognition
Instead of using IBM Watson’s default Visual Recognition model, we created our own custom model.
We created a custom class for the Organic category, and a custom class for the Recyclable category.

We also used a Negative class in our model. Images in the negative class are used when the objects do not fall under any of the positive classes (which are the Organic and Recyclable classes). So we put humans under the Negative class, as they are the most likely ones to be captured in the video, alongside the object that they are holding in front of the camera to throw out. So, whenever a human is in the frame, the application does not categorize them and only identifies other objects as organic or recyclable. 

## Required Python libraries
```
pip3 install opencv-python-headless
pip3 install matplotlib
pip3 install --upgrade "ibm-watson>=4.0.1"
pip3 install image
pip3 install imutils
pip3 install playsound
pip3 install pyobjc
```
