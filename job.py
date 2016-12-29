import untangle
import uuid
import os
import task_types



class Job():
    def __init__(self):
        self.xml = ''
        self.uuid = uuid.uuid4()
        self.tasks = []
        self.name = ""
        self.description = ""
        self.group = "default"

    def setXML(self,xml):
        if isinstance(xml,basestring):
            self.xml = xml
        if os.path.isfile(xml):
            try:
                with open(xml,'r') as file:
                    self.xml = file.read()
            except Exception as e:
                print repr(e)

    def populateTasks(self):
        xml = untangle.parse(self.xml)
        for task in xml.job.task:
            self.tasks.append(task_types.getTask(task))




    def run(self):
        for task in self.tasks:
            task.run()
