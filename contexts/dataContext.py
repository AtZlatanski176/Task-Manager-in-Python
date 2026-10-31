def save_tasks(tasks):
  with open("tasks.txt", "w", encoding="utf-8") as file:
    for task in tasks:
      file.write(task + "\n")


def load_tasks():
  try:
    with open("tasks.txt", "r", encoding="utf-8") as file:
      tasks = [line.strip() for line in file if line.strip()]
    return tasks
  except FileNotFoundError:
    save_tasks([])
    return []