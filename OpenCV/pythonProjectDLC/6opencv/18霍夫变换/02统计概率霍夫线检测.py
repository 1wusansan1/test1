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
    # 统计概率霍夫直线变换（统计的是线段）
    lines = cv2.HoughLinesP(image_edges, 0.8, np.pi / 180, 90, minLineLength=90, maxLineGap=50)

    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(drawing, (x1, y1), (x2, y2), (0, 0, 255))
    # 返回处理正确后的内容
    cv2.imshow("drawing", drawing)
    cv2.waitKey(0)
