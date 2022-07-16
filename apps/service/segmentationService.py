#coding=utf8
import cv2
import numpy as np


def roberts(img_name, result_name, val1, val2, exp):
    img_path = 'apps/assets/' + img_name
    result_path = 'apps/results/' + result_name

    try:
        val1 = float(val1)
        val2 = float(val2)
        exp = float(exp)
    except ValueError:
        return 2

    if (val1 < 0) or (val2 < 0):
        return 2

    img = cv2.imread(img_path)
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    kernel_x = np.array([[-1, 0], [0, 1]], dtype=int)
    kernel_y = np.array([[0, -1], [1, 0]], dtype=int)

    cal_x = cv2.filter2D(gray_image, cv2.CV_16S, kernel_x)
    cal_y = cv2.filter2D(gray_image, cv2.CV_16S, kernel_y)

    abs_x = cv2.convertScaleAbs(cal_x)
    abs_y = cv2.convertScaleAbs(cal_y)

    roberts_res = cv2.addWeighted(abs_x, val1, abs_y, val2, exp)

    cv2.imwrite(result_path, roberts_res)
    return 1


def sobel(img_name, result_name, val1, val2, exp):
    img_path = 'apps/assets/' + img_name
    result_path = 'apps/results/' + result_name

    try:
        val1 = float(val1)
        val2 = float(val2)
        exp = float(exp)
    except ValueError:
        return 2

    if (val1 < 0) or (val2 < 0):
        return 2

    img = cv2.imread(img_path)
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    kernel_x = cv2.Sobel(gray_image, cv2.CV_16S, 1, 0)
    kernel_y = cv2.Sobel(gray_image, cv2.CV_16S, 0, 1)

    abs_x = cv2.convertScaleAbs(kernel_x)
    abs_y = cv2.convertScaleAbs(kernel_y)

    sobel_res = cv2.addWeighted(abs_x, val1, abs_y, val2, exp)

    cv2.imwrite(result_path, sobel_res)
    return 1


def laplacian(img_name, result_name, kernel_size, exp, k_size):
    img_path = 'apps/assets/' + img_name
    result_path = 'apps/results/' + result_name

    try:
        kernel_size = int(kernel_size)
        exp = float(exp)
        k_size = int(k_size)
    except ValueError:
        return 2

    if (kernel_size <= 0) or (kernel_size % 2 == 0) or (k_size <= 0) or (k_size % 2 == 0):
        return 2

    img = cv2.imread(img_path)
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    blur = cv2.GaussianBlur(gray_image, (kernel_size, kernel_size), exp)

    dst = cv2.Laplacian(blur, cv2.CV_16S, ksize=k_size)

    laplacian_res = cv2.convertScaleAbs(dst)

    cv2.imwrite(result_path, laplacian_res)
    return 1


def LoG(img_name, result_name):
    img_path = 'apps/assets/' + img_name
    result_path = 'apps/results/' + result_name

    img = cv2.imread(img_path)

    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    image = cv2.copyMakeBorder(img, 2, 2, 2, 2, borderType=cv2.BORDER_REPLICATE)
    image = cv2.GaussianBlur(image, (3, 3), 0, 0)
    LoGMatr = [[0, 0, -1, 0, 0], [0, -1, -2, -1, 0], [-1, -2, 16, -2, -1], [0, -1, -2, -1, 0], [0, 0, -1, 0, 0]]
    img_m1 = np.array(LoGMatr)

    rows = image.shape[0]
    cols = image.shape[1]

    image1 = np.zeros(image.shape)

    for k in range(0, 2):
        for i in range(2, rows - 2):
            for j in range(2, cols - 2):
                image1[i, j] = np.sum((img_m1 * image[i - 2:i + 3, j - 2:j + 3, k]))

    image1 = cv2.convertScaleAbs(image1)

    cv2.imwrite(result_path, image1)
    return 1


def canny(img_name, result_name, kernel_size, exp):
    img_path = 'apps/assets/' + img_name
    result_path = 'apps/results/' + result_name

    try:
        kernel_size = int(kernel_size)
        exp = float(exp)
    except ValueError:
        return 2

    if (kernel_size <= 0) or (kernel_size % 2 == 0):
        return 2

    img = cv2.imread(img_path)
    blur = cv2.GaussianBlur(img, (kernel_size, kernel_size), exp)

    gray_image = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)

    grad_x = cv2.Sobel(gray_image, cv2.CV_16SC1, 1, 0)
    grad_y = cv2.Sobel(gray_image, cv2.CV_16SC1, 0, 1)

    edge_output = cv2.Canny(grad_x, grad_y, 50, 150)

    cv2.imwrite(result_path, edge_output)
    return 1


def hough_lines(img_name, result_name):
    img_path = 'apps/assets/' + img_name
    result_path = 'apps/results/' + result_name

    img = cv2.imread(img_path)

    img = cv2.GaussianBlur(img, (3, 3), 0)
    edges = cv2.Canny(img, 50, 150, apertureSize=3)

    lines = cv2.HoughLines(edges, 1, np.pi / 2, 118)

    result = img.copy()
    for i_line in lines:
        for line in i_line:
            rho = line[0]
            theta = line[1]
            if (theta < (np.pi / 4.)) or (theta > (3. * np.pi / 4.0)):  # 垂直直线
                pt1 = (int(rho / np.cos(theta)), 0)
                pt2 = (int((rho - result.shape[0] * np.sin(theta)) / np.cos(theta)), result.shape[0])
                cv2.line(result, pt1, pt2, (0, 0, 255))
            else:
                pt1 = (0, int(rho / np.sin(theta)))
                pt2 = (result.shape[1], int((rho - result.shape[1] * np.cos(theta)) / np.sin(theta)))
                cv2.line(result, pt1, pt2, (0, 0, 255), 1)

    cv2.imwrite(result_path, result)
    return 1


def hough_lines_p(img_name, result_name):
    img_path = 'apps/assets/' + img_name
    result_path = 'apps/results/' + result_name

    img = cv2.imread(img_path)

    img = cv2.GaussianBlur(img, (3, 3), 0)
    edges = cv2.Canny(img, 50, 150, apertureSize=3)

    min_line_length = 200
    max_line_gap = 15

    lines_p = cv2.HoughLinesP(edges, 1, np.pi / 180, 80, min_line_length, max_line_gap)

    result_p = img.copy()
    for i_P in lines_p:
        for x1, y1, x2, y2 in i_P:
            cv2.line(result_p, (x1, y1), (x2, y2), (0, 255, 0), 3)

    cv2.imwrite(result_path, result_p)
    return 1
