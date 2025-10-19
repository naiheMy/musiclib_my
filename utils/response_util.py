from flask import jsonify

def make_response(code=200, data=None, message=''):
    return jsonify({
        'code': code,
        'data': data,
        'message': message
    })