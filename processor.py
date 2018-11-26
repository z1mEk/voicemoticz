import json
import pyjq
import re

class txtProcessor:
  def __init__(self):
    self.rules = self.LoadJsonFromFile('rules.json')
    
  def LoadJsonFromFile(self, filename):
    with open(filename) as f:
      data = json.load(f)
    return data

  def GetDomoticzValue(self, query, jq):
    #TODO
    return 0
  
  def GoProcess(self, phrase, _number, _text):
    for rule in self.rules:
      if bool(re.search(rule['elicitation_pattern'], phrase)):
        for device in rule['devices']:
          if bool(re.search(device['name_pattern'], phrase)):
            query = device['query']
            query = re.sub('\{\{number\}\}', str(_number), query)
            query = re.sub('\{\{text\}\}', _text, query)
            domoticzValue = self.GetDomoticzValue(query, device['return'])
            reply = device['reply']
            reply = re.sub('\{\{return\}\}', str(domoticzValue), reply)
            reply = re.sub('\{\{number\}\}', str(_number), reply)
            reply = re.sub('\{\{text\}\}', _text, reply)
            return reply
            
