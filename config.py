import json

class config:

  def GetConfig(self):
    with open('config.json') as f:
      data = json.load(f)
    return data