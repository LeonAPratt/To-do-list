import json
def exportTasks(tasks, filename):
    fileObject = {}
    for task in tasks:
        name = task["name"]
        del task["name"]
        fileObject[name] = task


    jsonstring = json.dumps(fileObject)
    with open(filename, "w") as f:
        f.write(jsonstring)
