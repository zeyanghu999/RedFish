# coding: utf-8
import sys, os
sys.path.append(os.pardir)  # 为了导入父目录的文件而进行的设定
import numpy as np
from dataset.mnist import load_mnist
from PIL import Image


def img_show(img):
    pil_img = Image.fromarray(np.uint8(img))
    pil_img.show()
# 训练图像，训练标签；测试图像，测试标签
(x_train, t_train), (x_test, t_test) = load_mnist(flatten=True, normalize=False)
#参数normalize设置是否将输入图像正规化为0.0～1.0的值 如果将该参数设置为False，则输入图像的像素会保持原来的0～255
#参数flatten设置是否展开输入图像（变成一维数组）。如果将该参数设置为False，则输入图像为1 × 28 × 28的三维数组。若设置为True，则输入图像会保存为由784个元素构成的一维数组

img = x_train[0]
label = t_train[0]
print(label)  # 5

print(img.shape)  # (784,)
img = img.reshape(28, 28)  # 把图像的形状变为原来的尺寸
print(img.shape)  # (28, 28)

img_show(img)
