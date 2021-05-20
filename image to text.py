from PIL import ImageGrab       # install pillow using pip install 
import cv2                      # install cv2 using pip install 
import numpy as nm              # install numpy using pip install 
import pyautogui as gui         # install pyautogui using pip install 
import keyboard                 # install keyboard using pip install 
import pytesseract as pt        # install pytesseract using pip install and u also need to install google tesseract application using browser  

# creating infinate loop
# to come out of this loop press "q"
# follow the on screen instructions
while True:

    print("move your mouse pointer at left top side of your image and steadily hold and then press ',' button")
    while True:
        if keyboard.is_pressed(',') == True or keyboard.is_pressed('q') == True:
            if keyboard.is_pressed('q') == True:
                quit='q'
            if quit!='q':    
                mpos1=gui.position()
                mpos1=str(mpos1).replace("Point(x=",'')
                mpos1=str(mpos1).replace(" y=",'')
                mpos1=str(mpos1).replace(")",'')
                print(mpos1)
            break
    
    print("move your mouse pointer at right bottom side of your image and steadily hold and then press '.' button")
    while True:
        if keyboard.is_pressed('.') == True or keyboard.is_pressed('q') == True:
            if keyboard.is_pressed('q') == True:
                quit='q'
            if quit!='q':      
                mpos2=gui.position()
                mpos2=str(mpos2).replace("Point(x=",'')
                mpos2=str(mpos2).replace(" y=",'')
                mpos2=str(mpos2).replace(")",'')
                print(mpos2)
            break
    
    if quit=='q':
        break

    #creating co-ordinates of bbox
    #bbox=(int(left),int(top),int(right),int(bottom)
    [left,top]=mpos1.split(",")
    [right,bottom]=mpos2.split(",")
    
    print("wait for few seconds")

    # Path of tesseract executable  
    pt.pytesseract.tesseract_cmd =r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe" # here enter your tesseract path

    # ImageGrab-To capture the screen image in a loop.
    # Bbox used to capture a specific area.

    try:
        #creating capture area
        cap = ImageGrab.grab(bbox=(int(left),int(top),int(right),int(bottom)))
                    
        # Converted the image to monochrome for it to be easily
        # read by the OCR and obtained the output String.
        tesstr = pt.image_to_string(
                        cv2.cvtColor(nm.array(cap), cv2.COLOR_BGR2GRAY),
                        lang ='eng')

        print("<=====================your image grabed text=====================>")
        print(tesstr)
        print("<==============================end===============================>")

    except:
        print("wrong dimension was given")

    
    
 
    








