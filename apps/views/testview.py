from flask import Blueprint, request, jsonify

app = Blueprint('testview', __name__)


@app.route('/api/test')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/api/testinput')
def hello_test():  # put application's code here
    requestValues = request.args
    requestValues.to_dict()
    return jsonify(requestValues)
