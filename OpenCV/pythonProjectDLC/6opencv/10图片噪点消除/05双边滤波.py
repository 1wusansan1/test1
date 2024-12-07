# 导入OpenCV的库
import cv2

# 1. 读取要滤波的图像
image_np = cv2.imread('./11.jpg')
image_np = cv2.resize(image_np, (500, 500))
# 2. 直接进行双边滤波
# sigmaColor:像素值 ，sigmaSpace:像素位置
image_bil = cv2.bilateralFilter(image_np, 7, 100, 100)

cv2.imshow('image_np', image_np)
cv2.imshow('image_bil', image_bil)
cv2.waitKey(0)

