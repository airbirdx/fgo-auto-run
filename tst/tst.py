# import random
# import datetime
# import time
#
#
# ct = datetime.datetime.now()
#
# cts = int(time.mktime(ct.timetuple()))
#
# random.seed(cts)
# print("Random number with seed 10 : ", random.randint(-10, 10))
# print(datetime.datetime.now())
#
# print(cts)

import cv2
import numpy as np
import random

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


    print(img_gray.shape)
    w1, h1 = img_gray.shape[::-1]
    print(w1, h1)
    x = random.randrange(-300, 300) + (w1 / 2)
    y = random.randrange(-200, 200) + (h1 / 2)

    print(x, y)

    cv2.namedWindow('Detected',0)
    cv2.startWindowThread()
    cv2.imshow('Detected',img_rgb)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


    # self.crd = [x, y]


image=("./tmp/card_2.png")
Target=("./lib/battle/restraint.png")
value=0.85
mathc_img(image,Target,value)
# print('adsdasfdsad')

