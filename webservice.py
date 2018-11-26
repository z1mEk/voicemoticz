#!/usr/bin/env python3

from flask import Flask, request
import json

app = Flask(__name__)

@app.route("/say")
def say():
    text = request.args.get("text")
    return "Hello World!"

@app.route("/test/<filename>")
def test(filename):
    return filename

@app.route('/foo', methods=['POST']) 
def foo():
    if not request.json:
        abort(400)
    print request.json
    return json.dumps(request.json)
    
if __name__ == '__main__':
app.run(host='0.0.0.0', port=8082) 
