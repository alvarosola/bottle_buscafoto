from bottle import route, default_app, get, post, run, template, error, request, static_file, response
import requests
import json
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

#from requests_oauthlib import OAuth1
#from urlparse import parse_qs

key="5e540fc0e14e6863f1d69c5a15880c4a"
url_base="https://api.flickr.com/services/rest"

#ruta index
@route('/')
def index():
	return template('index')

#ruta busqueda
@route('/busqueda',method='POST')
def busqueda():
	nombre=request.forms.get('foto')
	payload={'method':'flickr.photos.search','api_key':key,'text':nombre,'extras':'url_o','format':'json'}
#EJEMPLO DE URL:
# https://api.flickr.com/services/rest/?method=flickr.photos.search&api_key=3e43ddf68638ce426d5e4aae08250ea4&text=arbol&extras=url_o&format=json
	r=requests.get(url_base,params=payload)
	lista=[]
	lista1=[]
	print r.url
	if r.status_code==200:
		doc = json.loads(r.text[14:-1])
		#print doc
#Obtener URL de fotos:
		for x in doc["photos"]["photo"]:
			if x.has_key("url_o"):
				lista.append(x['url_o'])
#Obtener IDS de fotos:
		for i in doc["photos"]["photo"]:
			if i.has_key("id"):
				lista1.append(i['id'])

		return template("busqueda.tpl",info=lista,ids=lista1)

#ruta detalle camara

@route ('/detalles/<id>')
def detalles(id):
	payload1={'method':'flickr.photos.getExif','api_key':key,'photo_id':id,'format':'json'}
#EJEMPLO URL:
#https://api.flickr.com/services/rest/?method=flickr.photos.getExif&api_key=01480c276d9e03abc8cb4e2273450144&photo_id=26952354992&format=json
	r1=requests.get(url_base,params=payload1)
	lista2=[]
	print r1.url
	if r1.status_code==200:
		doc1 = json.loads(r1.text[14:-1])
		print doc1
#Obtener detalles camara
		for prueba in doc1["photo"]:
			lista2.append(prueba['camera'])		


	return template('detalles.tpl',camara=lista2)

#ruta lugar geografico

@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root=os.environ['OPENSHIFT_REPO_DIR']+"static")

# This must be added in order to do correct path lookups for the views
import os
from bottle import TEMPLATE_PATH
TEMPLATE_PATH.append(os.path.join(os.environ['OPENSHIFT_REPO_DIR'], 'wsgi/views/')) 

application=default_app()