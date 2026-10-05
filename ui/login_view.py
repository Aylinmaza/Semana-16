import tkinter as tk
from tkinter import ttk, messagebox
import os

class LoginView(tk.Frame):
    def __init__(self, master, servicio, on_login_success):
        super().__init__(master)
        self.servicio = servicio
        self.on_login_success = on_login_success
        self.pack(fill="both", expand=True)

        # --- Logo seguro ---
        ruta_logo = os.path.join(os.path.dirname(__file__), "..", "assets", "logo.png")
        try:
            self.logo = tk.PhotoImage(file=ruta_logo)
            tk.Label(self, image=self.logo).pack(pady=10)
        except Exception:
            tk.Label(self, text="Restaurante App", font=("Arial", 20, "bold")).pack(pady=10)

        # --- Formulario de login ---
        frame = tk.Frame(self, padx=20, pady=20)
        frame.pack()

        tk.Label(frame, text="Usuario:").grid(row=0, column=0, sticky="w")
        self.entry_usuario = tk.Entry(frame)
        self.entry_usuario.grid(row=0, column=1)

        tk.Label(frame, text="Contraseña:").grid(row=1, column=0, sticky="w")
        self.entry_contrasena = tk.Entry(frame, show="*")
        self.entry_contrasena.grid(row=1, column=1)

        tk.Button(frame, text="Ingresar", command=self.login).grid(row=2, column=0, columnspan=2, pady=10)

    def login(self):
        usuario = self.entry_usuario.get()
        contrasena = self.entry_contrasena.get()
        try:
            u = self.servicio.validar_login(usuario, contrasena)
            messagebox.showinfo("Bienvenido", f"Hola {u['nombre']} ({u['rol']})")
            self.on_login_success(u)
        except Exception as e:
            messagebox.showerror("Error", str(e))
