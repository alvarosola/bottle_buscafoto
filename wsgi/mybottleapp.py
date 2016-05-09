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
	return template('index.tpl')

'''
#ruta busqueda
@route('/busqueda')
def busqueda():
	payload={method="flickr.photos.search",api_key=key,text="arbol",format="json"}
	r=requests.get(url_base,params=payload)
	if r.status_code==200:
		return template("busqueda.tpl",info=r.text)'''

#ruta detalle camara

#ruta lugar geografico

'''
@route('/name/<name>')
def nameindex(name='Stranger'):
    return '<strong>Hello, %s!</strong>' % name
 
@route('/')
def index():
    return '<strong>Hello World!</strong>'

@route('/hello/')
@route('/hello/<name>')
def hello(name='Mundo'):
    return template('template_hello.tpl', nombre=name)'''

@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root=os.environ['OPENSHIFT_REPO_DIR']+"static")

# This must be added in order to do correct path lookups for the views
import os
from bottle import TEMPLATE_PATH
TEMPLATE_PATH.append(os.path.join(os.environ['OPENSHIFT_REPO_DIR'], 'wsgi/views/')) 

application=default_app()
