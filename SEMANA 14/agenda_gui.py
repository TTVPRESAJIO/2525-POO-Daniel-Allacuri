# Agenda personal con Tkinter:

import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

# intentamos usar tkcalendar para un DatePicker
try:
    from tkcalendar import DateEntry
    HAS_TKCALENDAR = True
except Exception:
    HAS_TKCALENDAR = False


class AgendaApp:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Agenda Personal")
        self.root.geometry("760x420")

        # estructura interna: lista de eventos
        self.eventos = []

        # entrada de datos
        frame_top = ttk.Frame(root, padding=(10, 10))
        frame_top.pack(fill="x")

        # fecha
        lbl_fecha = ttk.Label(frame_top, text="Fecha:")
        lbl_fecha.grid(row=0, column=0, sticky="w")

        if HAS_TKCALENDAR:
            # DateEntry muestra un calendario desplegable
            self.input_fecha = DateEntry(frame_top, date_pattern="yyyy-mm-dd")
        else:
            # campo texto con instrucción de formato YYYY-MM-DD
            self.input_fecha = ttk.Entry(frame_top)
            self.input_fecha.insert(0, "YYYY-MM-DD")  # placeholder (no nativo)
            # limpia placeholder al hacer foco
            self.input_fecha.bind("<FocusIn>", self._clear_fecha_placeholder)
        self.input_fecha.grid(row=0, column=1, padx=(6, 12), sticky="ew")

        # hora
        lbl_hora = ttk.Label(frame_top, text="Hora (HH:MM):")
        lbl_hora.grid(row=0, column=2, sticky="w")
        self.input_hora = ttk.Entry(frame_top, width=10)
        self.input_hora.insert(0, "09:00")
        self.input_hora.grid(row=0, column=3, padx=(6, 12))

        # descripción
        lbl_desc = ttk.Label(frame_top, text="Descripción:")
        lbl_desc.grid(row=1, column=0, sticky="w", pady=(8, 0))
        self.input_desc = ttk.Entry(frame_top)
        self.input_desc.grid(row=1, column=1, columnspan=3, sticky="ew", padx=(6, 12), pady=(8, 0))

        # configurar columnas de grid para que la entrada crezca
        frame_top.columnconfigure(1, weight=1)
        frame_top.columnconfigure(2, weight=0)
        frame_top.columnconfigure(3, weight=0)

        # botones Add / Clear
        btn_frame = ttk.Frame(frame_top)
        btn_frame.grid(row=2, column=0, columnspan=4, pady=(10, 0), sticky="e")
        btn_add = ttk.Button(btn_frame, text="Agregar Evento", command=self.agregar_evento)
        btn_add.pack(side="left", padx=(0, 8))
        btn_clear_inputs = ttk.Button(btn_frame, text="Limpiar Entradas", command=self.limpiar_entradas)
        btn_clear_inputs.pack(side="left")

        # FRAME central: lista
        frame_center = ttk.Frame(root, padding=(10, 8))
        frame_center.pack(fill="both", expand=True)

        columns = ("fecha", "hora", "descripcion")
        self.tree = ttk.Treeview(frame_center, columns=columns, show="headings", selectmode="browse")
        self.tree.heading("fecha", text="Fecha")
        self.tree.heading("hora", text="Hora")
        self.tree.heading("descripcion", text="Descripción")
        self.tree.column("fecha", width=110, anchor="center")
        self.tree.column("hora", width=80, anchor="center")
        self.tree.column("descripcion", anchor="w")

        # Scrollbars
        vsb = ttk.Scrollbar(frame_center, orient="vertical", command=self.tree.yview)
        hsb = ttk.Scrollbar(frame_center, orient="horizontal", command=self.tree.xview)
        self.tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        vsb.pack(side="right", fill="y")
        hsb.pack(side="bottom", fill="x")
        self.tree.pack(side="left", fill="both", expand=True)

        # doble clic sobre un evento muestra detalles
        self.tree.bind("<Double-1>", self._detalle_evento)

        # FRAME inferior: acciones
        frame_bottom = ttk.Frame(root, padding=(10, 8))
        frame_bottom.pack(fill="x")
        btn_delete = ttk.Button(frame_bottom, text="Eliminar Evento Seleccionado", command=self.eliminar_evento)
        btn_delete.pack(side="left")
        btn_exit = ttk.Button(frame_bottom, text="Salir", command=self.root.quit)
        btn_exit.pack(side="right")

        # Atajos / Bindings
        root.bind("<Control-n>", lambda e: self.agregar_evento())  # Ctrl+N para nuevo evento
        root.bind("<Delete>", lambda e: self.eliminar_evento())    # Supr elimina seleccionado

    # helpers y validaciones
    def _clear_fecha_placeholder(self, event):
        # limpia el placeholder inicial si existe (solo en modo sin tkcalendar)
        widget = event.widget
        if widget.get() == "YYYY-MM-DD":
            widget.delete(0, tk.END)

    def validar_fecha(self, fecha_texto: str) -> bool:

        try:
            datetime.strptime(fecha_texto, "%Y-%m-%d")
            return True
        except Exception:
            return False

    def validar_hora(self, hora_texto: str) -> bool:

        try:
            datetime.strptime(hora_texto, "%H:%M")
            return True
        except Exception:
            return False

    # operaciones principales
    def agregar_evento(self):

        fecha = self.input_fecha.get().strip()
        hora = self.input_hora.get().strip()
        desc = self.input_desc.get().strip()

        # validaciones
        if not fecha or not hora or not desc:
            messagebox.showwarning("Campos incompletos", "Rellena fecha, hora y descripción.")
            return

        if not self.validar_fecha(fecha):
            messagebox.showerror("Fecha inválida", "Formato de fecha inválido. Usa YYYY-MM-DD.")
            return

        if not self.validar_hora(hora):
            messagebox.showerror("Hora inválida", "Formato de hora inválido. Usa HH:MM (24h).")
            return

        # construir evento y añadirlo
        evento = {"fecha": fecha, "hora": hora, "descripcion": desc}
        self.eventos.append(evento)

        # insertar en treeview con id basado en índice actual
        iid = str(len(self.eventos) - 1)  # ID interno simple
        self.tree.insert("", "end", iid=iid, values=(fecha, hora, desc))

        # limpiar campos y devolver foco
        self.limpiar_entradas()
        self.input_fecha.focus()

    def limpiar_entradas(self):

        if HAS_TKCALENDAR:
            # DateEntry: establecer fecha actual como valor (opcional)
            self.input_fecha.set_date(datetime.today())
        else:
            self.input_fecha.delete(0, tk.END)
            self.input_fecha.insert(0, "YYYY-MM-DD")
        self.input_hora.delete(0, tk.END)
        self.input_hora.insert(0, "09:00")
        self.input_desc.delete(0, tk.END)

    def eliminar_evento(self):

        sel = self.tree.selection()
        if not sel:
            messagebox.showinfo("Eliminar", "No hay ningún evento seleccionado.")
            return

        # confirmación
        if not messagebox.askyesno("Confirmar eliminación", "¿Deseas eliminar el evento seleccionado?"):
            return

        iid = sel[0]
        try:
            idx = int(iid)
        except ValueError:
            # ID inesperado: simplemente eliminar del tree
            self.tree.delete(iid)
            return

        # eliminar de la estructura interna (marcar None o pop)
        if 0 <= idx < len(self.eventos):
            self.eventos[idx] = None  # mantenemos índices para iids simples
        # eliminar de la vista
        self.tree.delete(iid)

    def _detalle_evento(self, event):

        sel = self.tree.selection()
        if not sel:
            return
        iid = sel[0]
        try:
            idx = int(iid)
            ev = self.eventos[idx]
            if ev is None:
                messagebox.showinfo("Detalle", "Evento eliminado.")
                return
            messagebox.showinfo("Detalle del Evento", f"Fecha: {ev['fecha']}\nHora: {ev['hora']}\n\n{ev['descripcion']}")
        except Exception:
            # Si hay problemas al recuperar, mostrar valores directos del tree
            vals = self.tree.item(iid, "values")
            messagebox.showinfo("Detalle del Evento", f"Fecha: {vals[0]}\nHora: {vals[1]}\n\n{vals[2]}")


def main():
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
