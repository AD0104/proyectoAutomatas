import tkinter
#Creates the window where all the widgets will be displayed.
main_window = tkinter.Tk()
main_window.geometry("700x400")
main_window.resizable(False,False)

#creation of an object with different color for the background and foreground
display_label = tkinter.Label(main_window, text="Ingresa la cadena a verificar",bg="black",fg="white")
text_entry_area = tkinter.Entry(main_window)
submit_button = tkinter.Button(main_window,text="Verificar")

display_label.pack(fill="x")
#Sets the entry area to fill the full width of the window where's been displayed
text_entry_area.pack(fill=tkinter.X)
submit_button.pack()

main_window.mainloop()
