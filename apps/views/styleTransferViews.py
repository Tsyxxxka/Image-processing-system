from flask import Blueprint, request

from apps.service import styleTransferService, utils

app = Blueprint('styleTransferViews', __name__)


@app.route('/api/styleTransfer/style_transfer')
def style_transfer():
    request_values = request.args
    request_values.to_dict(),
    code = styleTransferService.style_transfer(request_values['img_style_name'], request_values['img_content_name'], request_values['result_name'])

    print("qqqqqq")
    if code == 2:
        return utils.wrap_failure_json(request_values['result_name'])

    return utils.wrap_success_json(request_values['result_name'])