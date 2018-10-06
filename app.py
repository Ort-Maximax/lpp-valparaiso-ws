#!/usr/bin/python3

import configparser
from pathlib import Path

from flask import Flask
from flask import request

import ffmpeg

########## CONST ##########
APP_CONF_HOST = 'HOST'
APP_CONF_PORT = 'PORT'
APP_CONF_SECTION = 'app_flask'
CONF_FILE = 'app.ini'

FFMPEG_METHOD_CONVERT_MP4_H264 = 'convert_mp4_h264'
FFMPEG_METHOD_HFLIP = 'hflip'
FFMPEG_METHOD_VFLIP = 'vflip'

FLASK_DEFAULT_HOST = 'localhost'
FLASK_DEFAULT_PORT = 5000

JSON_METHOD = 'method'
JSON_INPUT = 'input'
JSON_OUTPUT = 'output'


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
def consumeJSON(json):
	if (json and json != ''):
		content = request.get_json()
		if (content[JSON_METHOD] and content[JSON_INPUT]):
			method = content[JSON_METHOD]
			path = content[JSON_INPUT]
			output = content[JSON_OUTPUT] if content[JSON_OUTPUT] else path
			file = Path(path)
			if not file.is_file():
				return 'Erreur : Le fichier spécifié "%s" n\'existe pas !\n' % path
			err = executeFfmpegMethod(method, path, output)
			if err and err != '':
				return 'Erreur : %s\n' % err

			return 'Succès : La méthode "%s" a été appliquée au fichier "%s".\n' % (method, path)

		return 'Erreur : Les champs "%s" et "%s" sont attendus dans le JSON !\n' % (JSON_METHOD, JSON_INPUT)

	return 'Erreur : Un JSON est attendu...\n'

def executeFfmpegMethod(method, inputFile, outputPath):
	err = ''
	if method == FFMPEG_METHOD_CONVERT_MP4_H264:
		out, err = (
			ffmpeg
			.input(inputFile)
			.output(outputPath, vcodec='libx264', format='mp4', pix_fmt='yuv420p10')
			.run(overwrite_output=True)
		)
	if method == FFMPEG_METHOD_VFLIP:
		out, err = (
			ffmpeg
			.input(inputFile)
			.vflip()
			.output(outputPath)
			.run(overwrite_output=True)
		)
	if method == FFMPEG_METHOD_HFLIP:
		out, err = (
			ffmpeg
			.input(inputFile)
			.hflip()
			.output(outputPath)
			.run(overwrite_output=True)
		)
	return err


########## FLASK APP ##########
app = Flask(__name__)

@app.route('/')
def indexAction():
	return 'Bienvenue sur Valparaiso - FFMPEG Web Service\n'

@app.route('/ffmpeg', methods=['POST'])
def ffmpegAction():
	return consumeJSON(request.get_json())		

if __name__ == '__main__':
	app.run(debug=True, host=app_host, port=app_port)
