#!/usr/bin/env python3

from flask import Flask, request, json
from config import config
from processor import txtProcessor
import logging
import os,signal,sys

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

txtp = txtProcessor()
conf = config.GetConfig(None)
app = Flask(__name__)

@app.route("/directask")
def ask():
  text = request.args.get("text")
  ga = request.args.get("ga")
  if not text:
    loging.info('text required')
    return False
  logging.info("Input text: " + text)
  ar = txtp.GoProcess(text=text, ga=ga)
  logging.info("Output text: " + ar)
  return ar

@app.route('/ask', methods = ['POST'])
def change_groups():
  if not request.json:
    logging.info("No json format")
    return False
  if not 'text' in request.json:
    looging.into("text is required")
    return False
  text = request.json['text']
  if 'ga' in request.json: ga = request.json['ga']
  else: ga = 0
  logging.info("Input text: " + text)
  ar = txtp.GoProcess(text=text, ga=ga)
  logging.info("Output text: " + ar)
  return ar

def set_exit_handler(func):
    signal.signal(signal.SIGTERM, func)

def on_exit(sig, func=None):
    print("exit handler triggered")
    sys.exit(1)

if __name__ == '__main__':
  host=conf['WebServiceAddress']
  port=conf['WebServicePort']

  print("\n ======== Welcome to VoiceMoticz webservice ========= ")
  print("| VoiceMoticz is voice controller for Domoticz       |")
  print("| version: 0.9.0                                     |")
  print("| author: https://github.com/z1mEk                   |")
  print(" ==================================================== ")

  set_exit_handler(on_exit)
  app.run(host=host, port=port)

