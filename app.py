from bottle import route, run, error, static_file, template
import json
import os

f=open('bekkur.json','r')

with open ('bekkur.json','r', encoding='utf-8') as f:
    bekkur = json.load(f)

@route('/')
def index():
    return template('index', bekkur=bekkur)

@route('/nemandi/<kt>')
def kt(kt):
    return template('nemandi', kt=kt, bekkur=bekkur)

@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='./static_files')

@error(404)
def error404(error):
    return '<h1>Síðan er ekki til.</h1>'

@error(500)
def error500(error):
    return '<h1>Síðan er ekki til.</h1>'

run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
