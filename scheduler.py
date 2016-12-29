from datetime import datetime
import time
import os

from apscheduler.schedulers.background import BackgroundScheduler



def getScheduler():
    scheduler = BackgroundScheduler()
    return scheduler