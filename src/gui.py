import argparse
import os
import tkinter as tk
from tkinter import filedialog, messagebox

filename = filedialog.askopenfilename()
messagebox.showinfo(filename, "Going swimingly")
