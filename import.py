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
        taskdata["name"] = name
        tasks.append(taskdata)

    return tasks