import tkinter as tk
from gui.add_task_window import AddTaskWindow
import contexts.taskContext as tasksContext
#from gui.task_list_window import TaskListWindow


COLORS = {
    "background": "#EAF3FF",
    "primary": "#2563EB",
    "secondary": "#60A5FA",
    "card": "#FFFFFF",
    "text": "#1E293B"
}


class TaskManagerApp:

    def __init__(self):

        #region Window setup
        self.window = tk.Tk()
        self.window.title("Tasky")
        self.window.geometry("800x600")
        self.window.configure(
            bg=COLORS["background"]
        )
        # endregion


        # Header
        self.header_frame = tk.Frame(
            self.window,
            bg=COLORS["background"]
        )

        self.header_frame.pack(
            pady=30
        )


        self.title_label = tk.Label(
            self.header_frame,
            text="Tasky",
            font=("Arial", 36, "bold"),
            bg=COLORS["background"],
            fg=COLORS["primary"]
        )

        self.title_label.pack()


        self.subtitle_label = tk.Label(
            self.header_frame,
            text="Manage your daily tasks",
            font=("Arial", 12),
            bg=COLORS["background"],
            fg=COLORS["text"]
        )

        self.subtitle_label.pack()


        # Add button
        self.add_button = tk.Button(
            self.window,
            text="+  Add Task",
            font=("Arial", 14, "bold"),
            bg=COLORS["primary"],
            fg="white",
            activebackground=COLORS["secondary"],
            activeforeground="white",
            width=15,
            height=2,
            relief="flat",
            command=self.open_add_task_window
        )

        self.add_button.pack(
            pady=15
        )


        # Task area
        self.tasks_container = tk.Frame(
          self.window,
          bg=COLORS["background"]
        )

        self.tasks_container.pack(
            fill="both",
            expand=True,
            padx=50,
            pady=20
        )


        self.canvas = tk.Canvas(
            self.tasks_container,
            bg=COLORS["background"],
            highlightthickness=0
        )

        self.scrollbar = tk.Scrollbar(
            self.tasks_container,
            orient="vertical",
            command=self.canvas.yview
        )


        self.tasks_frame = tk.Frame(
            self.canvas,
            bg=COLORS["background"]
        )


        # Update scroll area when tasks change
        self.tasks_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )


        self.canvas.create_window(
            (0, 0),
            window=self.tasks_frame,
            anchor="nw"
        )


        self.canvas.configure(
            yscrollcommand=self.scrollbar.set
        )


        self.canvas.pack(
            side="left",
            fill="both",
            expand=True
        )


        self.scrollbar.pack(
            side="right",
            fill="y"
        )

        self.canvas.bind_all(
          "<MouseWheel>",
          self.scroll
        )


    def open_add_task_window(self):

        AddTaskWindow(
            self.window,
            self.display_tasks
        )

    def scroll(self, event):

      self.canvas.yview_scroll(
        int(-1 * (event.delta / 120)),
        "units"
      )


    def display_tasks(self):

        for widget in self.tasks_frame.winfo_children():
            widget.destroy()


        tasks = tasksContext.readAll_tasks()


        if not tasks:

            empty_label = tk.Label(
                self.tasks_frame,
                text="No tasks yet",
                font=("Arial", 16),
                bg=COLORS["background"],
                fg=COLORS["text"]
            )

            empty_label.pack(
                pady=50
            )

            return


        for index, task in enumerate(tasks, start=1):

            card = tk.Frame(
                self.tasks_frame,
                bg=COLORS["card"],
                bd=0,
                padx=20,
                pady=15
            )

            card.pack(
                fill="x",
                pady=8
            )


            number_label = tk.Label(
                card,
                text=f"{index}.",
                font=("Arial", 14, "bold"),
                bg=COLORS["card"],
                fg=COLORS["primary"]
            )

            number_label.pack(
                side="left",
                padx=10
            )


            task_label = tk.Label(
                card,
                text=task,
                font=("Arial", 14),
                bg=COLORS["card"],
                fg=COLORS["text"],
                anchor="w"
            )

            task_label.pack(
                side="left",
                fill="x",
                expand=True
            )


    def run(self):

        self.window.mainloop()