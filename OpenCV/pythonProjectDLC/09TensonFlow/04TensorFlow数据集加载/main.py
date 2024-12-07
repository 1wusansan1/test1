import tensorflow as tf
import numpy as np

seed = 42
tf.random.set_seed(42)

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

# TensorFlow数据集加载
dataset = tf.data.Dataset.from_tensor_slices((x_train, y_train))

dataset = dataset.shuffle(buffer_size=10)
dataset = dataset.batch(10)
# CPU取数据同时GPU、TPU训练，CPU会预先取出来一批数据，在CPU上训练无效果
dataset = dataset.prefetch(buffer_size=tf.data.experimental.AUTOTUNE)
# for item in dataset:
#     print(item)


# 2、定义前向模型
# (1, )指的是(None, 1)形状
model = tf.keras.Sequential([tf.keras.layers.Dense(1, input_shape=(1, ))])

# 3、定义损失函数和优化器
optimizer = tf.keras.optimizers.SGD(learning_rate=0.01)
model.compile(optimizer=optimizer, loss="mean_squared_error")

# 4、开始迭代
epoches = 500
# history = model.fit(x_train, y_train, epochs=epoches)
for epoch in range(1, epoches + 1):
    total_loss = 0
    for batch_x, batch_y in dataset:
        history = model.fit(x_train, y_train, verbose=0)
        loss = history.history["loss"][0]
        total_loss += loss
    # 计算平均损失
    avg_loss = total_loss / len(dataset)

    # 5、显示频率设置
    if epoch % 10 == 0 or epoch == 1:
        print(f"epoch:{epoch}, avg_loss:{avg_loss}")
