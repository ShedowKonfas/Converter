from PIL import Image
import tkinter as tk
from tkinter import ttk

def convert():
    InputIm = dis_entry.get()
    OutputIm = vibor_entry.get()
    img = Image.open(InputIm)
    img.save(f"output.{OutputIm}")

root = tk.Tk()
root.geometry("300x175")
root.title("Converter")
root.resizable(False, False)

dis = tk.StringVar()
vibor = tk.StringVar()
agreement = tk.StringVar()

frame = ttk.Frame(root)
frame.pack(padx=10, pady=10, fill='x', expand=True)

dis_label = ttk.Label(frame, text="Название файла: ")
dis_label.pack(fill='x', expand=True)

dis_entry = ttk.Entry(frame, textvariable=dis)
dis_entry.pack(fill='x', expand=True)
dis_entry.focus()

vibor_label = ttk.Label(frame, text="Во что сконвертировать: ")
vibor_label.pack(fill='x', expand=True)

vibor_entry = ttk.Entry(frame, textvariable=vibor)
vibor_entry.pack(fill='x', expand=True)

btn_convert = tk.Button(frame, text="Сконвертировать", command=convert)
btn_convert.pack()

root.mainloop()