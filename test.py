"""
Demonstrates how to use the background scheduler to schedule a job that executes on 3 second
intervals.
"""

from datetime import datetime
import time
import os
import job
import logging
from apscheduler.schedulers.background import BackgroundScheduler

logging.basicConfig()

jobs = {}

job_defaults = {
    'coalesce': False,
    'max_instances': 2
}


def tick():
    print('Tick! The time is: %s' % datetime.now())

def runJob(id):
    job = jobs[id]
    job.run()


if __name__ == '__main__':
    scheduler = BackgroundScheduler()
    scheduler.configure(job_defaults=job_defaults)
    job1 = job.Job()
    job1.setXML("testjob.xml")
    jobs[job1.uuid] = job1
    job2 = job.Job()
    job2.setXML("testjob2.xml")
    jobs[job2.uuid] = job2
    scheduler.add_job(runJob, 'interval',[job1.uuid], seconds=3)
    #scheduler.add_job(runJob, 'interval', [job2.uuid], seconds=10)
    scheduler.start()
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

    try:
        # This is here to simulate application activity (which keeps the main thread alive).
        while True:
            time.sleep(1)
    except (KeyboardInterrupt, SystemExit):
        # Not strictly necessary if daemonic mode is enabled but should be done if possible
        scheduler.shutdown()