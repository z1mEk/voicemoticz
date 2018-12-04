import json
import pyjq
import re
from urllib.request import Request, urlopen
import ssl
from config import config
import os

class txtProcessor:
  def __init__(self):
    filename = os.path.dirname(__file__) + '/config/rules.json'
    self.rules = self.LoadJsonFromFile(filename)
    self.conf = config.GetConfig(self)

  def LoadJsonFromFile(self, filename):
    with open(filename) as f:
      data = json.load(f)
    return data

  def GetDomoticzValue(self, query, jq):
    ctx = ''
    if self.conf['DomoticzIgnoreSSLCert'] == 1:
      ctx = ssl.create_default_context()
      ctx.check_hostname = False
      ctx.verify_mode = ssl.CERT_NONE
    req = Request(self.conf['DomoticzAPIUrl'] + query)
    response = urlopen(req, context=ctx)
    data = response.read()
    j = json.loads(data.decode("utf-8"))
    return pyjq.first(jq, j)

  def ExtractNumber(self, phrase):
    nr = re.findall("\d+\.\d+|\d+,\d+|\d+", phrase)
    if len(nr) > 0: 
      return re.sub(',', '.', nr[0])
    else: return ''


  def GoProcess(self, text="", ga=0):
    for rule in self.rules:
      if bool(re.search(rule['elicitation_pattern'], text, re.IGNORECASE)):
        for device in rule['devices']:
          if bool(re.search(device['name_pattern'], text, re.IGNORECASE)):
            query = device['query']
            nr = self.ExtractNumber(text)
            query = re.sub('\{\{number\}\}', str(nr), query)
            domoticzValue = self.GetDomoticzValue(query, device['return'])
            reply = device['reply']
            reply = re.sub('\{\{return\}\}', str(domoticzValue), reply)
            reply = re.sub('\{\{number\}\}', str(nr), reply)
            return reply
        if 'reply_unknown' in rule:
          return rule['reply_unknown']
    return self.conf['reply_unknown']
