import tkinter as tk


class TaskManagerApp:

  def __init__(self):
    self.window = tk.Tk()
    self.window.title("Task Manager")

  def run(self):
    self.window.mainloop()