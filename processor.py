import json
import pyjq
import re
import urllib.request
import ssl
from config import config

class txtProcessor:
  def __init__(self):
    self.rules = self.LoadJsonFromFile('rules.json')
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
    response = urllib.request.urlopen(self.conf['DomoticzAPIUrl'] + query, context=ctx)
    data = response.read()
    j = json.loads(data.decode("utf-8"))
    return pyjq.first(jq, j)

  def ExtractNumber(self, phrase):
    nr = ''.join([n for n in phrase if n.isdigit()])
    return nr

  def GoProcess(self, phrase):
    for rule in self.rules:
      if bool(re.search(rule['elicitation_pattern'], phrase, re.IGNORECASE)):
        for device in rule['devices']:
          if bool(re.search(device['name_pattern'], phrase, re.IGNORECASE)):
            query = device['query']
            nr = self.ExtractNumber(phrase)
            query = re.sub('\{\{number\}\}', str(nr), query)
            domoticzValue = self.GetDomoticzValue(query, device['return'])
            reply = device['reply']
            reply = re.sub('\{\{return\}\}', str(domoticzValue), reply)
            reply = re.sub('\{\{number\}\}', str(nr), reply)
            return reply

