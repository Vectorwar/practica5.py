import tkinter as tk
from tkinter import filedialog, messagebox, colorchooser


class TextEditorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Editor de Texto de JJ")
        self.root.geometry("900x500")

        self.filename = None

        self.text_area = tk.Text(root, wrap=tk.WORD, undo=True)
        self.text_area.pack(expand=True, fill='both')

        self.menu_bar = tk.Menu(root)
        self.root.config(menu=self.menu_bar)

        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Archivo", menu=self.file_menu)
        self.file_menu.add_command(label="Abrir", accelerator="Ctrl+O", command=self.open_file)
        self.file_menu.add_command(label="Guardar", accelerator="Ctrl+S", command=self.save_file)
        self.file_menu.add_command(label="Borrar", accelerator="Ctrl+E", command=self.clear_text)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Salir", command=self.root.quit)

        self.edit_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Editar", menu=self.edit_menu)
        self.edit_menu.add_command(label="Buscar y Reemplazar", command=self.find_replace)

        self.format_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Formato", menu=self.format_menu)
        self.format_menu.add_command(label="Cambiar Color", command=self.change_color)

        self.root.bind('<Control-o>', lambda event: self.open_file())
        self.root.bind('<Control-s>', lambda event: self.save_file())
        self.root.bind('<Control-e>', lambda event: self.clear_text())

    def open_file(self):
        self.filename = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Archivos de texto", "*.txt"),
                                                                                       ("Todos los archivos", "*.*")])
        if self.filename:
            with open(self.filename, "r") as file:
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.END, file.read())

    def save_file(self):
        if self.filename:
            with open(self.filename, "w") as file:
                file.write(self.text_area.get(1.0, tk.END))
        else:
            self.filename = filedialog.asksaveasfilename(defaultextension=".txt",
                                                         filetypes=[("Archivos de texto", "*.txt"),
                                                                    ("Todos los archivos", "*.*")])
            if self.filename:
                with open(self.filename, "w") as file:
                    file.write(self.text_area.get(1.0, tk.END))

    def clear_text(self):
        self.text_area.delete(1.0, tk.END)

    def change_color(self):
        color = colorchooser.askcolor()[1]
        if color:
            self.text_area.config(fg=color)

    def find_replace(self):
        find_window = tk.Toplevel(self.root)
        find_window.title("Buscar y Reemplazar Archivo")

        tk.Label(find_window, text="Buscar:").grid(row=0, column=0)
        find_entry = tk.Entry(find_window)
        find_entry.grid(row=0, column=1)

        tk.Label(find_window, text="Reemplazar por:").grid(row=1, column=0)
        replace_entry = tk.Entry(find_window)
        replace_entry.grid(row=1, column=1)

        def find_and_replace():
            search_text = find_entry.get()
            replace_text = replace_entry.get()
            text_content = self.text_area.get(1.0, tk.END)
            new_text = text_content.replace(search_text, replace_text)
            self.text_area.delete(1.0, tk.END)
            self.text_area.insert(tk.END, new_text)
            find_window.destroy()

        tk.Button(find_window, text="Reemplazar", command=find_and_replace).grid(row=2, column=1)


if __name__ == "__main__":
    root = tk.Tk()
    app = TextEditorApp(root)
    root.mainloop()
