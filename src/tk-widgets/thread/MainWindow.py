# -*- coding: utf-8 -*-
"""Python e Tkinter: tk.Label() com threading."""

import threading
import time
import tkinter as tk
from pathlib import Path

APPLICATION_NAME = 'br.com.justcode.Tkinter'

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

        label = tk.Label(
            master=self,
            text='Utilizando threading para não congelar a interface.',
        )
        label.pack(expand=True, fill=tk.X)

        self.str_var = tk.StringVar()
        self.str_var.set('Contagem: 0.')
        label = tk.Label(
            master=self,
            textvariable=self.str_var,
        )
        label.pack(expand=True, fill=tk.X)

        self.button_countdown = tk.Button(
            master=self,
            text='Iniciar contagem',
            command=self.countdown_thread,
        )
        self.button_countdown.pack(expand=True)

        button = tk.Button(
            master=self,
            text='Clique aqui',
            command=self.on_button_clicked,
        )
        button.pack(expand=True)

    def countdown(self):
        self.button_countdown['state'] = tk.DISABLED
        for number in range(1, 31):
            self.str_var.set(f'Contagem: {number}.')
            print(number)
            time.sleep(1)
        self.button_countdown['state'] = tk.ACTIVE

    def countdown_thread(self):
        thread = threading.Thread(daemon=True, target=self.countdown)
        thread.start()

    def on_button_clicked(self):
        print('Botão pressionado')


class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.wm_title('Python e Tkinter: tk.Label() com threading.')
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
