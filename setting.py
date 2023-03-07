import tkinter as tk

window = tk.Tk()


window.title("Fortune Teller")

window.geometry("600x300")
window.configure(background="pink")

label = tk.Label(window, text="Hello")
label.pack(pady=20)


button = tk.Button(window, text="Click Me!")
button.pack(pady=10)

window.mainloop()
