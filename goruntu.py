import cv2
import numpy as np

kamera = cv2.VideoCapture(0)

dusuk = np.array([90,50,50])
yuksek = np.array([130,255,255])

while True:
    ret,video = kamera.read()
    hsv = cv2.cvtColor(video,cv2.COLOR_BGR2HSV)
    son = cv2.inRange(hsv,dusuk,yuksek)
    mask = cv2.bitwise_and(hsv,hsv,mask = son)

    cv2.imshow("goruntum",video)
    cv2.imshow("ayıtrt edici",son)

    if cv2.waitKey(25) & 0xFF == ord("q"):
        break

kamera.release()
cv2.destroyAllWindows()