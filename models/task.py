class Task:
  def __init__(self, title, description, due_date):
    self.title = title
    self.description = description
    self.due_date = due_date
    self.completed = False

  def complete_task(self):
    self.completed = True

  def __str__(self):
    status = "Done" if self.completed else "Pending"
    return (
      f"Title: {self.title}\n"
      f"Description: {self.description}\n"
      f"Due Date: {self.due_date}\n"
      f"Completed: {status}"
    )