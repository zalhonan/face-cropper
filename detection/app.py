import cv2
import numpy as np
from detect import detect
from flask import Flask, request, jsonify
import os

app = Flask(__name__)


@app.route('/')
def root():
    return 'Move alond, nothing to see here'

# получаем картинку, возвращаем масив [[x, y, w, h], [x, y, w, h]]
@app.route('/detection', methods=['GET', 'POST'])
def detection():

    # shorten request to r
    r = request
    # convert string of image data to uint8
    nparr = np.fromstring(r.data, np.uint8)
    # decode image
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # do some fancy processing here....
    res = detect(img)

    if len(res) != 0:
        res = res.tolist()
    else:
        res = []

    # build a response dict to send back to client
    response = {'squares': res}

    return jsonify(response)


if __name__ == '__main__':
    app.debug = True
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
