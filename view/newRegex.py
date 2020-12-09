import tkinter as tk
from tkinter import ttk
from model.comprobadorCadenas import Regex
def update_regex(new_regex, regex):
    print("method called")
    regex.set_regex(new_regex)
class Popup(ttk.Frame, Regex):
    #Master is the main window
    def __init__(self, master, regex):
        ttk.Frame.__init__(self, master)
        application_window = tk.Toplevel()
        application_window.wm_title("Nueva ReGex")

        display_label = tk.Label(application_window, text="Nuevo ReGex")
        display_label.pack()
        
        entry_text = tk.Entry(application_window)
        entry_text.pack()
        
        submit_button = tk.Button(application_window, text="Ingresar", command=lambda: update_regex(entry_text.get(), regex) )
        #submit_button = tk.Button(application_window, text="Ingresar", command= lambda: regex.set_regex(entry_text.get()) )
        submit_button.pack()
        
