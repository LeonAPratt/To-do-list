

from view_tasks import view_tasks

def mark_complete(tasks):
    if len(tasks) == 0:
        print("no tasks to complete")
        return
    

    view_tasks(tasks)
    num = input("which number? ")

    try:
        n = int(num)
    except:
        print("not a number")
        return

    if n < 0 or n >= len(tasks):
        print("that one doesnt exist")
        return
    

    tasks[n]["done"] = True
    print("marked done")
