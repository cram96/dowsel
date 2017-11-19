import tkinter as tk
import online

class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("Beermanity")

        self.label = tk.Label(master, text=online.mostrarTitulo())
        self.label.pack()
        self.label = tk.Label(master, text=online.mostrarPrueba())
        self.label.pack()

        self.greet_button = tk.Button(master, text="Siguente", command=lambda: online.siguiente())
        self.greet_button.pack()

        self.close_button = tk.Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def greet(self):
        print("Greetings!")

root =tk.Tk()
my_gui = MyFirstGUI(root)
root.mainloop()