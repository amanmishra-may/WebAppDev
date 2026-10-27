import tkinter as tk


root = tk.Tk()
root.geometry("300x200")
root.title("My first App")

label = tk.Label(root, text="hello")
label.pack(pady=(0,20))

button = tk.Button(root, text="click me")
button.pack(pady=(0,20))

entry = tk.Entry(root)
entry.pack(pady=(0,20))



text = tk.Text(root, height=5, width=30)
text.pack(pady=(0,20))


check = tk.Checkbutton(root, text="Python")
check.pack(pady=(0,20))

listbox = tk.Listbox(root)
listbox.pack(pady=(0,20))
listbox.insert(1, "Python")
listbox.insert(2, "Java")
listbox.insert(3, "Git")

root.mainloop()