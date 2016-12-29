import printtext

def getTask(task):
    if task.printtext:
        printtextTask = printtext.PrintText()
        printtextTask.name = task.name.cdata
        printtextTask.description = task.description.cdata
        printtextTask.text = task.printtext.text.cdata
        return printtextTask
