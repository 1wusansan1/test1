# 导入OpenCV的库
import cv2

# 1. 读取图片
image_np = cv2.imread('./picture.png')

# 复制一份原始图像，用来绘制轮廓
image_contours = image_np.copy()

# 2. 灰度化图像
image_gray = cv2.cvtColor(image_np, cv2.COLOR_BGR2GRAY)

# 3. 二值化图像
ret, image_binary = cv2.threshold(image_gray, 127, 255, cv2.THRESH_OTSU + cv2.THRESH_BINARY_INV)

# 4. 查找轮廓
# cv2.RETR_EXTERNAL 轮廓检索模式选择绘制外边框
# cv2.CHAIN_APPROX_SIMPLE表示只存储有用的点，比如直线只存储起点和终点，四边形只存储四个顶点，默认使用这个方法
# contours：存储了所有的轮廓点的坐标，比如说contours[0]就存储了第0个轮廓的点的坐标，contours[1]就存储了第1个轮廓的点的坐标
# hierarchy：存储了对应轮廓的层级关系，hierarchy[0]就存储了第0个轮廓的层级关系。
# contours, hierarchy = cv2.findContours(image_binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
contours, hierarchy = cv2.findContours(image_binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 5. 绘制轮廓
# cv2.drawContours(image_contours, contours, 1, (0, 0, 255), thickness=cv2.FILLED)
cv2.drawContours(image_contours, contours, -1, (255, 0, 255))
# 6. 结果显示
cv2.imshow('image_np', image_np)
cv2.imshow('image_contours', image_contours)
cv2.waitKey(0)
