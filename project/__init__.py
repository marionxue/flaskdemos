# -*- coding: utf-8 -*-
"""
File Name:       __init__
Description :
Author :         marion
date:            2020-01-21
Change Activity: 2020-01-21
IDE:             PyCharm
"""
# python
from flask import Flask,jsonify

app= Flask(__name__)
app.config.from_object('project.config.DevelopmentConfig')

@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify({
        'status': 'success',
        'message': 'pong!'
    })