#!/usr/bin/python3

import configparser
from pathlib import Path

from flask import Flask
from flask import request

########## CONST ##########
APP_CONF_HOST = 'HOST'
APP_CONF_PORT = 'PORT'
APP_CONF_SECTION = 'app_flask'
CONF_FILE = 'app.ini'

FLASK_DEFAULT_HOST = 'localhost'
FLASK_DEFAULT_PORT = 5000

JSON_METHOD = 'method'
JSON_PATH = 'path'


########## CONFIG ##########
def checkConfig(config):
	confFile = Path(CONF_FILE)
	if confFile.is_file():
		config.read(CONF_FILE)
		return True
	return False

def getConfParamFromSection(config, conf_section, conf_param):
	conf_sections = config.sections()
	if conf_section in conf_sections and conf_param in config[conf_section]:
		return config[conf_section][conf_param]
	return False

##### APP CONFIG
config = configparser.ConfigParser()
app_host = FLASK_DEFAULT_HOST
app_port = FLASK_DEFAULT_PORT
if checkConfig(config):
	app_host = getConfParamFromSection(config, APP_CONF_SECTION, APP_CONF_HOST) if getConfParamFromSection(config, APP_CONF_SECTION, APP_CONF_HOST) else FLASK_DEFAULT_HOST
	app_port = int(getConfParamFromSection(config, APP_CONF_SECTION, APP_CONF_PORT)) if getConfParamFromSection(config, APP_CONF_SECTION, APP_CONF_PORT) else FLASK_DEFAULT_PORT



########## FFMPEG ##########
def checkJSON(json):
	if (json and json != ''):
		content = request.get_json()
		if (content[JSON_METHOD] and content[JSON_PATH]):
			method = content[JSON_METHOD]
			path = content[JSON_PATH]
			return 'Succès : La méthode "%s" a été appliquée au fichier "%s".\n' % (method, path)
		return 'Erreur : Les champs "%s" et "%s" sont attendus dans le JSON !\n' % (JSON_METHOD, JSON_PATH)
	return 'Erreur : Un JSON est attendu...\n'



########## FLASK APP ##########
app = Flask(__name__)

@app.route('/')
def indexAction():
	return 'Bienvenue sur Valparaiso - FFMPEG Web Service\n'

@app.route('/ffmpeg', methods=['POST'])
def ffmpegAction():
	return checkJSON(request.get_json())		

if __name__ == '__main__':
	app.run(debug=True, host=app_host, port=app_port)
