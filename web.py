from bottle import route, run, template,request,post, static_file
from datetime import datetime
import time
import os
import job
import logging
from apscheduler.schedulers.background import BackgroundScheduler
import instance


logging.basicConfig()
jobs = {}
job_defaults = {
    'coalesce': False,
    'max_instances': 2
}
log = []

def runJob(id):
    job = jobs[id]
    job.run()

scheduler = BackgroundScheduler()
scheduler.configure(job_defaults=job_defaults)
scheduler.start()

@route('/')
def server_static():
    return static_file("index.html", root='./')

@route('/newjob')
def index():
    return template('newjob')

@route('/instances')
def index():
    return template('instances',jobs = jobs)

@post('/createjob')
def index():
    name = request.forms.get('name')
    group = request.forms.get('group')
    description = request.forms.get('description')
    xml = request.forms.get('xml')


    newjob = job.Job()
    newjob.setXML(xml)
    newjob.name = name
    newjob.description = description
    newjob.group = group
    jobs[newjob.uuid] = newjob
    scheduler.add_job(runJob, 'interval', [newjob.uuid], seconds=3)


run(host='localhost', port=8080)