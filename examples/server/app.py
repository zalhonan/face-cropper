"""
пример сервера на Flask
принимает на /string одну строчку по GET и POST
возвращает её же, в обратном порядке
как пример проекта для работы с текстами
"""

from flask import Flask, jsonify, request, send_file
from flask_cors import CORS, cross_origin
import os
import cv2
import numpy as np

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
# CORS(app, resources={r'/*': {'origins': '*'}})
cors = CORS(app)


@app.route('/',  methods=['GET', 'POST'])
def index():
    return jsonify("Nothing to see here")


@app.route('/pic', methods=['GET', 'POST'])
def pic():
    if request.method in ['GET', 'POST']:
        filename = "2.jpg"
        return (send_file(filename, mimetype='image/png'))


@app.route('/pic2', methods=['GET', 'POST'])
def pic2():
    if request.method in ['GET', 'POST']:
        return jsonify('-----file ok-------')


@app.route('/file', methods=['GET', 'POST'])
def file():
    if request.method == 'GET' or request.method == 'POST':
        # convert string of image data to uint8
        nparr = np.frombuffer(request.data, np.uint8)
        print('---------------------------')
        # print(request.data)
        # decode image
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        cv2.imwrite('filename.jpg', img)
        return jsonify('-----file ok-------')


@app.route('/reverse',  methods=['GET', 'POST'])
def reverse():
    if request.method == 'GET' or request.method == 'POST':
        print('-------------', list(request.args))
        line = request.args.get('line', 'no line parameter here')
        reversed_line = line[::-1]
        return jsonify(reversed_line)


if __name__ == '__main__':
    app.debug = True
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
