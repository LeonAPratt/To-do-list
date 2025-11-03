import json
def exportTasks(tasks, filename):
    fileObject = {}
    for task in tasks:
        name = task["Name"]
        del task["Name"]
        fileObject[name] = task


    jsonstring = json.dumps(fileObject)
    with open(filename, "w") as f:
        f.write(jsonstring)
