import tensorflow as tf
import numpy as np
from tensorflow.keras import Model

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
# x_train = tf.constant(x_data, dtype=tf.float32)
x_train = tf.constant(np.expand_dims(x_data, axis=1), dtype=tf.float32)
y_train = tf.constant(y_data, dtype=tf.float32)

dataset = tf.data.Dataset.from_tensor_slices((x_train, y_train))

dataset = dataset.shuffle(buffer_size=10)
dataset = dataset.batch(10)
# CPU取数据同时GPU、TPU训练，CPU会预先取出来一批数据，在CPU上训练无效果
dataset = dataset.prefetch(buffer_size=tf.data.experimental.AUTOTUNE)

# 2、定义前向模型
# 方案4
def linear():
    input = tf.keras.layers.Input(shape=(1, ), dtype=tf.float32)
    y = tf.keras.layers.Dense(1)(input)
    model = tf.keras.models.Model(inputs=input, outputs=y)
    return model

model = linear()

# 3、定义损失函数和优化器
optimizer = tf.keras.optimizers.SGD(learning_rate=0.01)
model.compile(optimizer=optimizer, loss="mean_squared_error")

# 1) summary
# print(model.summary())

# 2) plot_model函数保存网络结构图
# 本地虚拟仿真平台命令行中python -m pip install pydot==1.4.1
# install graphviz (see instructions at https://graphviz.gitlab.io/download/) for plot_model/model_to_dot to work
# tf.keras.utils.plot_model(model, to_file="model.png", show_shapes=True)

# 3)netron 虚拟仿真平台训练打开h5文件

# 4)tensorboard方法
epoches = 500
# 在计算图中添加模型
tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir="./logs")
# 把训练过程数据添加到模型中，便于显示
model.fit(x_train, y_train, epochs=epoches, callbacks=[tensorboard_callback])
# cd D:\projects\OpenCV\pythonProjectDLC\09TensonFlow\05TensorFlow的网络结构查看
# "D:\soft\FS\FS_AISIMS\tools\Python\python.exe" "D:\soft\FS\FS_AISIMS\tools\Python\Scripts\tensorboard.exe"  --logdir "logs"
