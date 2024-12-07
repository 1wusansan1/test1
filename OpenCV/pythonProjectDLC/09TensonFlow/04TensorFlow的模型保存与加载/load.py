import tensorflow as tf
from tensorflow.keras import models, Model
import numpy as np

# 加载模型
loaded_model = models.load_model("my_model.h5")
# 预测
input_data = np.array([[1.5]])
pre = loaded_model.predict(input_data)
print(f"预测结果: {pre[0][0]}")

# 只有参数的模型
def linear():
    input = tf.keras.layers.Input(shape=(1, ), dtype=tf.float32)
    y = tf.keras.layers.Dense(1)(input)
    model = tf.keras.models.Model(inputs=input, outputs=y)
    return model

model = linear()

input_data = np.array([[1.5]])

model.load_weights("model_weights.h5")
pre = model.predict(input_data)

print(pre)


class Linear(Model):
    def __init__(self):
        super(Linear, self).__init__()
        self.linear = tf.keras.layers.Dense(1)

    def call(self, x, **kwargs):
        x = self.linear(x)
        return x

model = Linear()

input_data = np.array([[1.5]])

_ = model(input_data)

model.load_weights("model_weights.h5")
pre = model.predict(input_data)

print(pre)

