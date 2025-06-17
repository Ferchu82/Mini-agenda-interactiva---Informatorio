import tkinter as tk
import time

ventana = tk.Tk()
ventana.title("Mini Agenda Interactiva")
ventana.geometry("450x350")
ventana.configure(bg="#f0f0f0")

barra_menu = tk.Menu(ventana)
ventana.config(menu=barra_menu)

menu_principal = tk.Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label="Opciones", menu=menu_principal)

submenu = tk.Menu(menu_principal, tearoff=0)
menu_principal.add_cascade(label="Tareas", menu=submenu)
submenu.add_command(label="Agregar nueva")
submenu.add_command(label="Eliminar tarea")



ventana.mainloop()