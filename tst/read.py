import os
import time


def get_sh(rotation=0, index=0):
    os.system('adb shell screencap -p /sdcard/tst.png')
    os.system('adb pull /sdcard/tst.png ./sh/sh_' + f'{index}.png')
    # inv-clockwise dir
    if rotation:
        img = cv2.imread(screenshot_path, 1)  # 1 is color, 0 is gray
        for i in range(rotation):
            img = np.rot90(img)
        cv2.imwrite(screenshot_path, img)
    time.sleep(1)





i = 0
while True:
    get_sh(rotation=0, index=i)
    i += 1






