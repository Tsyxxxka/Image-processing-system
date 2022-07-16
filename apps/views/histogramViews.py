from flask import Blueprint, request
from apps.service import histogramService, utils

app = Blueprint('histogramViews', __name__)


@app.route('/api/histogram/gray')
def gray_histogram():
    request_values = request.args
    request_values.to_dict()
    code = histogramService.gray_histogram(request_values['img_name'], request_values['result_name'])

    if code == 2:
        return utils.wrap_failure_json(request_values['result_name'])

    return utils.wrap_success_json(request_values['result_name'])


@app.route('/api/histogram/bgr')
def bgr_histogram():
    request_values = request.args
    request_values.to_dict()
    code = histogramService.bgr_histogram(request_values['img_name'], request_values['result_name'])

    if code == 2:
        return utils.wrap_failure_json(request_values['result_name'])

    return utils.wrap_success_json(request_values['result_name'])
