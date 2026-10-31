import contexts.dataContext as dataContext

tasks = dataContext.load_tasks()

def create_task(task):
    tasks.append(task)
    dataContext.save_tasks(tasks)
    print("Task created successfully!")

#def read_task(tasks, index):

def readAll_tasks():
  return tasks

#def update_task

def delete_task(task_index):
  while True:
    try:
      if 1 <= task_index <= len(tasks):
        deleted_task = tasks.pop(task_index - 1)
        print(f"Task '{deleted_task}' deleted successfully!")
        dataContext.save_tasks(tasks)
        break
      else:
        print("Invalid task index.")
    except ValueError:
      print("Invalid input. Please enter a valid task index.")