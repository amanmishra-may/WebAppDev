import tkinter as tk

def say_hello():
    name = entry.get()
    label.config(text="Welcome to Fiction Library," + name)

root = tk.Tk()
root.geometry("300x200")
root.title("My first App")

label = tk.Label(root, text="Hello")
label.pack()

label = tk.Label(root,text="Enter your name : ")
label.pack(pady=(0,20))

entry = tk.Entry(root)
entry.pack(pady=(0, 20))

button = tk.Button(root, text="click me", command=say_hello)
button.pack(pady=(0, 20))

root.mainloop()
