from bottle import route, default_app, get, post, run, template, error, request, static_file, response
import requests
import json
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
	nombre=str(request.forms.get('foto'))
	payload={'method':'flickr.photos.search','api_key':key,'text':nombre,'format':'json'}
#EJEMPLO DE URL:
#https://api.flickr.com/services/rest/?method=flickr.photos.search&api_key=42c4c2df25b50670ab964bef4372f3bd&text=perro&format=json
	r=requests.get(url_base,params=payload)
	if r.status_code==200:
#PRUEBAS PARA DEVOLVER ID
#		doc = etree.fromstring(r.text.encode ('utf-8'))
#		busq=doc.find("photo").attrib["id"]
#		return template("busqueda",id=busq)
		return template("busqueda.tpl",info=r.text)

#ruta detalle camara

#ruta lugar geografico

@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root=os.environ['OPENSHIFT_REPO_DIR']+"static")

# This must be added in order to do correct path lookups for the views
import os
from bottle import TEMPLATE_PATH
TEMPLATE_PATH.append(os.path.join(os.environ['OPENSHIFT_REPO_DIR'], 'wsgi/views/')) 

application=default_app()