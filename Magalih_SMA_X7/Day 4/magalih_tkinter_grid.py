import tkinter as tk
root = tk.Tk()
Label1 = tk.Label(root, text="Label 1")
Label2 = tk.Label(root, text="Label 2")
Label3 = tk.Label(root, text="Label 3")

Label1.grid(row=0, column=0)
Label2.grid(row=0, column=1)
Label3.grid(row=1, column=0, columnspan=2)
root.mainloop()