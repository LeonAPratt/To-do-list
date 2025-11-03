def add_task(tasks):
    name = input("task name: ").strip()
    desc = input("task description: ").strip()
    prio = input("Priority (low or med or high): ").strip().lower()

    if prio not in ("low", "med", "high"):
        prio = "low"  # default to low if invalid input

    tasks.append({
        "name":name,
        "description": desc,
        "priority": prio,
        "done": False
    })
    print("Task added.")

