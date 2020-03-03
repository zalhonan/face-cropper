"""
пример сервера на Flask
принимает на /reverse одну строчку по GET и POST
возвращает её же, в обратном порядке
как пример проекта для работы с текстами

принимает на /file картинку
"""

import uuid
import json
import cv2
import requests
import os
import numpy as np
from flask_cors import CORS
from flask import Flask, jsonify, request, send_from_directory


detect_hostname = 'http://localhost:5000'
detect_url = detect_hostname + '/detection'
myhostname = 'http://localhost:5050'

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

# возвращаем картинки по адресу например http://localhost:5050/pics/2/3.jpg
@app.route('/pics/<path:path>')
def send_pics(path):
    return send_from_directory('pics', path)


@app.route('/file', methods=['GET', 'POST'])
def file():
    if request.method == 'GET' or request.method == 'POST':
        # convert string of image data to uint8
        nparr = np.frombuffer(request.data, np.uint8)
        print('---------------------------')
        # print(request.data)
        # decode image
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        # сохраним текущую картинку
        pic_path = "./pics/" + str(uuid.uuid1()) + "/"
        os.mkdir(pic_path)
        filename = pic_path + str(uuid.uuid1()) + '.jpg'
        cv2.imwrite(filename, img)

        # сюда складываем ссылки на картинки. 1-я - исходный пик
        pic_responce = []
        pic_responce.append(myhostname + filename[1:])
        print(pic_responce)

        # encode image as jpeg
        _, img_encoded = cv2.imencode('.jpg', img)
        # send http request with image and receive response
        # prepare headers for http request
        content_type = 'image/jpeg'
        headers = {'content-type': content_type}
        response = requests.post(
            detect_url, data=img_encoded.tostring(), headers=headers)
        # decode and print response
        resp = response.text
        resp = json.loads(resp)['squares']

        # # если ответ нулевой - то вернуть просто ссылку на фотку
        if len(resp[0]) == 0:
            return jsonify(pic_responce)

        # нарисовать на основной картинке квадратики и сохранить её
        for square in resp:
            x, y, h, w = square
            color = (255, 255, 0)
            thickness = 2
            img = cv2.rectangle(img, (x, y), (x + h, y + w), color, thickness)
        filename = pic_path + str(uuid.uuid1()) + '.jpg'
        cv2.imwrite(filename, img)

        pic_responce.append(myhostname + filename[1:])
        print(pic_responce)

        # пройти по координатам и вырезать фотки
        # сохранить каждую в uuid имя
        for square in resp:
            x, y, h, w = square
            color = (255, 255, 0)
            thickness = 2
            crop_img = img[y:y+h, x:x+w]
            filename = pic_path + str(uuid.uuid1()) + '.jpg'
            cv2.imwrite(filename, crop_img)
            pic_responce.append(myhostname + filename[1:])

        # filename = pic_path + str(uuid.uuid1()) + '.jpg'
        # cv2.imwrite(filename, img)

        # вернуть массив со ссылками на эти имена

        return jsonify(pic_responce)


@app.route('/reverse',  methods=['GET', 'POST'])
def reverse():
    if request.method == 'GET' or request.method == 'POST':
        print('-------------', list(request.args))
        line = request.args.get('line', 'no line parameter here')
        reversed_line = line[::-1]
        return jsonify(reversed_line)


if __name__ == '__main__':
    app.debug = True
    port = int(os.environ.get("PORT", 5050))
    app.run(host='0.0.0.0', port=port)
