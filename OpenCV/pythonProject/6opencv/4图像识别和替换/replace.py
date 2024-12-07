# 导入OpenCV库，方便调用函数
import cv2
import numpy as np

# 1. 图片输入，将图片读取进来
image_np = cv2.imread('color.png')
print(image_np.shape)  # numpy先高后宽
image_np = cv2.resize(image_np, (500, 500))
cv2.imshow('image_np', image_np)

# 2. 将图片转换为HSV模型下的图片
image_hsv = cv2.cvtColor(image_np, cv2.COLOR_BGR2HSV)

# 3. 制作掩膜
color_lower = np.array([0, 43, 46])  # hsv颜色红色范围min
color_high = np.array([10, 255, 255])  # hsv颜色红色范围max
image_mask = cv2.inRange(image_hsv, color_lower, color_high)

# 4. 开运算(先腐蚀后膨胀)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))  # 矩形3×3的核
image_mask_open = cv2.morphologyEx(image_mask, cv2.MORPH_OPEN, kernel)
# 5. 图片颜色替换
# for i in range(image_mask_open.shape[0]):
#     for j in range(image_mask_open.shape[1]):
#         if image_mask_open[i, j] == 255:
#             image_np[i, j] = (255, 0, 0)
image_np[image_mask_open == 255] = (255, 0, 0)

# 6. 显示结果
cv2.imshow('image_np1', image_np)
cv2.imshow('image_mask_open', image_mask_open)
cv2.waitKey(0)
