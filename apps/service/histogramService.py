#coding=utf8
import cv2
from matplotlib import pyplot as plt


def gray_histogram(img_name, result_name):
    img_path = 'apps/assets/' + img_name
    result_path = 'apps/results/' + result_name

    img = cv2.imread(img_path, 0)
    plt.subplot(121)
    plt.imshow(img, "gray")
    plt.subplot(122)
    hist = cv2.calcHist([img], [0], None, [256], [0, 255])
    plt.plot(hist)
    plt.xlim([0, 255])
    plt.savefig(result_path)
    return 1


def bgr_histogram(img_name, result_name):
    img_path = 'apps/assets/' + img_name
    result_path = 'apps/results/' + result_name

    img = cv2.imread(img_path)
    color = ["r", "g", "b"]
    img_b, img_g, img_r = cv2.split(img)
    img = cv2.merge([img_r, img_g, img_b])
    plt.subplot(121)
    plt.imshow(img)
    plt.subplot(122)
    for index, c in enumerate(color):
        hist = cv2.calcHist([img], [index], None, [256], [0, 255])

        plt.plot(hist, color=c)
        plt.xlim([0, 255])
    plt.savefig(result_path)
    return 1
