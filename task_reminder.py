import tkinter as tk

root = tk.Tk()
root.title("Task Reminder System")
root.geometry("500x500")

title = tk.Label(root, text="Task Reminder System", font=("Arial",16))
title.pack(pady=20)

root.mainloop()
