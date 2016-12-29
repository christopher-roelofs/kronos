from apscheduler.schedulers.background import BackgroundScheduler



def getScheduler():
    scheduler = BackgroundScheduler()
    return scheduler