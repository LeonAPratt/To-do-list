import os
import importFile
import exportFile
import add_task
import view_tasks
import mark_complete

def menu(taskfile,tasks):
    tasks = importFile.importTaskFile(taskfile)
    option = int(input("Menu:\n(1) Add a task\n(2) Mark tast as completed\n(3) view tasks\n"))
    match option:
        case 1:
            print(tasks)
            add_task.add_task(tasks)
            print(tasks)
            exportFile.exportTasks(tasks, taskfile)
            os.system('cls' if os.name=='nt' else 'clear')
            menu(taskfile, tasks)
        case 2:
            mark_complete.mark_complete(tasks)
            exportFile.exportTasks(tasks, taskfile)
            os.system('cls' if os.name=='nt' else 'clear')
            menu(taskfile, tasks)
        case 3:
            view_tasks.view_tasks(tasks)
            menu(taskfile,tasks)
        case _:
            os.system('cls' if os.name=='nt' else 'clear')
            menu(taskfile, tasks)
    
def loadTaskFile():
    # input cleaning
    taskfile = str(input("Enter the name of your task list file: ")).replace("/","").replace("\\","").split(".")[0] + ".json" 
    if os.path.isfile(taskfile) == False:
        f = open(taskfile, "x")
        f.write("{}")
        f.close()
        return taskfile, []
    # import the task file contents
    tasks = importFile.importTaskFile(taskfile)
    return taskfile, tasks
if __name__ == "__main__":

    taskfile, tasks = loadTaskFile()
    menu(taskfile, tasks) # begin main loop