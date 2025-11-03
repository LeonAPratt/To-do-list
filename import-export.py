import json

def importTaskFile(filename):
    file = ""
    with open(filename, "r") as f:
        file = f.read()

    jsondata = json.loads(file)
    tasknames = list(jsondata.keys())
    
    tasks = []
    for name in tasknames:
        taskdata = jsondata[name]
        taskdata["Name"] = name
        tasks.append(taskdata)

    return tasks

def exportTasks(tasks, filename):
    fileObject = {}
    for task in tasks:
        name = task["Name"]
        del task["Name"]
        fileObject[name] = task


    jsonstring = json.dumps(fileObject)
    with open(filename, "w") as f:
        f.write(jsonstring)


