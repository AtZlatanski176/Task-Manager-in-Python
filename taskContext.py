import dataContext

def create_task(tasks):
  task = input("Enter the task: ")
  tasks.append(task)
  dataContext.save_tasks(tasks)
  print("Task created successfully!")

#def read_task(tasks, index):

def readAll_tasks(tasks):
  print("Tasks:")
  for index, task in enumerate(tasks):
    print(f"{index + 1}. {task}")

#def update_task

def delete_task(tasks):
  readAll_tasks(tasks)
  while True:
    try:
      task_index = int(input("Enter the index of the task to delete: "))
      if 1 <= task_index <= len(tasks):
        deleted_task = tasks.pop(task_index - 1)
        print(f"Task '{deleted_task}' deleted successfully!")
        dataContext.save_tasks(tasks)
        break
      else:
        print("Invalid task index.")
    except ValueError:
      print("Invalid input. Please enter a valid task index.")