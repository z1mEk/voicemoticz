import json
import pyjq
import re
import Requests

class txtProcessor:
  def __init__(self):
    self.rules = self.LoadJsonFromFile('rules.json')
    
  def LoadJsonFromFile(self, filename):
    with open(filename) as f:
      data = json.load(f)
    return data

  def GetDomoticzValue(self, query, jq):
    #TODO Domoticz Request
    data = ''
    return pyjq.first(jq, data)
  
  def GetNumberFromPharse(self, phrase):
    return ''
  
  def GoProcess(self, phrase):
    for rule in self.rules:
      if bool(re.search(rule['elicitation_pattern'], phrase)):
        for device in rule['devices']:
          if bool(re.search(device['name_pattern'], phrase)):
            query = device['query']
            _number = self.GetNumberFromPharse(pharse)
            query = re.sub('\{\{number\}\}', str(_number), query)
            domoticzValue = self.GetDomoticzValue(query, device['return'])
            reply = device['reply']
            reply = re.sub('\{\{return\}\}', str(domoticzValue), reply)
            reply = re.sub('\{\{number\}\}', str(_number), reply)
            return reply
            
