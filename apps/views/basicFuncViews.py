from flask import Blueprint, request

from apps.service import basicFuncService, utils

app = Blueprint('basicFuncViews', __name__)


@app.route('/api/basic_func/graying')
def graying():
    request_values = request.args
    request_values.to_dict()
    code = basicFuncService.graying(request_values['img_name'], request_values['result_name'])

    if code == 2:
        return utils.wrap_failure_json(request_values['result_name'])

    return utils.wrap_success_json(request_values['result_name'])


@app.route('/api/basic_func/thresholding')
def thresholding():
    request_values = request.args
    request_values.to_dict()
    code = basicFuncService.thresholding(request_values['img_name'], request_values['result_name'])

    if code == 2:
        return utils.wrap_failure_json(request_values['result_name'])

    return utils.wrap_success_json(request_values['result_name'])


@app.route('/api/basic_func/logical_and')
def logical_and():
    request_values = request.args
    request_values.to_dict()
    code = basicFuncService.logical_and(request_values['img_name1'], request_values['img_name2'], request_values['result_name'])

    if code == 2:
        return utils.wrap_failure_json(request_values['result_name'])

    return utils.wrap_success_json(request_values['result_name'])


@app.route('/api/basic_func/logical_or')
def logical_or():
    request_values = request.args
    request_values.to_dict()
    code = basicFuncService.logical_or(request_values['img_name1'], request_values['img_name2'], request_values['result_name'])

    if code == 2:
        return utils.wrap_failure_json(request_values['result_name'])

    return utils.wrap_success_json(request_values['result_name'])


@app.route('/api/basic_func/logical_not')
def logical_not():
    request_values = request.args
    request_values.to_dict()
    code = basicFuncService.logical_not(request_values['img_name'], request_values['result_name'])

    if code == 2:
        return utils.wrap_failure_json(request_values['result_name'])

    return utils.wrap_success_json(request_values['result_name'])


@app.route('/api/basic_func/add')
def add():
    request_values = request.args
    request_values.to_dict()
    code = basicFuncService.add(request_values['img_name1'], request_values['img_name2'], request_values['result_name'])

    if code == 2:
        return utils.wrap_failure_json(request_values['result_name'])

    return utils.wrap_success_json(request_values['result_name'])


@app.route('/api/basic_func/subtract')
def subtract():
    request_values = request.args
    request_values.to_dict()
    code = basicFuncService.subtract(request_values['img_name1'], request_values['img_name2'], request_values['result_name'])

    if code == 2:
        return utils.wrap_failure_json(request_values['result_name'])

    return utils.wrap_success_json(request_values['result_name'])


@app.route('/api/basic_func/multiply')
def multiply():
    request_values = request.args
    request_values.to_dict()
    code = basicFuncService.multiply(request_values['img_name1'], request_values['img_name2'], request_values['result_name'])

    if code == 2:
        return utils.wrap_failure_json(request_values['result_name'])

    return utils.wrap_success_json(request_values['result_name'])


@app.route('/api/basic_func/divide')
def divide():
    request_values = request.args
    request_values.to_dict()
    code = basicFuncService.divide(request_values['img_name1'], request_values['img_name2'], request_values['result_name'])

    if code == 2:
        return utils.wrap_failure_json(request_values['result_name'])

    return utils.wrap_success_json(request_values['result_name'])


@app.route('/api/basic_func/flip')
def flip():
    request_values = request.args
    request_values.to_dict()
    code = basicFuncService.flip(request_values['img_name'], request_values['result_name'], request_values['fli_choi'])

    if code == 2:
        return utils.wrap_failure_json(request_values['result_name'])

    return utils.wrap_success_json(request_values['result_name'])


@app.route('/api/basic_func/move')
def move():
    request_values = request.args
    request_values.to_dict()
    code = basicFuncService.move(request_values['img_name'], request_values['result_name'], request_values['move_x']
                          , request_values['move_y'])

    if code == 2:
        return utils.wrap_failure_json(request_values['result_name'])

    return utils.wrap_success_json(request_values['result_name'])


@app.route('/api/basic_func/rotate')
def rotate():
    request_values = request.args
    request_values.to_dict()
    code = basicFuncService.rotate(request_values['img_name'], request_values['result_name'], request_values['angle'])

    if code == 2:
        return utils.wrap_failure_json(request_values['result_name'])

    return utils.wrap_success_json(request_values['result_name'])


@app.route('/api/basic_func/resize')
def resize():
    request_values = request.args
    request_values.to_dict()
    code = basicFuncService.resize(request_values['img_name'], request_values['result_name'], request_values['size_x']
                          , request_values['size_y'])

    if code == 2:
        return utils.wrap_failure_json(request_values['result_name'])

    return utils.wrap_success_json(request_values['result_name'])
