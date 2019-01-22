import numpy as np
import pytesseract
from mss import mss

import cv2
chat = []


def process_img(image):
    processed_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # edge detection
    img = cv2.Canny(processed_img, threshold1=200, threshold2=300)
    return img


def run():
    while True:
        sct = mss()
        monitor = {"top": 469, "left": 13, "width": 485, "height": 17}
        img = np.array(sct.grab(monitor))
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        image = cv2.adaptiveThreshold(
            gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
            cv2.THRESH_BINARY, 11, 15)
            
        result = pytesseract.image_to_string(image)
        compare1(str(result))
        cv2.imshow('image', image)
        if cv2.waitKey(25) & 0xFF == ord("q"):
            cv2.destroyAllWindows()
            break


def compare1(text):
    if chat:
        if text != chat[-1]:
            chat.append(text)
            print(chat[-1])


run()
