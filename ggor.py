import numpy as np
import cv2

resim_1 = cv2.imread("hmy.jpg")
resim_gri = cv2.cvtColor(resim_1,cv2.COLOR_BGR2GRAY)

koseler = cv2.goodFeaturesToTrack(resim_gri,50,0.01,10)


for kose in koseler:
    x,y = kose.ravel()
    cv2.circle(resim_1,(x,y),3,(255,0,0),-1)
    print(koseler)


cv2.imshow("resmim",resim_1)
cv2.waitKey(0)
cv2.destroyAllWindows()