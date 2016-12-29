import untangle
import uuid
import os
import task_types
import instance



class Job():
    def __init__(self):
        self.xml = ''
        self.uuid = uuid.uuid4()
        self.tasks = []
        self.name = ""
        self.description = ""
        self.group = "default"
        self.instances = []

    def setXML(self,xml):
        if isinstance(xml,basestring):
            self.xml = xml
        if os.path.isfile(xml):
            try:
                with open(xml,'r') as file:
                    self.xml = file.read()
            except Exception as e:
                print repr(e)
        xmlobj = untangle.parse(self.xml)
        for task in xmlobj.job.task:
            self.tasks.append(task_types.getTask(task))

    def updateTasks(self):
        xml = untangle.parse(self.xml)
        for task in xml.job.task:
            self.tasks.append(task_types.getTask(task))




    def run(self):
        jobInstance = instance.Instance()
        jobInstance.id = instance.getInstanceId()
        for task in self.tasks:
            task.run()
        jobInstance.status = "good"
        jobInstance.jobName = self.name
        self.instances.append(jobInstance)

