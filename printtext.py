from datetime import datetime
import time
class PrintText():

    def __init__(self):
        self.text = ""
        self.name = ""
        self.description = ""

    def run(self):
        print "Running task : " + self.name + "%s" % datetime.now()
        print "Description: " + self.description
        print "text: " + self.text
        time.sleep(5)