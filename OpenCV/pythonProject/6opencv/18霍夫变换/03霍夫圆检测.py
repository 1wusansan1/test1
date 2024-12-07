import cv2
import numpy as np

if __name__ == "__main__":
    path = "./demo.png"
    image_np = cv2.imread(path)
    image_shape = image_np.shape
    # 转为灰度图
    image_np_gray = cv2.cvtColor(image_np, cv2.COLOR_BGR2GRAY)
    drawing = np.zeros(image_shape, dtype=np.uint8)
    # 统计概率霍夫直线变换（统计的是线段）,
    # 1. cv2.HOUGH_GRADIENT三维圆锥
    # dp = 1.5累加器分辨率
    # param1=70：canny边缘检测的高阈值，所以不用提前进行canny边缘检测，他内部会进行运算
    # param2=50：累加器阈值
    # circles = cv2.HoughCircles(image_np_gray, cv2.HOUGH_GRADIENT, 1, 20, param1=70, param2=30)
    # 2. cv2.HOUGH_GRADIENT_ALT霍夫梯度法
    circles = cv2.HoughCircles(image_np_gray, cv2.HOUGH_GRADIENT_ALT, 1, 10, param1=300, param2=0.85)
    circles = np.int32(np.around(circles))
    for circle in circles:
        x, y, radius = circle[0]
        cv2.circle(drawing, (x, y), radius, (0, 0, 255), 2)
    # 返回处理正确后的内容
    cv2.imshow("drawing", drawing)
    cv2.waitKey(0)
