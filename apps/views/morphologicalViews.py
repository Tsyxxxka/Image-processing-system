from flask import Blueprint, request

from apps.service import morphologicalService, utils

app = Blueprint('morphologicalViews', __name__)


@app.route('/api/morphological/erode')
def erode():
    request_values = request.args
    request_values.to_dict()
    code = morphologicalService.erode(request_values['img_name'], request_values['result_name'], request_values['kernel_type'], request_values['kernel_size'])

    if code == 2:
        return utils.wrap_failure_json(request_values['result_name'])

    return utils.wrap_success_json(request_values['result_name'])


@app.route('/api/morphological/dilate')
def dilate():
    request_values = request.args
    request_values.to_dict()
    code = morphologicalService.dilate(request_values['img_name'], request_values['result_name'], request_values['kernel_type'], request_values['kernel_size'])

    if code == 2:
        return utils.wrap_failure_json(request_values['result_name'])

    return utils.wrap_success_json(request_values['result_name'])


@app.route('/api/morphological/mor_open')
def mor_open():
    request_values = request.args
    request_values.to_dict()
    code = morphologicalService.mor_open(request_values['img_name'], request_values['result_name'], request_values['kernel_type'], request_values['kernel_size'])

    if code == 2:
        return utils.wrap_failure_json(request_values['result_name'])

    return utils.wrap_success_json(request_values['result_name'])


@app.route('/api/morphological/mor_close')
def mor_close():
    request_values = request.args
    request_values.to_dict()
    code = morphologicalService.mor_close(request_values['img_name'], request_values['result_name'], request_values['kernel_type'], request_values['kernel_size'])

    if code == 2:
        return utils.wrap_failure_json(request_values['result_name'])

    return utils.wrap_success_json(request_values['result_name'])