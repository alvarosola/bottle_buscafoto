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
	payload={'method':'flickr.photos.search','api_key':key,'text':nombre,'extras':'url_o,url_s','format':'json'}
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
				lista.append([x['url_s'],x["url_o"]])
#Obtener IDS de fotos:
		for i in doc["photos"]["photo"]:
			if i.has_key("id"):
				lista1.append(i['id'])

		print lista
		return template("busqueda.tpl",info=lista,ids=lista1)

#ruta detalle camara

@route ('/detalles/<id>')
def detalles(id):
	payload1={'method':'flickr.photos.getExif','api_key':key,'photo_id':id,'format':'json'}
#EJEMPLO URL:
#https://api.flickr.com/services/rest/?method=flickr.photos.getExif&api_key=01480c276d9e03abc8cb4e2273450144&photo_id=26952354992&format=json
	r1=requests.get(url_base,params=payload1)
	lista2=[]
	lista_info=[]
	lista_label=["Orientation","Software","Exposure","Aperture","ISO Speed","Date and Time (Original)","Flash","Saturation"]
	lista_label_esp=["Orientacion","Software","Exposure","Apertura","ISO","Fecha","Flash","Saturacion"]
	print r1.url
	if r1.status_code==200:
		doc1 = json.loads(r1.text[14:-1])

		if doc1.has_key('photo'):

		#print doc1
#Obtener detalles camara
			if doc1['photo'].has_key('camera'):
				if not len(doc1['photo']['camera']) <= 2:
					fich = doc1['photo']['camera']
				else:
					fich = 'La imagen no contiene informacion de la camara'
		
#Obtener caracteristicas de fotos
			for info in doc1['photo']['exif']:
				if info['label'] in lista_label:
					lista_info.append(info['raw']['_content'])

		else:
			fich = 'No hay informacion'

	return template('detalles.tpl',camara=fich,labels=lista_label_esp,info=lista_info)

#ruta lugar geografico
#@route("/mapa/<id>")
#def mapa(id):
#	return template("mapa.tpl",ubicaciones=[[41.700730,2.858247]])


@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root=os.environ['OPENSHIFT_REPO_DIR']+"static")

# This must be added in order to do correct path lookups for the views
import os
from bottle import TEMPLATE_PATH
TEMPLATE_PATH.append(os.path.join(os.environ['OPENSHIFT_REPO_DIR'], 'wsgi/views/')) 

application=default_app()