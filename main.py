  
from flask import Flask, render_template, request
import flask
import requests
import os
import sys

app = Flask(__name__)



@app.route('/',methods=['GET'])
def hello():
    if request.method == 'GET':
            return "BEM-VINDO AO ENDPOINT DA API-Thumb"
    else:
        return "ERRO"


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5050)
