#!/usr/bin/python3
import numpy as np
import cv2
from pyzbar import pyzbar

cap = cv2.VideoCapture(1)
#w = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
#h = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
#print(w,h)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 2304)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1536)
ret,frame = cap.read()
print(frame.shape)

while(cap.isOpened()):
    ret, image = cap.read()

    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    barcodes = pyzbar.decode(image)
    
    # loop over the detected barcodes
    for barcode in barcodes:
        # extract the bounding box location of the barcode and draw the
        # bounding box surrounding the barcode on the image
        (x, y, w, h) = barcode.rect
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
        # the barcode data is a bytes object so if we want to draw it on
        # our output image we need to convert it to a string first
        barcodeData = barcode.data.decode("utf-8")
        barcodeType = barcode.type
        # draw the barcode data and barcode type on the image
        text = "{} ({})".format(barcodeData, barcodeType)
        cv2.putText(image, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
            0.5, (0, 0, 255), 2)
        # print the barcode type and data to the terminal
        print("[INFO] Found {} barcode: {}".format(barcodeType, barcodeData))
    
    cv2.imshow('image',image)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
#print("ret", ret)
cap.release()
cv2.destroyAllWindows()
