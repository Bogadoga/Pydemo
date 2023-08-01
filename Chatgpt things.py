import tkinter as tk

def on_button_click():
    # Put the code you want to run here
    print("Button was clicked!")

root = tk.Tk()
root.title("Clickable Button")

button = tk.Button(root, text="Click me!", command=on_button_click)
button.pack()

root.mainloop()