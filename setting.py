from tkinter import Tk, Label

window= Tk()
window.title("Drea and Kit's Game")
window.geometry("700x400")

window.configure(bg="pink")
label= Label(window, text="Hello", font=("Arial Black",78,"bold") bg= ("pink"), fg= ("white"))
label.pack (pady=100)

window.mainloop()