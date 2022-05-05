import random
import string
import tkinter as tk
import qrcode
from PIL import ImageTk, Image

root = tk.Tk()
root.title("QrGen")

okno = tk.Canvas(root, width=600, height=300)
okno.grid(columnspan=3)

welcome_text = tk.Label(text="QR Code Generator", font="Arial")
welcome_text.grid(column=1, row=0)

url_input = tk.Entry(root)
url_input.grid(column=1, row=1)


def generate_qrcode():
    qrcode_img = qrcode.make(url_input.get())
    qrcode_img_name = "".join(random.choices(string.ascii_letters, k=5)) + ".png"
    qrcode_img.save(qrcode_img_name)
    img = ImageTk.PhotoImage(Image.open(qrcode_img_name))
    img_display = tk.Label(root, image=img)
    img_display.image = img
    img_display.grid(column=1, row=3)


submit_btn = tk.Button(text="Generuj", font="Arial", command=lambda: generate_qrcode())
submit_btn.grid(column=1, row=2)
