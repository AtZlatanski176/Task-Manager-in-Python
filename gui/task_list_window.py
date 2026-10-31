'''import tkinter as tk
import contexts.taskContext as tasksContext


class TaskListWindow:

    def __init__(self, parent):

        self.window = tk.Toplevel(parent)

        self.window.title("Your Tasks")
        self.window.geometry("500x500")

        self.tasks_frame = tk.Frame(self.window)
        self.tasks_frame.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

        self.display_tasks()


    def display_tasks(self):

        tasks = tasksContext.readAll_tasks()

        for task in tasks:

            card = tk.Frame(
                self.tasks_frame,
                bd=2,
                relief="solid",
                padx=20,
                pady=10
            )

            card.pack(
                fill="x",
                pady=10
            )


            label = tk.Label(
                card,
                text=task,
                font=("Arial", 14)
            )

            label.pack()'''