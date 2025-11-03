import json

def importTaskFile(filename):
    file = ""
    with open(filename, "r") as f:
        file = f.read()

    tasks = json.loads(file)
    return tasks


def exportTasks(tasks, filename):
    jsonstring = json.dumps(tasks)
    with open(filename, "w") as f:
        f.write(jsonstring)




