#!/usr/bin/python3
from flask.helpers import flash
from flask import Flask, render_template, Response, redirect, url_for, request, jsonify
import logging
import sys
import os
from SRAR.detect_model import detect
import cv2
fileName = sys.argv[0]

cwd = os.getcwd()

if fileName.startswith("."):
    PATH = cwd + fileName[1:]
elif fileName.startswith("/"):
    PATH = fileName
else:
    PATH = cwd + "/" + fileName

logging.info(f" PATH to executable {PATH}")

logging.getLogger("imported_module").setLevel(logging.WARNING)
for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)


logging.basicConfig(
    filename=PATH + "-application.log",
    format="%(asctime)s.%(msecs)-3d:%(filename)s:%(funcName)s:%(levelname)s:%(lineno)d:%(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    level=logging.DEBUG,
)
mpl_logger = logging.getLogger("__init__")
mpl_logger.setLevel(logging.ERROR)
EMBED_PATH = os.path.join(cwd, "students_embedding")
app = Flask(__name__)
app.secret_key=os.urandom(24)

''' 
    For video feed
'''
def gen(src):
     
    while True:
        raw_detect, _ = detect(src)
        # cv2.imshow('s',raw_detect)
        yield (
            b"--frame\r\n" b"Content-Type: image/jpeg\r\n\r\n" + raw_detect + b"\r\n"
        )


@app.route("/video", methods=['GET','POST'])
def video():
    if request.method == 'POST':
        src = request.form.get('src')
#     print(src)
    return Response(
        gen(src), mimetype="multipart/x-mixed-replace; boundary=frame" 
    )


@app.route("/", methods=['POST', 'GET'])
def show():
    return render_template("base.html")


            

if __name__ == "__main__":
    app.run(debug=True)
