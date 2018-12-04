import json
import os

class config:

  def GetConfig(self):
    filename = os.path.dirname(__file__) + '/config/config.json'
    with open(filename) as f:
      data = json.load(f)
    return data