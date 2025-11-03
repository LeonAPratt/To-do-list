 

def view_tasks(tasks):
     
    if not tasks:
        print("o tasks yet")
        return

    print("\nCurrent Tasks:")
    for i, t in enumerate(tasks):
        name = t.get("name", "")
        desc = t.get("description", "")
        prio = t.get("priority", "low")
        done = t.get("done", False)
        status = "DONE" if done else "TODO"
        print(f"{i}. {name}  [priority: {prio}]  [{status}]")
