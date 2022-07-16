#coding=utf8
import os
from flask import send_file, jsonify


def resp_file_upload(file):
    file_name = file.filename
    file_path = 'apps/assets/' + file_name

    if os.path.exists(file_path):
        return {'code': 0, 'msg': '同名文件已存在，保存失败'}
    else:
        file.save(file_path)
        return {'code': 1, 'msg': '保存文件成功'}


def resp_file_download(requ_data):
    file_name = requ_data['file_name']
    file_path = 'apps/results/' + file_name

    if os.path.exists(file_path):
        return send_file(file_path, as_attachment=True)
    else:
        return jsonify({
            'msg': '文件不存在',
        })
