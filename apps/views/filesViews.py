#coding=utf8
import os

from flask import Blueprint, jsonify, request, send_file

from apps.service.filesService import resp_file_upload, resp_file_download

app = Blueprint('filesView', __name__)


@app.route('/api/file/upload', methods=['POST'])
def file_upload():
    file = request.files['file']
    resp_data = resp_file_upload(file)

    return jsonify(resp_data)


@app.route('/api/file/download', methods=['POST'])
def file_download():
    requ_data = request.json
    return resp_file_download(requ_data)


@app.route('/api/get_ori_file/<file_name>', methods=['GET'])
def get_ori_file(file_name):
    file_path = os.path.join('assets/', file_name)

    # 向api返回（图片）文件
    return send_file(file_path)


@app.route('/api/get_res_file/<file_name>', methods=['GET'])
def get_res_file(file_name):
    file_path = os.path.join('results/', file_name)

    # 向api返回（图片）文件
    return send_file(file_path)
