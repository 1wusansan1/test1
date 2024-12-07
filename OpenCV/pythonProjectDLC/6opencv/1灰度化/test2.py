# 使用numpy库来创建三维数组
import numpy as np

# 使用OpenCV库来进行查看图像及其他操作
import cv2

# 使用matplotlib库来一次性展示多个图像
import matplotlib.pyplot as plt

# 创建一个700 * 700 的三维数组（彩色图）
# 使用np.zeros创建一个数值全为0的数组，对应一张黑色图
# uint8: unsigned int 无符号整数 0-255
image = np.zeros((700, 700, 3), dtype=np.uint8)
# 用来代表分割出来的矩形的大小
block_size = 100

for i in range(0, 700, block_size):
    # 使用j来代表每一列
    for j in range(0, 700, block_size):
        # i的取值：0，100，200，300，400，500，600
        # j的取值：0，100，200，300，400，500，600
        # 使用三维数组切片修改的方式去修改像素值
        # 对每一行来说，需要选中的是第i行里的所有像素
        image[i, :, :] = (255, 255, 255)
        image[:, j, :] = (255, 255, 255)
        #
        # # 根据观察图像所得，i和j的取值都不能为0和600
        if i != 0 and j != 0 and i != 600 and j != 600 and (i == j or i + j == 600):
            #     # 在OpenCV中，颜色的顺序是BGR
            image[i:i + block_size, j:j + block_size, :] = (0, 0, 255)
cv2.imshow('image', image)
cv2.waitKey(3000)
