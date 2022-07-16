from flask import Blueprint, request

from apps.service import smoothSharpenService, utils

app = Blueprint('smoothSharpenViews', __name__)


@app.route('/api/smooth_sharpen/smoo_neighbour_average')
def smoo_neighbour_average():
    request_values = request.args
    request_values.to_dict()
    code = smoothSharpenService.smoo_neighbour_average(request_values['img_name'], request_values['result_name'],
                                                       request_values['kernel_size'])

    if code == 2:
        return utils.wrap_failure_json(request_values['result_name'])

    return utils.wrap_success_json(request_values['result_name'])


@app.route('/api/smooth_sharpen/smoo_median_filter')
def smoo_median_filter():
    request_values = request.args
    request_values.to_dict()
    code = smoothSharpenService.smoo_median_filter(request_values['img_name'], request_values['result_name'],
                                                   request_values['kernel_size'])

    if code == 2:
        return utils.wrap_failure_json(request_values['result_name'])

    return utils.wrap_success_json(request_values['result_name'])


@app.route('/api/smooth_sharpen/shar_robert')
def shar_robert():
    request_values = request.args
    request_values.to_dict()
    code = smoothSharpenService.shar_robert(request_values['img_name'], request_values['result_name'])

    if code == 2:
        return utils.wrap_failure_json(request_values['result_name'])

    return utils.wrap_success_json(request_values['result_name'])


@app.route('/api/smooth_sharpen/shar_laplacian')
def shar_laplacian():
    request_values = request.args
    request_values.to_dict()
    code = smoothSharpenService.shar_laplacian(request_values['img_name'], request_values['result_name'])

    if code == 2:
        return utils.wrap_failure_json(request_values['result_name'])

    return utils.wrap_success_json(request_values['result_name'])


@app.route('/api/smooth_sharpen/shar_sobel')
def shar_sobel():
    request_values = request.args
    request_values.to_dict()
    code = smoothSharpenService.shar_sobel(request_values['img_name'], request_values['result_name'])

    if code == 2:
        return utils.wrap_failure_json(request_values['result_name'])

    return utils.wrap_success_json(request_values['result_name'])


@app.route('/api/smooth_sharpen/shar_prewitt')
def shar_prewitt():
    request_values = request.args
    request_values.to_dict()
    code = smoothSharpenService.shar_prewitt(request_values['img_name'], request_values['result_name'])

    if code == 2:
        return utils.wrap_failure_json(request_values['result_name'])

    return utils.wrap_success_json(request_values['result_name'])


@app.route('/api/smooth_sharpen/smoo_ideal_filter')
def smoo_ideal_filter():
    request_values = request.args
    request_values.to_dict()
    code = smoothSharpenService.smoo_ideal_filter(request_values['img_name'], request_values['result_name'], request_values['d0'])

    if code == 2:
        return utils.wrap_failure_json(request_values['result_name'])

    return utils.wrap_success_json(request_values['result_name'])


@app.route('/api/smooth_sharpen/smoo_barte_filter')
def smoo_barte_filter():
    request_values = request.args
    request_values.to_dict()
    code = smoothSharpenService.smoo_barte_filter(request_values['img_name'], request_values['result_name'], request_values['d0'], request_values['rank'])

    if code == 2:
        return utils.wrap_failure_json(request_values['result_name'])

    return utils.wrap_success_json(request_values['result_name'])


@app.route('/api/smooth_sharpen/smoo_exp_filter')
def smoo_exp_filter():
    request_values = request.args
    request_values.to_dict()
    code = smoothSharpenService.smoo_exp_filter(request_values['img_name'], request_values['result_name'], request_values['d0'], request_values['rank'])

    if code == 2:
        return utils.wrap_failure_json(request_values['result_name'])

    return utils.wrap_success_json(request_values['result_name'])


@app.route('/api/smooth_sharpen/shar_ideal_high')
def shar_ideal_high():
    request_values = request.args
    request_values.to_dict()
    code = smoothSharpenService.shar_ideal_high(request_values['img_name'], request_values['result_name'], request_values['d0'])

    if code == 2:
        return utils.wrap_failure_json(request_values['result_name'])

    return utils.wrap_success_json(request_values['result_name'])


@app.route('/api/smooth_sharpen/shar_barte_filter')
def shar_barte_filter():
    request_values = request.args
    request_values.to_dict()
    code = smoothSharpenService.shar_barte_filter(request_values['img_name'], request_values['result_name'], request_values['d0'], request_values['rank'])

    if code == 2:
        return utils.wrap_failure_json(request_values['result_name'])

    return utils.wrap_success_json(request_values['result_name'])


@app.route('/api/smooth_sharpen/shar_exp_filter')
def shar_exp_filter():
    request_values = request.args
    request_values.to_dict()
    code = smoothSharpenService.shar_exp_filter(request_values['img_name'], request_values['result_name'], request_values['d0'], request_values['rank'])

    if code == 2:
        return utils.wrap_failure_json(request_values['result_name'])

    return utils.wrap_success_json(request_values['result_name'])


