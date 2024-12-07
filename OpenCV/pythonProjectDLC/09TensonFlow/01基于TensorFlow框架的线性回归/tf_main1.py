import tensorflow as tf
import numpy as np

# 1、散点输入，定义输入数据
data = [[-0.5, 7.7], [1.8, 98.5], [0.9, 57.8], [0.4, 39.2], [-1.4, -15.7], [-1.4, -37.3], [-1.8, -49.1], [1.5, 75.6], [0.4, 34.0], [0.8, 62.3]]
# data列表10*2
# 转换成numpy
data = np.array(data)
x_data = data[:, 0]
y_data = data[:, 1]

# 转换成TensorFlow张量
x_train = tf.constant(x_data, dtype=tf.float32)
y_train = tf.constant(y_data, dtype=tf.float32)

# 2、定义前向模型
# (1, )指的是(None, 1)形状
model = tf.keras.Sequential([tf.keras.layers.Dense(1, input_shape=(1, ))])

# 3、定义损失函数和优化器
optimizer = tf.keras.optimizers.SGD(learning_rate=0.01)
model.compile(optimizer=optimizer, loss="mean_squared_error")

# 4、开始迭代
epoches = 500
# history = model.fit(x_train, y_train, epochs=epoches)
# 方便理解用循环打印，一般都是直接引用 history = model.fit(x_train, y_train, epochs=epoches)一句话实现
for epoch in range(1, epoches + 1):
    history = model.fit(x_train, y_train, verbose=0)
    loss = history.history["loss"][0]

    # 5、显示频率设置
    if epoch % 10 == 0 or epoch == 1:
        print(f"epoch:{epoch}, loss:{loss}")
