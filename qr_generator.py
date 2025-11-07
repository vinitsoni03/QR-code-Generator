import qrcode
from qrcode.constants import ERROR_CORRECT_H
from PIL import Image, ImageTk
import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox

# -------------------- Core QR Generator -------------------- #
def generate_qr(text, output_path, fill_color="black", back_color="white", logo_path=None):
    """Generate a QR code with optional logo overlay."""
    qr = qrcode.QRCode(
        version=None,
        error_correction=ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color=fill_color, back_color=back_color).convert("RGB")

    # Overlay logo
    if logo_path:
        try:
            logo = Image.open(logo_path)
            # Resize logo (around 20% of QR code size)
            qr_width, qr_height = img.size
            logo_size = int(qr_width * 0.2)
            logo = logo.resize((logo_size, logo_size), Image.LANCZOS)
            # Center position
            pos = ((qr_width - logo_size) // 2, (qr_height - logo_size) // 2)
            img.paste(logo, pos, mask=logo if logo.mode == "RGBA" else None)
        except Exception as e:
            messagebox.showerror("Logo Error", f"Failed to overlay logo: {e}")
    img.save(output_path)
    return img

# -------------------- Batch from CSV -------------------- #
def batch_generate(csv_path, output_folder, logo_path=None):
    """Generate multiple QR codes from a CSV file."""
    df = pd.read_csv(csv_path)
    for _, row in df.iterrows():
        text = row["text"]
        filename = row.get("filename", "qr.png")
        output_path = f"{output_folder}/{filename}"
        generate_qr(text, output_path, logo_path=logo_path)
    messagebox.showinfo("Batch Complete", "All QR codes generated successfully!")

# -------------------- GUI -------------------- #
class QRGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("QR Code Generator")
        self.root.geometry("450x400")
        self.root.resizable(False, False)

        # Inputs
        tk.Label(root, text="Enter Text or URL:", font=("Arial", 11)).pack(pady=5)
        self.text_entry = tk.Entry(root, width=50)
        self.text_entry.pack(pady=5)

        tk.Button(root, text="Choose Logo (optional)", command=self.choose_logo).pack(pady=5)
        self.logo_path = None

        tk.Button(root, text="Generate QR", bg="#4CAF50", fg="white", command=self.generate_single).pack(pady=8)

        # Batch section
        tk.Label(root, text="--- Batch Mode ---", font=("Arial", 11, "bold")).pack(pady=10)
        tk.Button(root, text="Select CSV File", command=self.select_csv).pack(pady=5)
        tk.Button(root, text="Select Output Folder", command=self.select_folder).pack(pady=5)
        tk.Button(root, text="Generate Batch", bg="#2196F3", fg="white", command=self.generate_batch).pack(pady=8)

        # Preview
        self.preview_label = tk.Label(root)
        self.preview_label.pack(pady=10)

        # Storage
        self.csv_path = None
        self.output_folder = None

    def choose_logo(self):
        self.logo_path = filedialog.askopenfilename(title="Select Logo", filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        if self.logo_path:
            messagebox.showinfo("Logo Selected", f"Logo: {self.logo_path}")

    def select_csv(self):
        self.csv_path = filedialog.askopenfilename(title="Select CSV", filetypes=[("CSV Files", "*.csv")])
        if self.csv_path:
            messagebox.showinfo("CSV Selected", f"File: {self.csv_path}")

    def select_folder(self):
        self.output_folder = filedialog.askdirectory(title="Select Output Folder")
        if self.output_folder:
            messagebox.showinfo("Folder Selected", f"Folder: {self.output_folder}")

    def generate_single(self):
        text = self.text_entry.get().strip()
        if not text:
            messagebox.showerror("Error", "Please enter text or URL.")
            return
        output_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG Files", "*.png")])
        if not output_path:
            return
        img = generate_qr(text, output_path, logo_path=self.logo_path)
        img.thumbnail((180, 180))
        img_tk = ImageTk.PhotoImage(img)
        self.preview_label.config(image=img_tk)
        self.preview_label.image = img_tk
        messagebox.showinfo("Success", f"QR Code saved at:\n{output_path}")

    def generate_batch(self):
        if not self.csv_path or not self.output_folder:
            messagebox.showerror("Error", "Please select CSV and output folder first.")
            return
        batch_generate(self.csv_path, self.output_folder, logo_path=self.logo_path)

# -------------------- Run GUI -------------------- #
if __name__ == "__main__":
    root = tk.Tk()
    app = QRGeneratorApp(root)
    root.mainloop()
