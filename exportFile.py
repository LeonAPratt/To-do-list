import json
def exportTasks(tasks, filename):
    fileObject = {}
    for task in tasks: # iterate over the tasks
        name = task["name"] # get the name of the task
        del task["name"] # restructure the dictionary such that the dictionary is a value associated with the task name
        fileObject[name] = task


    jsonstring = json.dumps(fileObject) # write the dictionary to a json file
    with open(filename, "w") as f:
        f.write(jsonstring)
