import qrcode
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def generate_qr_code():
    data=entry.get()
    if not data:
        messagebox.showwarning("Input Error", "Please enter some data to generate a QR code.")
        return
    qr=qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img.save("generated_qr.png")
    qr_image = Image.open("generated_qr.png")
    qr_image = qr_image.resize((250, 250))  # Resize to fit the window
    qr_photo = ImageTk.PhotoImage(qr_image)
    qr_label.config(image=qr_photo)
    qr_label.image = qr_photo
    messagebox.showinfo("Success", "QR Code generated successfully!")
    
root = tk.Tk()
root.title("QR Code Generator")
root.geometry("400x500")
label = tk.Label(root, text="Enter data to generate a QR Code:", font=("Arial", 12))
label.pack(pady=20)
entry = tk.Entry(root, width=40)
entry.pack(pady=10)
button = tk.Button(root, text="Generate QR Code", command=generate_qr_code, font=("Arial", 12))
button.pack(pady=20)
qr_label = tk.Label(root)
qr_label.pack(pady=20)
root.mainloop()