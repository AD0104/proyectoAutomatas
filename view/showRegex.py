import tkinter as tk
from tkinter import ttk
from model.comprobadorCadenas import Regex
class Show(ttk.Frame, Regex):
    def __init__(self, master,regex):
        ttk.Frame.__init__(self, master)
        application_window = tk.Toplevel()
        application_window.wm_title("ReGex actual")
        application_window.geometry("200x75")
        application_window.resizable(False, False)
        color="#ff6542"
        application_window.configure(bg=color)

        display_label = tk.Label(application_window, text=regex.get_regex(), font="Arial 14", fg="#1a5b5c", bg=color)
        
        accept_button = tk.Button(application_window, text="Aceptar", command= lambda: application_window.destroy() )

        display_label.pack(fill="both")
        accept_button.pack()
