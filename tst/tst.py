

import cv2
import numpy as np

def mathc_img(image,Target,value):


    img_rgb = cv2.imread(image)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(Target,0)
    w, h = template.shape[::-1]
    print(template.shape)
    print(w, h)
    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
    threshold = value
    loc = np.where( res >= threshold)
    pos = []
    for pt in zip(*loc[::-1]):
        print(pt)
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (7,249,151), 2)
        pos.append(pt)

    print(pos) # location


    cv2.namedWindow('Detected',0)
    cv2.startWindowThread()
    cv2.imshow('Detected',img_rgb)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



image =('meilin1' + '.png')

# yanzuo_lizhuang_manpo

Target=('manpo0' + '.png')
value=0.85
mathc_img(image,Target,value)
# print('adsdasfdsad')

