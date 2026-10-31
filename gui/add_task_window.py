import tkinter as tk
import contexts.taskContext as tasksContext


COLORS = {
    "background": "#EAF3FF",
    "primary": "#2563EB",
    "secondary": "#60A5FA",
    "card": "#FFFFFF",
    "text": "#1E293B"
}


class AddTaskWindow:

    def __init__(self, parent, refresh_callback):

        self.window = tk.Toplevel(parent)

        self.refresh_callback = refresh_callback

        self.window.title("Add Task")
        self.window.geometry("450x300")
        self.window.resizable(False, False)

        self.window.configure(
            bg=COLORS["background"]
        )

        # Keep window above parent
        self.window.transient(parent)
        self.window.grab_set()

        self.create_widgets()


    def create_widgets(self):

        # Header
        self.title_label = tk.Label(
            self.window,
            text="Create New Task",
            font=("Arial", 24, "bold"),
            bg=COLORS["background"],
            fg=COLORS["primary"]
        )

        self.title_label.pack(
            pady=(30, 5)
        )


        self.subtitle_label = tk.Label(
            self.window,
            text="What do you need to do?",
            font=("Arial", 12),
            bg=COLORS["background"],
            fg=COLORS["text"]
        )

        self.subtitle_label.pack(
            pady=(0, 20)
        )


        # Entry container
        self.entry_frame = tk.Frame(
            self.window,
            bg=COLORS["background"]
        )

        self.entry_frame.pack()


        self.task_entry = tk.Entry(
            self.entry_frame,
            font=("Arial", 14),
            width=35,
            bg=COLORS["card"],
            fg=COLORS["text"],
            relief="solid",
            bd=1
        )

        self.task_entry.pack(
            ipady=7
        )

        self.task_entry.focus()


        # Button
        self.save_button = tk.Button(
            self.window,
            text="+  Add Task",
            font=("Arial", 13, "bold"),
            width=15,
            height=2,
            bg=COLORS["primary"],
            fg="white",
            activebackground=COLORS["secondary"],
            activeforeground="white",
            relief="flat",
            command=self.save_task
        )

        self.save_button.pack(
            pady=30
        )


        # Enter key
        self.window.bind(
            "<Return>",
            lambda event: self.save_task()
        )


    def save_task(self):

        task = self.task_entry.get().strip()

        if task:

            tasksContext.create_task(task)

            self.refresh_callback()

            self.window.destroy()