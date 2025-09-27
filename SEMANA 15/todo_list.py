#lista de tareas

import tkinter as tk
from tkinter import ttk, messagebox


class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas")
        self.root.geometry("400x400")

        # Lista interna para almacenar las tareas como diccionarios
        self.tareas = []

        # Frame superior: entrada y botón
        frame_top = ttk.Frame(root, padding=10)
        frame_top.pack(fill="x")

        self.entry_tarea = ttk.Entry(frame_top)
        self.entry_tarea.pack(side="left", fill="x", expand=True, padx=(0, 6))
        self.entry_tarea.focus()

        btn_add = ttk.Button(frame_top, text="Añadir Tarea", command=self.add_task)
        btn_add.pack(side="left")

        # Atajo: presionar Enter en el campo también añade la tarea
        self.entry_tarea.bind("<Return>", lambda e: self.add_task())

        # Frame central: lista de tareas
        frame_center = ttk.Frame(root, padding=10)
        frame_center.pack(fill="both", expand=True)

        self.listbox = tk.Listbox(frame_center, selectmode="single", height=12)
        self.listbox.pack(side="left", fill="both", expand=True)

        # Scrollbar
        scrollbar = ttk.Scrollbar(frame_center, orient="vertical", command=self.listbox.yview)
        self.listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        # Doble clic en tarea -> marcar como completada
        self.listbox.bind("<Double-1>", lambda e: self.toggle_task())

        # Frame inferior: botones de acción
        frame_bottom = ttk.Frame(root, padding=10)
        frame_bottom.pack(fill="x")

        btn_done = ttk.Button(frame_bottom, text="Marcar como Completada", command=self.toggle_task)
        btn_done.pack(side="left", padx=(0, 6))

        btn_delete = ttk.Button(frame_bottom, text="Eliminar Tarea", command=self.delete_task)
        btn_delete.pack(side="left")

    #  Lógica principal
    def add_task(self):
        """Añade una nueva tarea desde la entrada a la lista."""
        texto = self.entry_tarea.get().strip()
        if not texto:
            messagebox.showwarning("Aviso", "Escribe una tarea antes de añadir.")
            return

        # Creamos dict con estado inicial
        tarea = {"texto": texto, "completada": False}
        self.tareas.append(tarea)

        # Mostrar en listbox
        self.listbox.insert(tk.END, texto)

        # Limpiar entrada
        self.entry_tarea.delete(0, tk.END)

    def toggle_task(self):
        """Marca/desmarca la tarea seleccionada como completada."""
        seleccion = self.listbox.curselection()
        if not seleccion:
            messagebox.showinfo("Info", "Selecciona una tarea para marcarla.")
            return

        idx = seleccion[0]
        tarea = self.tareas[idx]

        # Cambiar estado
        tarea["completada"] = not tarea["completada"]

        # Actualizar visualmente en listbox
        self.listbox.delete(idx)
        texto = tarea["texto"]
        if tarea["completada"]:
            texto = "✓ " + texto  # añadir check visual
        self.listbox.insert(idx, texto)

    def delete_task(self):
        """Elimina la tarea seleccionada."""
        seleccion = self.listbox.curselection()
        if not seleccion:
            messagebox.showinfo("Info", "Selecciona una tarea para eliminar.")
            return

        idx = seleccion[0]

        # Confirmación
        if not messagebox.askyesno("Confirmar", "¿Seguro que deseas eliminar esta tarea?"):
            return

        # Eliminar de lista interna y listbox
        self.tareas.pop(idx)
        self.listbox.delete(idx)


def main():
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
