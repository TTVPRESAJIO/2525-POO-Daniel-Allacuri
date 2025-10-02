# BLOCK DE NOTAS GUI

import tkinter as tk
from tkinter import ttk, messagebox


class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas Pendientes")
        self.root.geometry("450x400")

        # Lista de tareas internas
        self.tareas = []

        # Frame superior: entrada y botón
        frame_top = ttk.Frame(root, padding=10)
        frame_top.pack(fill="x")

        self.entry = ttk.Entry(frame_top)
        self.entry.pack(side="left", fill="x", expand=True, padx=(0, 6))
        self.entry.focus()

        btn_add = ttk.Button(frame_top, text="Añadir Tarea", command=self.add_task)
        btn_add.pack(side="left")

        # Frame central: Listbox con Scrollbar
        frame_center = ttk.Frame(root, padding=10)
        frame_center.pack(fill="both", expand=True)

        self.listbox = tk.Listbox(
            frame_center,
            selectmode="single",
            height=15,
            font=("Segoe UI", 11)
        )
        self.listbox.pack(side="left", fill="both", expand=True)

        scrollbar = ttk.Scrollbar(frame_center, orient="vertical", command=self.listbox.yview)
        self.listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        # Frame inferior: botones de acción
        frame_bottom = ttk.Frame(root, padding=10)
        frame_bottom.pack(fill="x")

        btn_done = ttk.Button(frame_bottom, text="Marcar como Completada", command=self.toggle_task)
        btn_done.pack(side="left", padx=5)

        btn_delete = ttk.Button(frame_bottom, text="Eliminar Tarea", command=self.delete_task)
        btn_delete.pack(side="left", padx=5)

        btn_exit = ttk.Button(frame_bottom, text="Salir", command=self.root.quit)
        btn_exit.pack(side="right")

        # Atajos de teclado
        self.entry.bind("<Return>", lambda e: self.add_task())   # Enter = añadir
        root.bind("<c>", lambda e: self.toggle_task())           # c = completar
        root.bind("<C>", lambda e: self.toggle_task())           # C = completar
        root.bind("<d>", lambda e: self.delete_task())           # d = eliminar
        root.bind("<D>", lambda e: self.delete_task())           # D = eliminar
        root.bind("<Delete>", lambda e: self.delete_task())      # Supr = eliminar
        root.bind("<Escape>", lambda e: root.quit())             # Escape = salir

    # Lógica principal
    def add_task(self):
        """Añadir una nueva tarea a la lista."""
        texto = self.entry.get().strip()
        if not texto:
            messagebox.showwarning("Aviso", "Escribe una tarea antes de añadir.")
            return

        tarea = {"texto": texto, "completada": False}
        self.tareas.append(tarea)

        self.listbox.insert(tk.END, texto)
        self.entry.delete(0, tk.END)

    def toggle_task(self):
        #Marcar o desmarcar la tarea seleccionada como completada
        seleccion = self.listbox.curselection()
        if not seleccion:
            return
        idx = seleccion[0]
        tarea = self.tareas[idx]

        tarea["completada"] = not tarea["completada"]

        # Actualizar visual en la lista
        self.listbox.delete(idx)
        texto = tarea["texto"]

        if tarea["completada"]:
            self.listbox.insert(idx, texto)
            self.listbox.itemconfig(idx, fg="gray", font=("Segoe UI", 11, "overstrike"))
        else:
            self.listbox.insert(idx, texto)
            self.listbox.itemconfig(idx, fg="black", font=("Segoe UI", 11, "normal"))

    def delete_task(self):
        #Elimina la tarea seleccionada
        seleccion = self.listbox.curselection()
        if not seleccion:
            return
        idx = seleccion[0]

        if not messagebox.askyesno("Confirmar", "¿Seguro que deseas eliminar esta tarea?"):
            return

        self.tareas.pop(idx)
        self.listbox.delete(idx)


def main():
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
