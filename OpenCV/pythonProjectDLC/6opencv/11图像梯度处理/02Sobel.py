# 导入OpenCV库
import cv2
import numpy as np

# 1. 图像输入
image_np = cv2.imread('./test.png')

# 灰度化
image_np = cv2.cvtColor(image_np, cv2.COLOR_BGR2GRAY)
# 注意：如果是单通道图时（例如灰度图），进行梯度处理的时候如果卷积运算减出来负数会强制置为0，就会丢失部分边缘细节
# 2. 进行卷积运算
image_Sobel = cv2.Sobel(image_np, -1, 1, 0)


# 3. 图像显示
cv2.imshow('image_np', image_np)
cv2.imshow('image_Sobel', image_Sobel)
cv2.waitKey(0)

