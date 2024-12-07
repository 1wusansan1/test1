import cv2
import numpy as np

if __name__ == "__main__":
    path = "./demo.png"
    image_np = cv2.imread(path)
    image_shape = image_np.shape
    # 转为灰度图
    image_np_gray = cv2.cvtColor(image_np, cv2.COLOR_BGR2GRAY)
    # 进行canny边缘检测
    image_edges = cv2.Canny(image_np_gray, 30, 70)
    drawing = np.zeros(image_np.shape[:], dtype=np.uint8)
    # 霍夫直线变换（统计的是线）
    lines = cv2.HoughLines(image_edges, 0.8, np.pi / 180, 90)

    # for line in lines:
    #     rho, theta = line[0]
    #     a = np.cos(theta)
    #     b = np.sin(theta)
    #     x0 = a * rho
    #     y0 = b * rho
    #     x1 = int(x0 + 1000 * (-b))
    #     y1 = int(y0 + 1000 * (a))
    #     x2 = int(x0 - 1000 * (-b))
    #     y2 = int(y0 - 1000 * (a))
    #     cv2.line(drawing, (x1, y1), (x2, y2), (0, 0, 255))
    for line in lines:
        rho, theta = line[0]
        cos_theta = np.cos(theta)
        sin_theta = np.sin(theta)
        # rho = x * cos_theta + y * sin_theta
        # y = (rho -x * cos_theta) / sin_theta
        x1, x2 = 0, image_shape[1]
        y1 = int((rho - x1 * cos_theta) / sin_theta)
        y2 = int((rho - x2 * cos_theta) / sin_theta)
        cv2.line(drawing, (x1, y1), (x2, y2), (0, 0, 255))
    # 返回处理正确后的内容
    cv2.imshow("drawing", drawing)
    cv2.waitKey(0)
