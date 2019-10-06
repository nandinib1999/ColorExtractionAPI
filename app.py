# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 17:29:48 2019

@author: agilist
"""

import dominantColors as dmcolor
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from PIL import Image


app = Flask(__name__)
api = Api(app)

@app.route("/")
def home_page():
    return "<h1>Welcome!!!</h1>"

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

@app.route("/home/<int:clusters>", methods=["POST"])
def home(clusters):
    print("Success")
    return jsonify(dmcolor.start(request.files['files'], clusters))                        

if __name__ == '__main__':
    app.debug = True
    app.run()