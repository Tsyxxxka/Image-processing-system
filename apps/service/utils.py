#coding=utf8
import matplotlib.pyplot as plt
import cv2
import numpy as np
from math import *

from flask import jsonify
import tensorflow as tf

from apps.service import settings


def wrap_success_json(result_name):
    result_name = 'http://127.0.0.1:5000/api/get_res_file/' + result_name
    return_data = {'code': '1', 'message': 'Success', 'result_name': result_name}
    return jsonify(return_data)


def wrap_failure_json(result_name):
    result_name = 'http://127.0.0.1:5000/api/get_res_file/' + result_name
    return_data = {'code': '2', 'message': 'Failure', 'result_name': result_name}
    return jsonify(return_data)


def img_expand(img1, img2):
    shape1 = img1.shape
    shape2 = img2.shape
    row1 = shape1[0]
    col1 = shape1[1]
    row2 = shape2[0]
    col2 = shape2[1]
    if row1 > row2:
        row = row1
    else:
        row = row2
    if col1 > col2:
        col = col1
    else:
        col = col2

    if (row - row1) % 2 != 0:
        r11 = int((row - row1) / 2)
        r12 = r11 + 1
    else:
        r11 = r12 = int((row - row1) / 2)

    if (col - col1) % 2 != 0:
        c11 = int((col - col1) / 2)
        c12 = c11 + 1
    else:
        c11 = c12 = int((col - col1) / 2)

    if (row - row2) % 2 != 0:
        r21 = int((row - row2) / 2)
        r22 = r21 + 1
    else:
        r21 = r22 = int((row - row2) / 2)

    if (col - col2) % 2 != 0:
        c21 = int((col - col2) / 2)
        c22 = c21 + 1
    else:
        c21 = c22 = int((col - col2) / 2)

    img1 = cv2.copyMakeBorder(img1, r11, r12, c11, c12, cv2.BORDER_CONSTANT, value=[255, 255, 255])
    img2 = cv2.copyMakeBorder(img2, r21, r22, c21, c22, cv2.BORDER_CONSTANT, value=[255, 255, 255])
    return img1, img2


def swap(val1, val2):
    return val2, val1


def order_desc(array):
    # 列表的长度
    length = len(array)
    # 对列表进行选择排序，获得有序的列表
    for i in range(length):
        for j in range(i + 1, length):
            # 选择最大的值
            if array[j] > array[i]:
                # 交换位置
                temp = array[j]
                array[j] = array[i]
                array[i] = temp
    return array


def grayHist(img, filename):
    plt.figure(filename, figsize=(16, 8))
    plt.subplot(121)
    plt.imshow(img, 'gray')
    plt.subplot(122)
    h, w = img.shape[:2]
    pixelSequence = img.reshape(1, h * w)
    numberBins = 256

    histogram, bins, patch = plt.hist(img.ravel(), 256, [0, 255])

    plt.xlabel("gray label")
    plt.ylabel("number of pixels")
    plt.axis([0, 255, 0, np.max(histogram)])
    plt.savefig(filename)
    plt.show()


def rotate(image, angle):
    height, width, channels = image.shape

    heightNew = int(width * fabs(sin(radians(angle))) + height * fabs(cos(radians(angle))))
    widthNew = int(height * fabs(sin(radians(angle))) + width * fabs(cos(radians(angle))))

    matRotation = cv2.getRotationMatrix2D((width / 2, height / 2), angle, 1)

    matRotation[0, 2] += (widthNew - width) / 2
    matRotation[1, 2] += (heightNew - height) / 2
    imgRotation = None
    if channels == 1:
        imgRotation = cv2.warpAffine(image, matRotation, (widthNew, heightNew), borderValue=(255))
    elif channels == 3:
        imgRotation = cv2.warpAffine(image, matRotation, (widthNew, heightNew), borderValue=(255, 255, 255))
    return imgRotation


# 频域平滑
def ideal_low_filter(img, D0):
    """
    生成一个理想低通滤波器（并返回）
    """
    h, w = img.shape[:2]
    filter_img = np.ones((h, w))
    u = np.fix(h / 2)
    v = np.fix(w / 2)
    for i in range(h):
        for j in range(w):
            d = np.sqrt((i - u) ** 2 + (j - v) ** 2)
            filter_img[i, j] = 0 if d > D0 else 1
    return filter_img


def butterworth_low_filter(img, D0, rank):
    """
        生成一个Butterworth低通滤波器（并返回）
    """
    h, w = img.shape[:2]
    filter_img = np.zeros((h, w))
    u = np.fix(h / 2)
    v = np.fix(w / 2)
    for i in range(h):
        for j in range(w):
            d = np.sqrt((i - u) ** 2 + (j - v) ** 2)
            filter_img[i, j] = 1 / (1 + 0.414 * (d / D0) ** (2 * rank))
    return filter_img


def exp_low_filter(img, D0, rank):
    """
        生成一个指数低通滤波器（并返回）
    """
    h, w = img.shape[:2]
    filter_img = np.zeros((h, w))
    u = np.fix(h / 2)
    v = np.fix(w / 2)
    for i in range(h):
        for j in range(w):
            d = np.sqrt((i - u) ** 2 + (j - v) ** 2)
            filter_img[i, j] = np.exp(np.log(1 / np.sqrt(2)) * (d / D0) ** (2 * rank))
    return filter_img


def filter_use(img, filter):
    """
    将图像img与滤波器filter结合，生成对应的滤波图像
    """
    # 首先进行傅里叶变换
    f = np.fft.fft2(img)
    f_center = np.fft.fftshift(f)
    # 应用滤波器进行反变换
    S = np.multiply(f_center, filter)  # 频率相乘——l(u,v)*H(u,v)
    f_origin = np.fft.ifftshift(S)  # 将低频移动到原来的位置
    f_origin = np.fft.ifft2(f_origin)  # 使用ifft2进行傅里叶的逆变换
    f_origin = np.abs(f_origin)  # 设置区间
    return f_origin


def DFT_show(img):
    """
    对传入的图像进行傅里叶变换，生成频域图像
    """
    f = np.fft.fft2(img)  # 使用numpy进行傅里叶变换
    fshift = np.fft.fftshift(f)  # 把零频率分量移到中间
    result = np.log(1 + abs(fshift))
    return result


# 频域锐化
def ideal_high_filter(img, D0):
    """
    生成一个理想高通滤波器（并返回）
    """
    h, w = img.shape[:2]
    filter_img = np.zeros((h, w))
    u = np.fix(h / 2)
    v = np.fix(w / 2)
    for i in range(h):
        for j in range(w):
            d = np.sqrt((i - u) ** 2 + (j - v) ** 2)
            filter_img[i, j] = 0 if d < D0 else 1
    return filter_img


def butterworth_high_filter(img, D0, rank):
    """
        生成一个Butterworth高通滤波器（并返回）
    """
    h, w = img.shape[:2]
    filter_img = np.zeros((h, w))
    u = np.fix(h / 2)
    v = np.fix(w / 2)
    for i in range(h):
        for j in range(w):
            d = np.sqrt((i - u) ** 2 + (j - v) ** 2)
            filter_img[i, j] = 1 / (1 + (D0 / d) ** (2 * rank))
    return filter_img


def exp_high_filter(img, D0, rank):
    """
        生成一个指数高通滤波器（并返回）
    """
    h, w = img.shape[:2]
    filter_img = np.zeros((h, w))
    u = np.fix(h / 2)
    v = np.fix(w / 2)
    for i in range(h):
        for j in range(w):
            d = np.sqrt((i - u) ** 2 + (j - v) ** 2)
            filter_img[i, j] = np.exp((-1) * (D0 / d) ** rank)
    return filter_img


def filter_use2(img, filter):
    """
    将图像img与滤波器filter结合，生成对应的滤波图像
    """
    # 首先进行傅里叶变换
    f = np.fft.fft2(img)
    f_center = np.fft.fftshift(f)
    # 应用滤波器进行反变换
    S = np.multiply(f_center, filter)  # 频率相乘——l(u,v)*H(u,v)
    f_origin = np.fft.ifftshift(S)  # 将低频移动到原来的位置
    f_origin = np.fft.ifft2(f_origin)  # 使用ifft2进行傅里叶的逆变换
    f_origin = np.abs(f_origin)  # 设置区间
    f_origin = f_origin / np.max(f_origin.all())
    return f_origin


# 我们准备使用经典网络在imagenet数据集上的与训练权重，所以归一化时也要使用imagenet的平均值和标准差
image_mean = tf.constant([0.485, 0.456, 0.406])
image_std = tf.constant([0.299, 0.224, 0.225])


def normalization(x):
    """
    对输入图片x进行归一化，返回归一化的值
    """
    return (x - image_mean) / image_std


def load_images(image_path, width=settings.WIDTH, height=settings.HEIGHT):
    """
    加载并处理图片
    :param image_path:　图片路径
    :param width: 图片宽度
    :param height: 图片长度
    :return:　一个张量
    """
    # 加载文件
    x = tf.io.read_file(image_path)
    # 解码图片
    x = tf.image.decode_jpeg(x, channels=3)
    # 修改图片大小
    x = tf.image.resize(x, [height, width])
    x = x / 255.
    # 归一化
    x = normalization(x)
    x = tf.reshape(x, [1, height, width, 3])
    # 返回结果
    return x


def save_image(image, filename):
    x = tf.reshape(image, image.shape[1:])
    x = x * image_std + image_mean
    x = x * 255.
    x = tf.cast(x, tf.int32)
    x = tf.clip_by_value(x, 0, 255)
    x = tf.cast(x, tf.uint8)
    x = tf.image.encode_jpeg(x)
    tf.io.write_file(filename, x)
