# kronos
Task scheduler

Jobs are a collection of tasks to be executed serially. each job is defined in xml format.

<?xml version="1.0" encoding="UTF-8"?>
<job>
<task>
<name></name>
<description></description>
<tasktype>
<param><\/param>
<tasktype>
<\/task
<\/job>

new task types can be added and go in task_types. Each task section of a job is parsed and a task object is created for each.
