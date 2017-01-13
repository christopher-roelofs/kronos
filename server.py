from bottle import route, run, template, get, debug, static_file
from mako.template import Template
from mako.lookup import TemplateLookup

mylookup = TemplateLookup(directories=['./views'], output_encoding='utf-8',)

def serve_template(templatename, **kwargs):
  mytemplate = mylookup.get_template(templatename)
  return mytemplate.render(**kwargs)

@route('/static/:path#.+#', name='static')
def static(path):
  return static_file(path, root='./static')

@get('/')
def index():
  return serve_template('index.html')

debug(True)
run(host='localhost', port=8080)
