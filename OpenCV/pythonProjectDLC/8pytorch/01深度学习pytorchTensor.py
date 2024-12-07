import torch

# # 打印一个标量
# scalar_tensor = torch.tensor(3.14)
# print("scalar_tensor:", scalar_tensor)
#
# 打印一个向量
vector_tensor = torch.tensor([1, 2, 3, 4, 5, 6])
print("vector_tensor:", vector_tensor)

# 打印一个矩阵
matrix_tensor = torch.tensor([[1, 2], [3, 4]])
print("matrix_tensor:", matrix_tensor)


"""
tensor的存储
"""
# tensor1 = torch.tensor([[1., 2, 3], [4, 5, 6]])
# # 打印张量
# print(tensor1)
# # 打印形状
# print(tensor1.shape)
# # 数据类型
# print(tensor1.dtype)
# # 存储的内容
# print(tensor1.storage().tolist())

"""
float16的二进制和十进制的转换
"""
# import numpy as np
# import struct
# def print_float16(val: float):
#     """ Print Float16 in a binary form """
#     m = struct.unpack('H', struct.pack('e', np.float16(val)))[0]
#     return format(m, 'b').zfill(16)
#
# def ieee_754_conversion(sign, exponent_raw, mantissa, exp_len=8, mant_len=23):
#     """ Convert binary data into the floating point value """
#     sign_mult = -1 if sign == 1 else 1
#     exponent = exponent_raw - (2 ** (exp_len - 1) - 1)
#     mant_mult = 1
#     for b in range(mant_len - 1, -1, -1):
#         if mantissa & (2 ** b):
#             mant_mult += 1 / (2 ** (mant_len - b))
#     return sign_mult * (2 ** exponent) * mant_mult
#
# print(print_float16(0.75))
# print(ieee_754_conversion(0, 0b01110, 0b1000000000, exp_len=5, mant_len=10))
# # 最大值和最小值
# # 这里使用0b11110，是因为在IEEE 754标准中，0b11111是为“无穷大”保留的:
# print(ieee_754_conversion(0, 0b11110, 0b1111111111, exp_len=5, mant_len=10))
# print(ieee_754_conversion(0, 0b00001, 0b0000000000, exp_len=5, mant_len=10))


"""
storage的存储：
    对张量进行操作时（比如调整形状、转置等），它不会创建一个新的张量，而是返回一个指向相同数据的视图。
    即PyTorch通常会共享相同的存储对象，以节省内存和提高效率。
    发现a和b的地址相同
"""
a = torch.arange(12).reshape(3, 4)
print(a)
# print(a.storage().tolist())
print(a.storage().data_ptr())  # 地址
print(a.shape)
b = a.transpose(0, 1)
print(b)
# print(b.storage().tolist())
print(b.storage().data_ptr())
print(b.shape)
"""
tensor的步长:
    步长指的是在每个维度上移动一个元素时在底层存储中需要跨越的元素数。
"""
print('---------------------------------tensor的步长')
a = torch.arange(12).reshape(3, 4)
print(a)
print(a.stride(), '------步长')

"""
tensor的连续性
"""
print('---------------------------------tensor的连续性')
a = torch.arange(12).reshape(3, 4)
# print(a.flatten())
# # print(a.storage().tolist())
b = a.transpose(0, 1)  # 转置
# print(b.flatten())
# print(b.storage().tolist())
print(b.is_contiguous())
b = b.contiguous()
print(b.is_contiguous())
print(b.view(2, 6))
