# -*- coding: utf-8 -*-
"""Python e Tkinter: filedialog.asksaveasfile()."""
import tkinter as tk
from pathlib import Path
from tkinter import filedialog

APPLICATION_NAME = 'br.com.justcode.Tkinter'
HOME = Path.home()

BASE_DIR = Path(__file__).resolve().parent
SRC_DIR = BASE_DIR.parent.parent
ICON_WINDOW = SRC_DIR.joinpath('data', 'icons', f'{APPLICATION_NAME}.png')


class MainWindow(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack(
            expand=True,
            fill=tk.BOTH,
            padx=6,
            pady=6,
        )

        # scrollbar = tk.Scrollbar(master=self)
        # scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.text = tk.Text(master=self)
        self.text.insert(index=tk.INSERT, chars='Olá Mundo')
        self.text.pack(expand=True, fill=tk.X)

        button = tk.Button(
            master=self,
            text='Abrir diálogo',
            command=self.on_button_clicked,
        )
        button.pack(expand=False)

    def on_button_clicked(self):
        result = filedialog.asksaveasfile(
            parent=self,
            initialdir=HOME,
            filetypes=[('txt', '*.txt'), ('python', '*.py')],
        )
        if result:
            result.write(self.text.get(index1='1.0', index2=tk.END))


class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.wm_title('Python e Tkinter: filedialog.asksaveasfile().')
        self.iconphoto(False, tk.PhotoImage(file=ICON_WINDOW))

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        self.geometry(newGeometry=f'{int(screen_width / 2)}x{int(screen_height / 2)}')
        self.minsize(width=int(screen_width / 3), height=int(screen_height / 3))

if __name__ == '__main__':
    import sys

    if sys.platform == 'win32':
        from ctypes import windll

        windll.shell32.SetCurrentProcessExplicitAppUserModelID(
            APPLICATION_NAME,
        )

    application = Application()
    app = MainWindow(master=application)
    app.mainloop()
