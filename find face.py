import cv2
import numpy as np

video = cv2.VideoCapture(0)
yuz_bul = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
while True:
    ret,kare = video.read()
    gri_ton = cv2.cvtColor(kare,cv2.COLOR_BGR2GRAY)

    yuzler = yuz_bul.detectMultiScale(gri_ton,1.1,4)

    for(x,y,h,w) in yuzler:
      cv2.rectangle(kare,(x,y),(x+w,y+h),(255,0,0),2)

    cv2.imshow("resimm",kare)
    if cv2.waitKey(25) & 0xFF == ord("q"):
        break


video.release()
cv2.destroyAllWindows()