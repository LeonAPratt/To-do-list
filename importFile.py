import json

def importTaskFile(filename):
    file = ""
    try: # ensure that file exists
        with open(filename, "r") as f:
            file = f.read()
    except:
        return "File does not exist"
    jsondata = json.loads(file) # load the json content into a python object
    tasknames = list(jsondata.keys()) # get the list of task names
    
    tasks = []
    for name in tasknames: # iterate over the task names
        taskdata = jsondata[name] # restructure python object to make name an attribute of the dictionary
        taskdata["name"] = name
        tasks.append(taskdata)

    return tasks