import tkinter
from tkinter import messagebox
from model.comprobadorCadenas import Regex
from view.newRegex import Popup
from view.stringVerificator import Verification
from view.showRegex import Show

def showRegex():
    #messagebox.showinfo(message=regex.get_regex(), title="Expresión regular actual")
    popup = Show(main_window, regex)    
    popup.mainloop()
def showPopup():
    popup = Popup(main_window, regex)
    popup.mainloop()
def showVerif():
    popup = Verification(main_window, text_entry_area.get(), regex)
    popup.mainloop()
#Creates the window where all the widgets will be displayed.
main_window = tkinter.Tk()
main_window.title("Verificador de cadenas")
main_window.geometry("700x400")
main_window.resizable(False,False)

regex = Regex()

menu_bar = tkinter.Menu(main_window)
menu_bar.add_command(label="Mostrar ReGex", command=showRegex)
menu_bar.add_command(label="Reasignar ReGex", command= showPopup)

#creation of an object with different color for the background and foreground
display_label = tkinter.Label(main_window, text="Ingresa la cadena a verificar",bg="black",fg="white")

text_entry_area = tkinter.Entry(main_window)

submit_button = tkinter.Button(main_window,text="Verificar", command=showVerif)

display_label.pack(fill="x")
#Sets the entry area to fill the full width of the window where's been displayed
text_entry_area.pack(fill=tkinter.X)
submit_button.pack()


main_window.config(menu=menu_bar)
main_window.mainloop()
