# -*- coding: utf-8 -*-
"""Python e Tkinter: tk.Button()."""

import tkinter as tk
from pathlib import Path

APPLICATION_NAME = 'br.com.justcode.Tkinter'

BASE_DIR = Path(__file__).resolve().parent
SRC_DIR = BASE_DIR.parent.parent
ICON_WINDOW = SRC_DIR.joinpath('data', 'icons', f'{APPLICATION_NAME}.png')


class MainWindow(tk.Frame):
    def __init__(self, master):
        super().__init__(master=master)
        self.pack(
            expand=True,
            fill=tk.BOTH,
            padx=6,
            pady=6,
        )

        
class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.wm_title('Python e Tkinter: tk.Button().')
        self.iconphoto(False, tk.PhotoImage(file=ICON_WINDOW))

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
