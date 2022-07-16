#coding=utf8
import cv2
import numpy as np
from apps.service import utils


def smoo_neighbour_average(img_name, result_name, kernel_size):
    img_path = 'apps/assets/' + img_name
    result_path = 'apps/results/' + result_name

    try:
        kernel_size = int(kernel_size)
    except ValueError:
        return 2

    if (kernel_size <= 0) or (kernel_size % 2 == 0):
        return 2

    img = cv2.imread(img_path)
    result = cv2.blur(img, (kernel_size, kernel_size))
    cv2.imwrite(result_path, result)
    return 1


def smoo_median_filter(img_name, result_name, kernel_size):
    img_path = 'apps/assets/' + img_name
    result_path = 'apps/results/' + result_name

    try:
        kernel_size = int(kernel_size)
    except ValueError:
        return 2

    if (kernel_size <= 0) or (kernel_size % 2 == 0):
        return 2

    img = cv2.imread(img_path)
    result = cv2.medianBlur(img, kernel_size)
    cv2.imwrite(result_path, result)
    return 1


def shar_robert(img_name, result_name):
    img_path = 'apps/assets/' + img_name
    result_path = 'apps/results/' + result_name

    img = cv2.imread(img_path)
    h = img.shape[0]
    w = img.shape[1]
    result = np.zeros(img.shape, np.uint8)
    for i in range(1, h - 1):
        for j in range(1, w - 1):
            result[i][j] = np.abs(img[i][j].astype(int) - img[i + 1][j + 1].astype(int)) + np.abs(
                img[i + 1][j].astype(int) - img[i][j + 1].astype(int))
    cv2.imwrite(result_path, result)
    return 1


def shar_laplacian(img_name, result_name):
    img_path = 'apps/assets/' + img_name
    result_path = 'apps/results/' + result_name

    img = cv2.imread(img_path)
    h = img.shape[0]
    w = img.shape[1]
    result = np.zeros(img.shape, np.uint8)
    for i in range(1, h - 1):
        for j in range(1, w - 1):
            result[i][j] = 4 * img[i][j].astype(int) - img[i + 1][j].astype(int) - img[i - 1][j].astype(int) - \
                           img[i][j + 1].astype(int) - img[i][j - 1].astype(int)
    cv2.imwrite(result_path, result)
    return 1


def shar_sobel(img_name, result_name):
    img_path = 'apps/assets/' + img_name
    result_path = 'apps/results/' + result_name

    img = cv2.imread(img_path)
    kern_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    kern_y = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
    img_x = cv2.filter2D(img, -1, kern_x, borderType=cv2.BORDER_REFLECT)
    img_y = cv2.filter2D(img, -1, kern_y, borderType=cv2.BORDER_REFLECT)
    abs_x = cv2.convertScaleAbs(img_x)
    abs_y = cv2.convertScaleAbs(img_y)
    result = cv2.addWeighted(abs_x, 0.5, abs_y, 0.5, 0)
    cv2.imwrite(result_path, result)
    return 1


def shar_prewitt(img_name, result_name):
    img_path = 'apps/assets/' + img_name
    result_path = 'apps/results/' + result_name

    img = cv2.imread(img_path)
    kern_x = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]])
    kern_y = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
    img_x = cv2.filter2D(img, cv2.CV_16S, kern_x)
    img_y = cv2.filter2D(img, cv2.CV_16S, kern_y)
    abs_x = cv2.convertScaleAbs(img_x)
    abs_y = cv2.convertScaleAbs(img_y)
    result = cv2.addWeighted(abs_x, 0.5, abs_y, 0.5, 0)
    cv2.imwrite(result_path, result)
    return 1


def smoo_ideal_filter(img_name, result_name, d0):
    img_path = 'apps/assets/' + img_name
    result_path = 'apps/results/' + result_name

    try:
        d0 = int(d0)
    except ValueError:
        return 2

    if (d0 < 0) or (d0 > 255):
        return 2

    img = cv2.imread(img_path, 0)
    ideal_filter = utils.ideal_low_filter(img, d0)
    result = utils.filter_use(img, ideal_filter)
    cv2.imwrite(result_path, result)
    return 1


def smoo_barte_filter(img_name, result_name, d0, rank):
    img_path = 'apps/assets/' + img_name
    result_path = 'apps/results/' + result_name

    try:
        d0 = int(d0)
        rank = int(rank)
    except ValueError:
        return 2

    if (d0 < 0) or (d0 > 255):
        return 2

    img = cv2.imread(img_path, 0)
    butterworth_filter = utils.butterworth_low_filter(img, d0, rank)
    result = utils.filter_use(img, butterworth_filter)
    cv2.imwrite(result_path, result)
    return 1


def smoo_exp_filter(img_name, result_name, d0, rank):
    img_path = 'apps/assets/' + img_name
    result_path = 'apps/results/' + result_name

    try:
        d0 = int(d0)
        rank = int(rank)
    except ValueError:
        return 2

    if (d0 < 0) or (d0 > 255):
        return 2

    img = cv2.imread(img_path, 0)
    exp_filter = utils.exp_low_filter(img, d0, rank)
    result = utils.filter_use(img, exp_filter)
    cv2.imwrite(result_path, result)
    return 1


def shar_ideal_high(img_name, result_name, d0):
    img_path = 'apps/assets/' + img_name
    result_path = 'apps/results/' + result_name

    try:
        d0 = int(d0)
    except ValueError:
        return 2

    if (d0 < 0) or (d0 > 255):
        return 2

    img = cv2.imread(img_path, 0)
    ideal_filter = utils.ideal_high_filter(img, d0)
    result = utils.filter_use2(img, ideal_filter)
    cv2.imwrite(result_path, result)
    return 1


def shar_barte_filter(img_name, result_name, d0, rank):
    img_path = 'apps/assets/' + img_name
    result_path = 'apps/results/' + result_name

    try:
        d0 = int(d0)
        rank = int(rank)
    except ValueError:
        return 2

    if (d0 < 0) or (d0 > 255):
        return 2

    img = cv2.imread(img_path, 0)
    butterworth_filter = utils.butterworth_high_filter(img, d0, rank)
    result = utils.filter_use2(img, butterworth_filter)
    cv2.imwrite(result_path, result)
    return 1


def shar_exp_filter(img_name, result_name, d0, rank):
    img_path = 'apps/assets/' + img_name
    result_path = 'apps/results/' + result_name

    try:
        d0 = int(d0)
        rank = int(rank)
    except ValueError:
        return 2

    if (d0 < 0) or (d0 > 255):
        return 2

    img = cv2.imread(img_path, 0)
    exp_filter = utils.exp_high_filter(img, d0, rank)
    result = utils.filter_use2(img, exp_filter)
    cv2.imwrite(result_path, result)
    return 1
