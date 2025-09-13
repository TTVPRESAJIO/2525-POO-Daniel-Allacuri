import json
import tkinter as tk
from tkinter import ttk, messagebox, filedialog

# Nombre por defecto del archivo para guardar/cargar
DEFAULT_FILENAME = "datos.json"


class App:
    """Aplicación principal: gestor visual de ítems con persistencia JSON."""

    def __init__(self, root):
        """Inicializa la GUI y las estructuras internas."""
        self.root = root
        self.root.title("Gestor Visual — Lista de Ítems")
        # contador simple para generar IDs únicos en la sesión
        self._next_id = 1
        # Diccionario interno: id(int) -> texto(str)
        self.items = {}

        # --- Layout ---
        # Marco superior: entrada y botones
        top_frame = ttk.Frame(root, padding=(10, 10, 10, 5))
        top_frame.pack(fill="x")

        ttk.Label(top_frame, text="Escribe un ítem:").pack(side="left")
        self.entry = ttk.Entry(top_frame)
        self.entry.pack(side="left", fill="x", expand=True, padx=(6, 6))
        self.entry.focus()  # coloca el foco en el campo al iniciar

        btn_add = ttk.Button(top_frame, text="Agregar", command=self.add_item)
        btn_add.pack(side="left", padx=(0, 6))

        btn_clear = ttk.Button(top_frame, text="Limpiar", command=self.clear_entry)
        btn_clear.pack(side="left")

        # Bind: Enter en el entry también agrega el ítem
        self.entry.bind("<Return>", self._on_enter_pressed)

        # --- Marco central: tabla / lista (Treeview) ---
        mid_frame = ttk.Frame(root, padding=(10, 5, 10, 5))
        mid_frame.pack(fill="both", expand=True)

        columns = ("id", "texto")
        self.tree = ttk.Treeview(mid_frame, columns=columns, show="headings", selectmode="extended")
        self.tree.heading("id", text="ID")
        self.tree.heading("texto", text="Texto")
        self.tree.column("id", width=60, anchor="center")
        self.tree.column("texto", anchor="w")

        # Scrollbar vertical
        vsb = ttk.Scrollbar(mid_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=vsb.set)
        vsb.pack(side="right", fill="y")
        self.tree.pack(side="left", fill="both", expand=True)

        # Doble click en fila -> mostrar detalles
        self.tree.bind("<Double-1>", self._on_item_double_click)

        # --- Marco inferior: acciones adicionales ---
        bottom_frame = ttk.Frame(root, padding=(10, 5, 10, 10))
        bottom_frame.pack(fill="x")

        btn_delete = ttk.Button(bottom_frame, text="Eliminar seleccionado", command=self.delete_selected)
        btn_delete.pack(side="left")

        btn_save = ttk.Button(bottom_frame, text="Guardar (JSON)", command=self.save_to_file)
        btn_save.pack(side="left", padx=(6, 6))

        btn_load = ttk.Button(bottom_frame, text="Cargar (JSON)", command=self.load_from_file)
        btn_load.pack(side="left")

        # Botón para importar desde un archivo seleccionado por el usuario
        btn_import = ttk.Button(bottom_frame, text="Importar archivo...", command=self.import_file)
        btn_import.pack(side="right")

    # ----------------- Operaciones -----------------
    def add_item(self):
        """Agrega el texto de entry a la tabla si no está vacío."""
        texto = self.entry.get().strip()
        if not texto:
            messagebox.showwarning("Aviso", "El campo está vacío. Escribe algo antes de agregar.")
            return

        _id = self._next_id
        self._next_id += 1

        # Guardamos en estructura interna y mostramos en la tabla
        self.items[_id] = texto
        self.tree.insert("", "end", iid=str(_id), values=(_id, texto))

        # Limpiamos el campo y devolvemos el foco
        self.entry.delete(0, tk.END)
        self.entry.focus()

    def _on_enter_pressed(self, event):
        """Handler para Enter (viene con un evento)."""
        self.add_item()
        return "break"  # evita que se produzcan comportamientos por defecto

    def clear_entry(self):
        """Limpia el campo de texto."""
        self.entry.delete(0, tk.END)
        self.entry.focus()

    def delete_selected(self):
        """Elimina las filas seleccionadas del Treeview y del diccionario interno."""
        seleccion = self.tree.selection()
        if not seleccion:
            messagebox.showinfo("Eliminar", "No hay filas seleccionadas.")
            return

        # Pregunta de confirmación
        if not messagebox.askyesno("Confirmar", "¿Deseas eliminar las filas seleccionadas?"):
            return

        for iid in seleccion:
            try:
                _id = int(iid)
            except ValueError:
                continue
            # eliminar del tree y del dict
            self.tree.delete(iid)
            self.items.pop(_id, None)

    def _on_item_double_click(self, event):
        """Muestra una ventana con detalles del elemento al hacer double-click."""
        sel = self.tree.selection()
        if not sel:
            return
        iid = sel[0]
        try:
            _id = int(iid)
            texto = self.items.get(_id, "<sin dato>")
        except ValueError:
            return

        messagebox.showinfo("Detalle del ítem", f"ID: {_id}\nTexto: {texto}")

    # ----------------- Persistencia en JSON -----------------
    def save_to_file(self, filename: str = DEFAULT_FILENAME):
        """Guarda los ítems actuales en un archivo JSON."""
        data = [{"id": k, "texto": v} for k, v in self.items.items()]
        try:
            with open(filename, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
        except PermissionError:
            messagebox.showerror("Error", "No se tienen permisos para escribir el archivo.")
            return
        except Exception as e:
            messagebox.showerror("Error", f"Error al guardar: {e}")
            return

        messagebox.showinfo("Guardar", f"Datos guardados en '{filename}'.")

    def load_from_file(self, filename: str = DEFAULT_FILENAME):
        """Carga ítems desde el archivo JSON (reemplaza la lista actual)."""
        try:
            with open(filename, "r", encoding="utf-8") as f:
                data = json.load(f)
            if not isinstance(data, list):
                raise ValueError("Formato de archivo inválido.")
        except FileNotFoundError:
            messagebox.showwarning("Cargar", f"El archivo '{filename}' no existe.")
            return
        except json.JSONDecodeError:
            messagebox.showerror("Cargar", f"El archivo '{filename}' no contiene JSON válido.")
            return
        except PermissionError:
            messagebox.showerror("Error", "No se tienen permisos para leer el archivo.")
            return
        except Exception as e:
            messagebox.showerror("Error", f"Error al cargar: {e}")
            return

        # Limpiar datos actuales
        self.items.clear()
        for row in self.tree.get_children():
            self.tree.delete(row)

        # Reconstruir a partir de los datos guardados
        max_id = 0
        for entry in data:
            try:
                _id = int(entry.get("id"))
                texto = str(entry.get("texto", ""))
            except Exception:
                continue
            self.items[_id] = texto
            self.tree.insert("", "end", iid=str(_id), values=(_id, texto))
            if _id > max_id:
                max_id = _id

        # Asegurar que el próximo ID siga después del máximo cargado
        self._next_id = max_id + 1
        messagebox.showinfo("Cargar", f"Datos cargados desde '{filename}'.")

    def import_file(self):
        """Permite al usuario elegir un archivo JSON a importar (carga)."""
        path = filedialog.askopenfilename(title="Selecciona archivo JSON",
                                          filetypes=[("JSON files", "*.json"), ("All files", "*.*")])
        if path:
            self.load_from_file(path)


def main():
    root = tk.Tk()
    app = App(root)
    root.geometry("700x420")  # tamaño inicial (opcional)
    root.mainloop()


if __name__ == "__main__":
    main()
