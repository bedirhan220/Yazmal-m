import cv2
import numpy as np

kamera = cv2.VideoCapture(0)

while True:
    ret,kare= kamera.read()
    gri_kare = cv2.cvtColor(kare,cv2.COLOR_BGR2GRAY)
    nesne = cv2.imread("bardak.png",0)
    w,h = nesne.shape

    tarama = cv2.matchTemplate(gri_kare,nesne,cv2.TM_CCOEFF_NORMED)

    esik = 0.8

    loc = np.where(tarama > esik)
    for n in zip(*loc[::-1]):
        cv2.rectangle(kare,n,(n[0]+h,n[1]+w),(0,255,255),2)

    cv2.imshow("gorntumyum",kare)

    if cv2.waitKey(25) & 0xFF == ord("q"):
        break

kamera.release()
cv2.destroyAllWindows()