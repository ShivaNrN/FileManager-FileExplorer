from tkinter import Tk
from tkinter.filedialog import askdirectory


def ask_directory(title="Choose a directory"):
    Tk().withdraw()  # .withdraw --> method to untoggle an superflous dialog window.
    path = askdirectory(title=title)
    return path
