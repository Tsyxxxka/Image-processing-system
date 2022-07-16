from flask import Blueprint, request

from apps.service import segmentationService, utils

app = Blueprint('segmentationViews', __name__)


@app.route('/api/segmentation/roberts')
def roberts():
    request_values = request.args
    request_values.to_dict()
    code = segmentationService.roberts(request_values['img_name'], request_values['result_name'], request_values['val1'], request_values['val2'], request_values['exp'])

    if code == 2:
        return utils.wrap_failure_json(request_values['result_name'])

    return utils.wrap_success_json(request_values['result_name'])


@app.route('/api/segmentation/sobel')
def sobel():
    request_values = request.args
    request_values.to_dict()
    code = segmentationService.sobel(request_values['img_name'], request_values['result_name'], request_values['val1'], request_values['val2'], request_values['exp'])

    if code == 2:
        return utils.wrap_failure_json(request_values['result_name'])

    return utils.wrap_success_json(request_values['result_name'])


@app.route('/api/segmentation/laplacian')
def laplacian():
    request_values = request.args
    request_values.to_dict()
    code = segmentationService.laplacian(request_values['img_name'], request_values['result_name'], request_values['kernel_size'], request_values['exp'], request_values['k_size'])

    if code == 2:
        return utils.wrap_failure_json(request_values['result_name'])

    return utils.wrap_success_json(request_values['result_name'])


@app.route('/api/segmentation/LoG')
def LoG():
    request_values = request.args
    request_values.to_dict()
    code = segmentationService.LoG(request_values['img_name'], request_values['result_name'])

    if code == 2:
        return utils.wrap_failure_json(request_values['result_name'])

    return utils.wrap_success_json(request_values['result_name'])


@app.route('/api/segmentation/canny')
def canny():
    request_values = request.args
    request_values.to_dict()
    code = segmentationService.canny(request_values['img_name'], request_values['result_name'], request_values['kernel_size'], request_values['exp'])

    if code == 2:
        return utils.wrap_failure_json(request_values['result_name'])

    return utils.wrap_success_json(request_values['result_name'])


@app.route('/api/segmentation/hough_lines')
def hough_lines():
    request_values = request.args
    request_values.to_dict()
    code = segmentationService.hough_lines(request_values['img_name'], request_values['result_name'])

    if code == 2:
        return utils.wrap_failure_json(request_values['result_name'])

    return utils.wrap_success_json(request_values['result_name'])


@app.route('/api/segmentation/hough_lines_p')
def hough_lines_p():
    request_values = request.args
    request_values.to_dict()
    code = segmentationService.hough_lines_p(request_values['img_name'], request_values['result_name'])

    if code == 2:
        return utils.wrap_failure_json(request_values['result_name'])

    return utils.wrap_success_json(request_values['result_name'])
