import math

x = [1, 2]
y = [4, 6]

print([(a, b) for a, b in zip(x, y)])
print([a ** 2 for a in x])


# 1欧式距离
def eucalidean_siatance1(x, y):
    sum0 = math.sqrt(sum([(a - b) ** 2 for a, b in zip(x, y)]))
    # for a, b in zip(x, y):
    #     sum += (a - b) ** 2
    return sum0


print(eucalidean_siatance1(x, y), '---1欧式距离')


# 2曼哈顿距离
def eucalidean_siatance2(x, y):
    ss = sum([abs(a - b) for a, b in zip(x, y)])
    return ss


print(eucalidean_siatance2(x, y), '---2曼哈顿距离')


# 3切比雪夫距离
def eucalidean_siatance3(x, y):
    ss = max([abs(a - b) for a, b in zip(x, y)])
    return ss


print(eucalidean_siatance3(x, y), '---3切比雪夫距离')


# 4 余弦相似度
def eucalidean_siatance4(x, y):
    s0 = sum([abs(a * b) for a, b in zip(x, y)])
    s1 = math.sqrt(sum([a ** 2 for a in x])) * math.sqrt(sum([b ** 2 for b in y]))
    return s0 / s1


print(eucalidean_siatance4(x, y), '---4余弦相似度')


# 5 汉明距离
def eucalidean_siatance5(str_x, str_y):
    return sum(a != b for a, b in zip(str_x, str_y))


str_x = "101100"
str_y = "111000"
print(eucalidean_siatance5(str_x, str_y), '---汉明距离')


# 闵可夫斯基距离
def minkefu(x, y, p):
    return sum(abs(a - b) ** p for a, b in zip(x, y)) ** (1 / p)


print(minkefu(x, y, 100), '---闵可夫斯基距离')


# jaccrd指数
def jaccard_index(x_set, y_set):
    intersection = len(set(x_set & y_set))
    union = len(set(x_set | y_set))
    return intersection / union


x_set = {1, 2, 3}
y_set = {2, 3, 4}
print(jaccard_index(x_set, y_set), '---jaccrd指数')


# 半正矢距离
def haversine_distance(lat1, lon1, lat2, lon2):
    R = 6371.0
    # 地球半径，km
    # 将十进制转成弧度
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)
    lon = lon2 - lon1
    lat = lat2 - lat1
    return 2 * R * math.asin(
        math.sqrt(math.sin(lat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(lon / 2) ** 2))


lat1, lon1 = 52.2296756, 21.0122287  # 华沙的经纬度
lat2, lon2 = 51.5073509, -0.1277583  # 伦敦的经纬度
print(haversine_distance(lat1, lon1,lat2, lon2), '---半正矢距离')
