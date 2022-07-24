#coding=utf8
import sys

import cv2
import numpy as np

from apps.service import utils


def gauss_noise(img_name, result_name):
    img_path = 'apps/assets/' + img_name
    result_path = 'apps/results/' + result_name

    img = cv2.imread(img_path)
    image = np.array(img / 255, dtype=float)

    noise = np.random.normal(0, 0.1, image.shape)

    out = image + noise
    out = np.clip(out, 0.0, 1.0)
    out = np.uint8(out * 255)
    cv2.imwrite(result_path, out)
    return 1


def sault_pepper_noise(img_name, result_name, ran_x1, ran_y1, ran_x2, ran_y2):
    img_path = 'apps/assets/' + img_name
    result_path = 'apps/results/' + result_name

    try:
        if ran_y1 == "MAX":
            ran_y1 = sys.maxsize

        if ran_y2 == "MAX":
            ran_y2 = sys.maxsize

        ran_x1 = int(ran_x1)
        ran_y1 = int(ran_y1)
        ran_x2 = int(ran_x2)
        ran_y2 = int(ran_y2)
    except ValueError:
        return 2

    if (ran_x1 < 0) or (ran_y1 < 0) or (ran_x2 < 0) or (ran_y2 < 0):
        return 2

    if ran_x1 >= ran_y1:
        ran_x1, ran_y1 = utils.swap(ran_x1, ran_y1)

    if ran_x2 >= ran_y2:
        ran_x2, ran_y2 = utils.swap(ran_x2, ran_y2)

    img = cv2.imread(img_path, 0)
    out = np.zeros(img.shape, np.uint8)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if ran_x1 < img[i][j] < ran_y1:
                # 添加胡椒噪声
                out[i][j] = 0
            elif ran_x2 < img[i][j] < ran_y2:
                # 添加食盐噪声
                out[i][j] = 255
            else:
                # 不添加噪声
                out[i][j] = img[i][j]
    cv2.imwrite(result_path, out)
    return 1


def arithmetic_average_filter(img_name, result_name, filter_size_p, filter_size_q ):
    img_path = 'apps/assets/' + img_name
    result_path = 'apps/results/' + result_name

    try:
        filter_size_p = int(filter_size_p)
        filter_size_q = int(filter_size_q)
    except ValueError:
        return 2

    if (filter_size_p <= 0) or (filter_size_q <= 0):
        return 2

    if ((filter_size_p % 2) == 0) or ((filter_size_q % 2) == 0):
        return 2

    p = int(filter_size_p / 2)
    q = int(filter_size_q / 2)

    img = cv2.imread(img_path, 0)
    out = np.zeros(img.shape, np.uint8)

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            sum = 0

            for m in range(-p, p + 1):
                for n in range(-q, q + 1):
                    if 0 <= i + m < img.shape[0] and 0 <= j + n < img.shape[1]:
                        sum += img[i + m][j + n]

            out[i][j] = int(sum / (filter_size_p * filter_size_q))

    cv2.imwrite(result_path, out)
    return 1


def geometric_average_filter(img_name, result_name, filter_size_p, filter_size_q):
    img_path = 'apps/assets/' + img_name
    result_path = 'apps/results/' + result_name

    try:
        filter_size_p = int(filter_size_p)
        filter_size_q = int(filter_size_q)
    except ValueError:
        return 2

    if (filter_size_p <= 0) or (filter_size_q <= 0):
        return 2

    if ((filter_size_p % 2) == 0) or ((filter_size_q % 2) == 0):
        return 2

    p = int(filter_size_p / 2)
    q = int(filter_size_q / 2)

    img = cv2.imread(img_path, 0)
    out = np.zeros(img.shape, np.uint8)

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            mul = 1

            for m in range(-p, p + 1):
                for n in range(-q, q + 1):
                    if 0 <= i + m < img.shape[0] and 0 <= j + n < img.shape[1]:
                        mul *= img[i + m][j + n]

            out[i][j] = int(pow(mul, float (1 / (filter_size_p * filter_size_q))))

    cv2.imwrite(result_path, out)
    return 1


def harmonic_average_filter(img_name, result_name, filter_size_p, filter_size_q):
    img_path = 'apps/assets/' + img_name
    result_path = 'apps/results/' + result_name

    try:
        filter_size_p = int(filter_size_p)
        filter_size_q = int(filter_size_q)
    except ValueError:
        return 2

    if (filter_size_p <= 0) or (filter_size_q <= 0):
        return 2

    if ((filter_size_p % 2) == 0) or ((filter_size_q % 2) == 0):
        return 2

    p = int(filter_size_p / 2)
    q = int(filter_size_q / 2)

    img = cv2.imread(img_path, 0)
    out = np.zeros(img.shape, np.uint8)

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            harm = 0.0

            for m in range(-p, p + 1):
                for n in range(-q, q + 1):
                    if 0 <= i + m < img.shape[0] and 0 <= j + n < img.shape[1]:
                        harm += 1 / img[i + m][j + n]

            out[i][j] = int((filter_size_p * filter_size_q) / harm)

    cv2.imwrite(result_path, out)
    return 1


def min_filter(img_name, result_name):
    img_path = 'apps/assets/' + img_name
    result_path = 'apps/results/' + result_name

    img = cv2.imread(img_path, 0)
    out = np.zeros(img.shape, np.uint8)

    array = []

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            array.clear()
            for m in range(-1, 2):
                for n in range(-1, 2):
                    if 0 <= i + m < img.shape[0] and 0 <= j + n < img.shape[1]:
                        array.append(img[i + m][j + n])
            res_array = utils.order_desc(array)
            res_array_leng = len(res_array)
            out[i][j] = res_array[res_array_leng - 1]

    cv2.imwrite(result_path, out)
    return 1


def max_filter(img_name, result_name):
    img_path = 'apps/assets/' + img_name
    result_path = 'apps/results/' + result_name

    img = cv2.imread(img_path, 0)
    out = np.zeros(img.shape, np.uint8)

    array = []

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            array.clear()
            for m in range(-1, 2):
                for n in range(-1, 2):
                    if 0 <= i + m < img.shape[0] and 0 <= j + n < img.shape[1]:
                        array.append(img[i + m][j + n])
            res_array = utils.order_desc(array)
            res_array_leng = len(res_array)
            out[i][j] = res_array[0]

    cv2.imwrite(result_path, out)
    return 1


def median_filter(img_name, result_name):
    img_path = 'apps/assets/' + img_name
    result_path = 'apps/results/' + result_name

    img = cv2.imread(img_path, 0)
    out = np.zeros(img.shape, np.uint8)

    array = []

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            array.clear()
            for m in range(-1, 2):
                for n in range(-1, 2):
                    if 0 <= i + m < img.shape[0] and 0 <= j + n < img.shape[1]:
                        array.append(img[i + m][j + n])
            res_array = utils.order_desc(array)
            res_array_leng = len(res_array)
            out[i][j] = res_array[int(res_array_leng / 2)]

    cv2.imwrite(result_path, out)
    return 1


def range_filter(img_name, result_name, min, max, color):
    img_path = 'apps/assets/' + img_name
    result_path = 'apps/results/' + result_name

    try:
        if max == "MAX":
            max = sys.maxsize

        min = int(min)
        max = int(max)
    except ValueError:
        return 2

    if (min < 0) or (max < 0):
        return 2

    if min >= max:
        min, max = utils.swap(min, max)

    img = cv2.imread(img_path, 0)
    out = np.zeros(img.shape, np.uint8)

    array = []

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            # 滤波器内像素值的和
            array.clear()
            if min < img[i][j] < max:
                out[i][j] = img[i][j]
            else:
                if color == '0':
                    out[i][j] = 0
                elif color == '255':
                    out[i][j] = 255
                else:
                    return 2

    cv2.imwrite(result_path, out)
    return 1
