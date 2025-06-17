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

def actualizar_hora():
    hora_actual = time.strftime("%H:%M:%S")
    reloj.config(text=hora_actual)
    ventana.after(1000, actualizar_hora)

reloj = tk.Label(ventana, font=("Arial", 24), fg="white", bg="black")
reloj.pack(pady=10)
actualizar_hora()

marco_lista = tk.Frame(ventana)
marco_lista.pack(padx=10, pady=10, fill='both', expand=True)

scrollbar = tk.Scrollbar(marco_lista)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

lista_tareas = tk.Listbox(marco_lista, yscrollcommand=scrollbar.set, height=10, font=('Arial', 10))
for i in range(1, 21):
    lista_tareas.insert(tk.END, f'Tarea {i}')
lista_tareas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar.config(command=lista_tareas.yview)

def guardar_tarea():
    seleccion = lista_tareas.curselection()
    if seleccion:
        tarea = lista_tareas.get(seleccion)
        print(f"Tarea guardada: {tarea}")
        tk.messagebox.showinfo("Tarea Guardada", f"Tarea guardada:\n{tarea}")
    else:
        tk.messagebox.showwarning("Sin selección", "Seleccione una tarea para guardar.")

boton_guardar = tk.Button(ventana, text="Guardar tarea", bg="#4CAF50", fg="white",
                          font=('Arial', 10, 'bold'), command=guardar_tarea)
boton_guardar.pack(pady=10)

nombre_autor = tk.Label(ventana, text="© Fernando E. Peró", font=('Arial', 8), bg='#f0f0f0', anchor='se')
nombre_autor.pack(side='right', padx=10, pady=5)

ventana.mainloop()