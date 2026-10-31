#main program
#import contexts.dataContext as dataContext
#import contexts.taskContext as taskContext
from gui.app import TaskManagerApp


app = TaskManagerApp()

app.run()

#tasks = dataContext.load_tasks()
#while True:
  #print ("Task Manager")
  #print ("1. Create new task")
  #print ("2. View tasks")
  #print ("3. Delete task")
  #print ("4. Exit")
  #input_choice = input("Enter your choice (1-4): ")
  #if input_choice == "1":
    #taskContext.create_task(tasks)
    #input("Press Enter to continue...")
  #elif input_choice == "2":
    #taskContext.readAll_tasks(tasks)
    #input("Press Enter to continue...")
  #elif input_choice == "3":
    #if not tasks:
      #print("No tasks available to delete.")
      #input("Press Enter to continue...")
    #else:
      #taskContext.delete_task(tasks)
      #input("Press Enter to continue...")
  #elif input_choice == "4":
    #print("Exiting the program. Goodbye!")
    #break
  #else:
    #print("Invalid choice. Please try again.")
    #input("Press Enter to continue...")