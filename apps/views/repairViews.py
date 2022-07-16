from flask import Blueprint, request

from apps.service import repairService, utils

app = Blueprint('repairViews', __name__)


@app.route('/api/repair/gauss_noise')
def gauss_noise():
    request_values = request.args
    request_values.to_dict()
    code = repairService.gauss_noise(request_values['img_name'], request_values['result_name'])

    if code == 2:
        return utils.wrap_failure_json(request_values['result_name'])

    return utils.wrap_success_json(request_values['result_name'])


@app.route('/api/repair/sault_pepper_noise')
def sault_pepper_noise():
    request_values = request.args
    request_values.to_dict()
    code = repairService.sault_pepper_noise(request_values['img_name'], request_values['result_name'], request_values['ran_x1'], request_values['ran_y1'], request_values['ran_x2'], request_values['ran_y2'])

    if code == 2:
        return utils.wrap_failure_json(request_values['result_name'])

    return utils.wrap_success_json(request_values['result_name'])


@app.route('/api/repair/arithmetic_average_filter')
def arithmetic_average_filter():
    request_values = request.args
    request_values.to_dict()
    code = repairService.arithmetic_average_filter(request_values['img_name'], request_values['result_name'], request_values['filter_size_p'], request_values['filter_size_q'])

    if code == 2:
        return utils.wrap_failure_json(request_values['result_name'])

    return utils.wrap_success_json(request_values['result_name'])


@app.route('/api/repair/geometric_average_filter')
def geometric_average_filter():
    request_values = request.args
    request_values.to_dict()
    code = repairService.geometric_average_filter(request_values['img_name'], request_values['result_name'], request_values['filter_size_p'], request_values['filter_size_q'])

    if code == 2:
        return utils.wrap_failure_json(request_values['result_name'])

    return utils.wrap_success_json(request_values['result_name'])


@app.route('/api/repair/harmonic_average_filter')
def harmonic_average_filter():
    request_values = request.args
    request_values.to_dict()
    code = repairService.harmonic_average_filter(request_values['img_name'], request_values['result_name'], request_values['filter_size_p'], request_values['filter_size_q'])

    if code == 2:
        return utils.wrap_failure_json(request_values['result_name'])

    return utils.wrap_success_json(request_values['result_name'])


@app.route('/api/repair/min_filter')
def min_filter():
    request_values = request.args
    request_values.to_dict()
    code = repairService.min_filter(request_values['img_name'], request_values['result_name'])

    if code == 2:
        return utils.wrap_failure_json(request_values['result_name'])

    return utils.wrap_success_json(request_values['result_name'])


@app.route('/api/repair/max_filter')
def max_filter():
    request_values = request.args
    request_values.to_dict()
    code = repairService.max_filter(request_values['img_name'], request_values['result_name'])

    if code == 2:
        return utils.wrap_failure_json(request_values['result_name'])

    return utils.wrap_success_json(request_values['result_name'])


@app.route('/api/repair/median_filter')
def median_filter():
    request_values = request.args
    request_values.to_dict()
    code = repairService.median_filter(request_values['img_name'], request_values['result_name'])

    if code == 2:
        return utils.wrap_failure_json(request_values['result_name'])

    return utils.wrap_success_json(request_values['result_name'])


@app.route('/api/repair/range_filter')
def range_filter():
    request_values = request.args
    request_values.to_dict()
    code = repairService.range_filter(request_values['img_name'], request_values['result_name'], request_values['min'], request_values['max'], request_values['color'])

    if code == 2:
        return utils.wrap_failure_json(request_values['result_name'])

    return utils.wrap_success_json(request_values['result_name'])
