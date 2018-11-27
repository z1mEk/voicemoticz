# VoiceMoticz

Ask Domoticz a natural language about the temperature or ask him to turn on the light in the living room.

- [x] text processor
- [x] config
- [x] get data from Domoticz
- [x] set data to Domoticz
- [ ] say to Google Home
- [ ] as Flask webservice
- [ ] daemon
- [ ] get text from Google Home Assistant


## Install for tests
git clone https://github.com/z1mEk/voicemoticz.git
sudo chmod +x voicemoticz.py

## Config
Open the config.json file and set your Domoticz API url. 

## Set rules
Open the rules.json and modify data for your preference and your Domoticz

## Run Test
'''
./voicemoticz.ph "Jaka jest temperatura u Marysi?"
'''
or 
'''
./voicemoticz.ph "Ile stopni jest u Szymka w pokoju?"
'''
or
'''
./voicemoticz.ph "Ciepło jest na dworze?"
'''

## 
