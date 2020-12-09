import tkinter as tk
from tkinter import ttk
from model.comprobadorCadenas import Regex
class Verification(ttk.Frame, Regex):
    def __init__(self, master, text, regex):
        ttk.Frame.__init__(self, master)
        application_window = tk.Toplevel()
        application_window.wm_title("Verificación")
        application_window.geometry("200x75")
        application_window.resizable(False, False)

        display_label = None
        answ = regex.verify_text(text)
        if answ:
            color = "#71fc2b"
            application_window.configure(bg=color)
            display_label = tk.Label(application_window, text="Cadena valida", font="Arial 18", bg=color, pady=15)
        else:
            application_window.configure(bg="red")
            display_label = tk.Label(application_window, text="Cadena no valida", font="Arial 18", bg='red', pady=15)
        accept_button = tk.Button(application_window, text="Aceptar", command= lambda: application_window.destroy() )

        display_label.pack(fill="both")
        accept_button.pack()
