 

def add_task(tasks):
     
    desc = input("task description: ").strip()
    prio = input("Priority (low or med or high): ").strip().lower()

    if prio not in ("low", "med", "high"):
        prio = "low"  # default to low if invalid input

    tasks.append({
        "description": desc,
        "priority": prio,
        "done": False
    })
    print("Task added.")
