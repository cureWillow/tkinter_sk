import tkinter as tk
import tkinterdnd2 as tkdnd
from app.controllers.main_controller import MainController

if __name__ == "__main__":
    root = tkdnd.TkinterDnD.Tk()
    app = MainController(root)
    root.mainloop()
