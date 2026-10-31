#creating a task in file
def create_task(tasks):
  task = input("Enter the task: ")
  tasks.append(task)
  save_tasks(tasks)
  print("Task created successfully!")

def save_tasks(tasks):
  with open("tasks.txt", "w") as file:
    for task in tasks:
      file.write(task + "\n")

#reading tasks from file
def show_tasks(tasks):
  print("Tasks:")
  for index, task in enumerate(tasks):
    print(f"{index + 1}. {task}")

def load_tasks():
  with open("tasks.txt", "r") as file:
    tasks = [line.strip() for line in file]
  return tasks


#deleting task from file
def delete_task(tasks):
  show_tasks(tasks)
  while True:
    try:
      task_index = int(input("Enter the index of the task to delete: "))
      if 1 <= task_index <= len(tasks):
        deleted_task = tasks.pop(task_index - 1)
        print(f"Task '{deleted_task}' deleted successfully!")
        save_tasks(tasks)
        break
      else:
        print("Invalid task index.")
    except ValueError:
      print("Invalid input. Please enter a valid task index.")


#main program
tasks = load_tasks()
while True:
  print ("Task Manager")
  print ("1. Create new task")
  print ("2. View tasks")
  print ("3. Delete task")
  print ("4. Exit")
  input_choice = input("Enter your choice (1-4): ")
  if input_choice == "1":
    create_task(tasks)
    input("Press Enter to continue...")
  elif input_choice == "2":
    show_tasks(tasks)
    input("Press Enter to continue...")
  elif input_choice == "3":
    if not tasks:
      print("No tasks available to delete.")
      input("Press Enter to continue...")
    else:
      delete_task(tasks)
      input("Press Enter to continue...")
  elif input_choice == "4":
    print("Exiting the program. Goodbye!")
    break
  else:
    print("Invalid choice. Please try again.")
    input("Press Enter to continue...")