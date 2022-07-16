#coding=utf8
import cv2
import numpy as np
from apps.service import utils


def graying(img_name, result_name):
    img_path = 'apps/assets/' + img_name
    result_path = 'apps/results/' + result_name

    img = cv2.imread(img_path, 1)
    result = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(result_path, result)
    return 1


def thresholding(img_name, result_name):
    img_path = 'apps/assets/' + img_name
    result_path = 'apps/results/' + result_name

    img = cv2.imread(img_path, 1)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, result = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    cv2.imwrite(result_path, result)
    return 1


def logical_and(img_name1, img_name2, result_name):
    img_path1 = 'apps/assets/' + img_name1
    img_path2 = 'apps/assets/' + img_name2
    result_path = 'apps/results/' + result_name

    img1 = cv2.imread(img_path1, 0)
    img2 = cv2.imread(img_path2, 0)

    img1, img2 = utils.img_expand(img1, img2)

    result = img1 & img2
    cv2.imwrite(result_path, result)
    return 1


def logical_or(img_name1, img_name2, result_name):
    img_path1 = 'apps/assets/' + img_name1
    img_path2 = 'apps/assets/' + img_name2
    result_path = 'apps/results/' + result_name

    img1 = cv2.imread(img_path1, 0)
    img2 = cv2.imread(img_path2, 0)

    img1, img2 = utils.img_expand(img1, img2)

    result = img1 | img2
    cv2.imwrite(result_path, result)
    return 1


def logical_not(img_name, result_name):
    img_path = 'apps/assets/' + img_name
    result_path = 'apps/results/' + result_name

    img = cv2.imread(img_path, 0)
    result = ~img
    cv2.imwrite(result_path, result)
    return 1


def add(img_name1, img_name2, result_name):
    img_path1 = 'apps/assets/' + img_name1
    img_path2 = 'apps/assets/' + img_name2
    result_path = 'apps/results/' + result_name

    img1 = cv2.imread(img_path1, 1)
    img2 = cv2.imread(img_path2, 1)

    img1, img2 = utils.img_expand(img1, img2)

    result = cv2.add(img1, img2)
    cv2.imwrite(result_path, result)
    return 1


def subtract(img_name1, img_name2, result_name):
    img_path1 = 'apps/assets/' + img_name1
    img_path2 = 'apps/assets/' + img_name2
    result_path = 'apps/results/' + result_name

    img1 = cv2.imread(img_path1, 1)
    img2 = cv2.imread(img_path2, 1)

    img1, img2 = utils.img_expand(img1, img2)

    result = cv2.subtract(img1, img2)
    cv2.imwrite(result_path, result)
    return 1


def multiply(img_name1, img_name2, result_name):
    img_path1 = 'apps/assets/' + img_name1
    img_path2 = 'apps/assets/' + img_name2
    result_path = 'apps/results/' + result_name

    img1 = cv2.imread(img_path1, 1)
    img2 = cv2.imread(img_path2, 1)

    img1, img2 = utils.img_expand(img1, img2)

    result = cv2.multiply(img1, img2)
    cv2.imwrite(result_path, result)
    return 1


def divide(img_name1, img_name2, result_name):
    img_path1 = 'apps/assets/' + img_name1
    img_path2 = 'apps/assets/' + img_name2
    result_path = 'apps/results/' + result_name

    img1 = cv2.imread(img_path1, 1)
    img2 = cv2.imread(img_path2, 1)

    img1, img2 = utils.img_expand(img1, img2)

    result = cv2.divide(img1, img2)
    cv2.imwrite(result_path, result)
    return 1


def flip(img_name, result_name, fli_choi):
    img_path = 'apps/assets/' + img_name
    result_path = 'apps/results/' + result_name

    img = cv2.imread(img_path, 1)

    if fli_choi == 'horizontal':
        result = cv2.flip(img, 1)
    elif fli_choi == 'vertical':
        result = cv2.flip(img, 0)
    elif fli_choi == 'diagonal':
        result = cv2.flip(img, -1)
    else:
        return 2

    cv2.imwrite(result_path, result)
    return 1


def move(img_name, result_name, move_x, move_y):
    img_path = 'apps/assets/' + img_name
    result_path = 'apps/results/' + result_name

    try:
        move_x = int(move_x)
        move_y = int(move_y)
    except ValueError:
        return 2

    img = cv2.imread(img_path, 1)

    pix_M = np.float32([[1, 0, move_x], [0, 1, move_y]])
    img_height, img_width, img_channel = img.shape
    result = cv2.warpAffine(img, pix_M, (img_width, img_height))

    cv2.imwrite(result_path, result)
    return 1


def rotate(img_name, result_name, angle):
    img_path = 'apps/assets/' + img_name
    result_path = 'apps/results/' + result_name

    try:
        angle = int(angle)
    except ValueError:
        return 2

    img = cv2.imread(img_path, 1)

    result = utils.rotate(img, angle)

    cv2.imwrite(result_path, result)
    return 1


def resize(img_name, result_name, size_x, size_y):
    img_path = 'apps/assets/' + img_name
    result_path = 'apps/results/' + result_name

    try:
        size_x = float(size_x)
        size_y = float(size_y)
    except ValueError:
        return 2

    if (size_x <= 0) or (size_y <= 0):
        return 2

    img = cv2.imread(img_path, 1)

    result = cv2.resize(img, (0, 0), fx=size_x, fy=size_y, interpolation=cv2.INTER_LINEAR)
    cv2.imwrite(result_path, result)
    return 1
