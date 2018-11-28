# VoiceMoticz

Ask Domoticz a natural language about the temperature or ask him to turn on the light in the living room.

## ChangeLog
2018.11.28
+ add support "unknown ask" plase add keys 'reply_unknown' in rules.json and conf.json (see my example files)
+ add support float number recognize from phrase

## TODO
- [x] text processor
- [x] config
- [x] get data from Domoticz
- [x] set data to Domoticz
- [ ] say to Google Home
- [ ] as Flask webservice
- [ ] daemon
- [ ] get text from Google Home Assistant

## Install requirements python library
```
pip3 install pyjq
```
## Install for tests
```
git clone https://github.com/z1mEk/voicemoticz.git
sudo chmod +x voicemoticz.py
```
## Config
Open the config.json file and set your Domoticz API url. 

## Set rules
Open the rules.json and modify data for your preference and your Domoticz
Keys 'elicitation_pattern' and 'name_pattern' suported regex.
You must do it carefully, keeping the logic

## Run Test
```
./voicemoticz.py "Jaka jest temperatura u Marysi?"
```
or 
```
./voicemoticz.py "Ile stopni jest u Szymka w pokoju?"
```
or
```
./voicemoticz.py "Ciepło jest na dworze?"
```
or
```
./voicemoticz.py "Włącz kinkiety w salonie?"
```
## Example Result
```
Temperatura w pokoju Szymka wynosi 20.5℃
```
```
OK, włączam kinkiety w salonie
```
