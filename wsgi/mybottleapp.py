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
	payload={'method':'flickr.photos.search','api_key':key,'text':nombre,'format':'json'}
#EJEMPLO DE URL:
#https://api.flickr.com/services/rest/?method=flickr.photos.search&api_key=42c4c2df25b50670ab964bef4372f3bd&text=perro&format=json
	r=requests.get(url_base,params=payload)
	lista=[]
	lista1=[]
	print r.url
	if r.status_code==200:
#IMPRIMIR ID:
		doc = json.loads(r.text[14:-1])
				
		for x in doc["photos"]["photo"]:
			lista.append(x["id"])
#EJEMPLO URL:
#https://api.flickr.com/services/rest/?method=flickr.photos.getInfo&api_key=3e43ddf68638ce426d5e4aae08250ea4&photo_id=26692818150&format=json
		payload1={'method':'flickr.photos.getInfo','api_key':key,'photo_id':lista,'format':'json'}
		r1=requests.get(url_base,params=payload1)
		if r1.status_code==200:
			doc1 = json.loads(r1.text[14:-1])
			for i in doc1["photo"]["urls"]["url"]:
				lista1.append(i["_content"])

		return template("busqueda.tpl",info=lista1)

#		doc = etree.fromstring(r.text.encode ('utf-8'))
#		busq=doc.find("photo").attrib["id"]
#		return template("busqueda.tpl",id=busq.text)

#		return template("busqueda.tpl",info=r.text)

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