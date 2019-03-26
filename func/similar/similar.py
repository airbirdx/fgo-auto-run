
import cv2
from util.cvs import analyze
from func.similar.histogram import classfiy_histogram
from func.similar.histogram2 import classfiy_histogram_with_split
from func.similar.aHash import classfiy_aHash
from func.similar.dHash import classfiy_dHash
from func.similar.pHash import classify_DCT


def similar_image(im1, im2):

	res1 = classfiy_histogram(im1, im2)
	res2 = classfiy_histogram_with_split(im1, im2)
	res3 = classfiy_aHash(im1, im2)
	res4 = classfiy_dHash(im1, im2)
	res5 = classify_DCT(im1, im2)

	print('[%.2f, %.2f' % (res1, res2), res3, '%4d, %4d]' % (res4, res5))

	b1 = bool(res1 > 0.55)
	b2 = bool(res2 > 0.7)
	b3 = res3
	b4 = bool(res4 < 20)
	b5 = bool(res5 < 10)

	res = bool((b1 + b2 + b3 + b4 + b5) >= 3)

	return res


def similar_image2(file1, file2):
	im1 = cv2.imread(file1, 0)
	im2 = cv2.imread(file2, 0)

	w, h = im2.shape[::-1]
	n = 5
	area = im2[h // n:h // n * (n - 1), w // n:w // n * (n - 1)]  # 裁剪坐标为[y0:y1, x0:x1]

	thd = 0.9
	if analyze(im1, area, thd):
		return True
	else:
		return False
