

import cv2
import numpy as np

def mathc_img(image,Target,value):


    img_rgb = cv2.imread(image)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(Target,0)
    w, h = template.shape[::-1]
    area = template

    # # w, h = im2.shape[::-1]
    # n = 5
    # area = template[h//n:h//n*(n-1), w//n:w//n*(n-1)]  # 裁剪坐标为[y0:y1, x0:x1]
    # # area = template[h // 4:h // 4 * 3, w // 4:w // 4 * 3]  # 裁剪坐标为[y0:y1, x0:x1]
    # w, h = area.shape[::-1]


    print(area.shape)
    print(w, h)
    res = cv2.matchTemplate(img_gray,area,cv2.TM_CCOEFF_NORMED)
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



image =('sh' + '.png')

# yanzuo_lizhuang_manpo

Target=('confirm' + '.png')
value=0.85
mathc_img(image,Target,value)
# print('adsdasfdsad')

