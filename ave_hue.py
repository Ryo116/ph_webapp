import numpy as np
import matplotlib.pyplot as plt
import cv2
import sys
from collections import Counter
from statistics import mean

# 画像を読み込み
# python ave_hue.py ImageFile_name
argv = sys.argv
filename = argv[1]
img = cv2.imread(filename)
img_scr = cv2.imread(filename)
# BGR->HSV に変換
img_hsv = cv2.cvtColor(img_scr, cv2.COLOR_BGR2HSV)

height = img_hsv.shape[0]
width = img_hsv.shape[1]

pixels = []
saturation = []

for y in range(height):
    for x in range(width):
        if (img_hsv[y, x, 1] > 45 and 35 < img_hsv[y, x, 2]):
            pixels.append(img_hsv[y, x, 0])
            saturation.append(img_hsv[y, x, 1])

plt.xlim(0, 180)
plt.xticks([0, 15, 30, 45, 60, 75, 90, 105, 120, 135, 150, 165, 180])
plt.hist(pixels, bins=24, range=(0, 180), align="mid", rwidth=1.0, color="blue")

bins = np.linspace(0, 180, 25)
# print(bins)
index = np.digitize(pixels, bins)
c = Counter(index)
# print(c)
mode = c.most_common(1)
print(mode[0][0])
# 以下彩度表示
saturation_average = mean(saturation)
print('Saturaion Average:' + str(saturation_average))
# 効果判定
if mode[0][0] == 16 and int(saturation_average) > 65:
    print("Effective")
else:
    print("No Effect")
plt.show()
