instance = 0

def getInstanceId():
    global instance
    instance += 1
    return instance

class Instance():
    def __init__(self):
        self.id = 0
        self.status = ""
        self.log = []
        self.jobName = ""




