def save_tasks(tasks):
  with open("tasks.txt", "w") as file:
    for task in tasks:
      file.write(task + "\n")
      
def load_tasks():
  with open("tasks.txt", "r") as file:
    tasks = [line.strip() for line in file]
  return tasks