#!/usr/bin/python3

from flask import Flask
from flask import request

########## CONST ##########
APP_CONF = 'app_flask'
APP_CONF_HOST = 'HOST'
APP_CONF_PORT = 'PORT'

JSON_METHOD = 'method'
JSON_PATH = 'path'


########## CONFIG ##########



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
	app.run(debug=True)
