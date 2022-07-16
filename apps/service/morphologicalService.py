#coding=utf8
import cv2
import numpy as np
from apps.service import utils


def erode(img_name, result_name, kernel_type, kernel_size):
    img_path = 'apps/assets/' + img_name
    result_path = 'apps/results/' + result_name

    try:
        kernel_size = int(kernel_size)
    except ValueError:
        return 2

    if (kernel_size <= 0) or (kernel_size % 2 == 0):
        return 2

    img = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)
    if kernel_type == 'cross':
        kernel = cv2.cv2.getStructuringElement(cv2.MORPH_CROSS, (kernel_size, kernel_size))
    elif kernel_type == 'rectangle':
        kernel = cv2.cv2.getStructuringElement(cv2.MORPH_RECT, (kernel_size, kernel_size))
    else:
        return 2

    result = cv2.erode(img, kernel)
    cv2.imwrite(result_path, result)
    return 1


def dilate(img_name, result_name, kernel_type, kernel_size):
    img_path = 'apps/assets/' + img_name
    result_path = 'apps/results/' + result_name

    try:
        kernel_size = int(kernel_size)
    except ValueError:
        return 2

    if (kernel_size <= 0) or (kernel_size % 2 == 0):
        return 2

    img = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)
    if kernel_type == 'cross':
        kernel = cv2.cv2.getStructuringElement(cv2.MORPH_CROSS, (kernel_size, kernel_size))
    elif kernel_type == 'rectangle':
        kernel = cv2.cv2.getStructuringElement(cv2.MORPH_RECT, (kernel_size, kernel_size))
    else:
        return 2

    result = cv2.dilate(img, kernel)
    cv2.imwrite(result_path, result)
    return 1


def mor_open(img_name, result_name, kernel_type, kernel_size):
    img_path = 'apps/assets/' + img_name
    result_path = 'apps/results/' + result_name

    try:
        kernel_size = int(kernel_size)
    except ValueError:
        return 2

    if (kernel_size <= 0) or (kernel_size % 2 == 0):
        return 2

    img = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)
    if kernel_type == 'cross':
        kernel = cv2.cv2.getStructuringElement(cv2.MORPH_CROSS, (kernel_size, kernel_size))
    elif kernel_type == 'rectangle':
        kernel = cv2.cv2.getStructuringElement(cv2.MORPH_RECT, (kernel_size, kernel_size))
    else:
        return 2

    result = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
    cv2.imwrite(result_path, result)
    return 1


def mor_close(img_name, result_name, kernel_type, kernel_size):
    img_path = 'apps/assets/' + img_name
    result_path = 'apps/results/' + result_name

    try:
        kernel_size = int(kernel_size)
    except ValueError:
        return 2

    if (kernel_size <= 0) or (kernel_size % 2 == 0):
        return 2

    img = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)
    if kernel_type == 'cross':
        kernel = cv2.cv2.getStructuringElement(cv2.MORPH_CROSS, (kernel_size, kernel_size))
    elif kernel_type == 'rectangle':
        kernel = cv2.cv2.getStructuringElement(cv2.MORPH_RECT, (kernel_size, kernel_size))
    else:
        return 2

    result = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
    cv2.imwrite(result_path, result)
    return 1
