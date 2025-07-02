#!/usr/bin/env python3
"""Image Encryption Tool GUI

A simple GUI utility that lets you encrypt or decrypt image files
using symmetric (Fernet) encryption.

------------------------------------------------------------
Created by Suvam Biswas – 2025-07-02
------------------------------------------------------------

How it works
============
1. A single symmetric key (stored in ``secret.key``) is generated the
   first time you run the program.  Keep this file safe – without it you
   cannot decrypt your images.
2. Click **Encrypt Image** to pick an image (JPG / PNG / …) and choose
   where to save the ``*.enc`` result.
3. Click **Decrypt Image** to pick a previously‑encrypted ``*.enc`` file
   and restore it back to an image.

Dependencies
============
    pip install cryptography pillow

"""
from __future__ import annotations

import os
from pathlib import Path
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
from cryptography.fernet import Fernet

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
APP_NAME = "🛡️  Image Encryption Tool"
KEY_FILE = Path("secret.key")
WINDOW_SIZE = "500x360"
FONT_HEADER = ("Helvetica", 18, "bold")
FONT_BUTTON = ("Helvetica", 13, "bold")
FONT_FOOTER = ("Helvetica", 9)
BUTTON_STYLE = {
    "bg": "#add8e6",
    "fg": "#ff4444",
    "activebackground": "#5a5a8a",
    "activeforeground": "#ff4444",
    "relief": "raised",
    "bd": 2,
    "cursor": "hand2",
    "highlightthickness": 0,
}

SOCIAL_LINKS = {
    "github": "https://github.com/Ninja-Atmos",
    "linkedin": "https://www.linkedin.com/in/suvam0961/",
    "facebook": "https://www.facebook.com/Suvam0961/",
    "instagram": "https://www.instagram.com/suvam__biswas/",
}

SUPPORTED_IMAGE_TYPES = [
    ("All Image Files", "*.jpg *.jpeg *.png *.bmp *.gif *.tiff *.webp *.ico *.jfif"),
    ("JPEG", "*.jpg *.jpeg *.jfif"),
    ("PNG", "*.png"),
    ("TIFF", "*.tiff"),
    ("Bitmap", "*.bmp"),
    ("GIF", "*.gif"),
    ("WebP", "*.webp"),
    ("ICO", "*.ico"),
    ("All Files", "*.*")
]

# ---------------------------------------------------------------------------
# Key utilities
# ---------------------------------------------------------------------------

def _generate_key() -> bytes:
    key: bytes = Fernet.generate_key()
    KEY_FILE.write_bytes(key)
    return key


def _load_key() -> bytes:
    if not KEY_FILE.exists():
        return _generate_key()
    return KEY_FILE.read_bytes()


def _get_fernet() -> Fernet:
    return Fernet(_load_key())


# ---------------------------------------------------------------------------
# Encryption helpers
# ---------------------------------------------------------------------------

def encrypt_file() -> None:
    src_path = filedialog.askopenfilename(
        title="Select Image File",
        filetypes=SUPPORTED_IMAGE_TYPES,
    )
    if not src_path:
        return

    try:
        data = Path(src_path).read_bytes()
        cipher = _get_fernet()
        encrypted = cipher.encrypt(data)

        dst_path = filedialog.asksaveasfilename(
            title="Save Encrypted File As",
            defaultextension=".enc",
            filetypes=[("Encrypted Files", "*.enc")],
        )
        if not dst_path:
            return

        Path(dst_path).write_bytes(encrypted)
        messagebox.showinfo(APP_NAME, "Image encrypted successfully! ✔️")
    except Exception as err:
        messagebox.showerror(APP_NAME, f"Encryption failed:\n{err}")


def decrypt_file() -> None:
    enc_path = filedialog.askopenfilename(
        title="Select Encrypted File",
        filetypes=[("Encrypted Files", "*.enc")],
    )
    if not enc_path:
        return

    try:
        encrypted_data = Path(enc_path).read_bytes()
        cipher = _get_fernet()
        decrypted = cipher.decrypt(encrypted_data)

        dst_path = filedialog.asksaveasfilename(
            title="Save Decrypted Image As",
            defaultextension=".png",
            filetypes=SUPPORTED_IMAGE_TYPES,
        )
        if not dst_path:
            return

        Path(dst_path).write_bytes(decrypted)
        messagebox.showinfo(APP_NAME, "Image decrypted successfully! ✔️")
    except Exception as err:
        messagebox.showerror(APP_NAME, f"Decryption failed:\n{err}")


# ---------------------------------------------------------------------------
# GUI setup
# ---------------------------------------------------------------------------

def open_link(url):
    import webbrowser
    webbrowser.open(url)


def _build_gui() -> tk.Tk:
    root = tk.Tk()
    root.title(APP_NAME)
    root.geometry(WINDOW_SIZE)
    root.configure(bg="#111120")
    root.resizable(False, False)

    frame = tk.Frame(root, padx=20, pady=20, bg="#111120")
    frame.pack(expand=True, fill=tk.BOTH)

    tk.Label(
        frame,
        text="🔐 Image Encryption Tool",
        font=FONT_HEADER,
        fg="#ffffff",
        bg="#111120"
    ).pack(pady=10)

    tk.Button(
        frame,
        text="🔒 Encrypt Image",
        font=FONT_BUTTON,
        width=24,
        command=encrypt_file,
        bg="#3c3c5c",
        fg="#e0e0ff",
        activebackground="#5a5a8a",
        activeforeground="#e0e0ff",
        relief="flat",
        bd=0,
        cursor="hand2",
        highlightthickness=0
    ).pack(pady=8)

    tk.Button(
        frame,
        text="🔓 Decrypt Image",
        font=FONT_BUTTON,
        width=24,
        command=decrypt_file,
        bg="#3c3c5c",
        fg="#e0e0ff",
        activebackground="#5a5a8a",
        activeforeground="#e0e0ff",
        relief="flat",
        bd=2,
        cursor="hand2",
        highlightthickness=0
    ).pack(pady=8)

    icon_frame = tk.Frame(frame, bg="#111120")
    icon_frame.pack(pady=15)

    for platform, url in SOCIAL_LINKS.items():
        try:
            icon_path = f"icons/{platform}.png"
            icon_img = Image.open(icon_path).resize((24, 24))
            icon_photo = ImageTk.PhotoImage(icon_img)
            btn = tk.Button(
                icon_frame,
                image=icon_photo,
                command=lambda u=url: open_link(u),
                bg="#111120",
                borderwidth=0,
                activebackground="#111120",
                cursor="hand2"
            )
            btn.image = icon_photo
            btn.pack(side=tk.LEFT, padx=10)
        except FileNotFoundError:
            continue

    tk.Label(
        frame,
        text="Created by Suvam Biswas",
        font=FONT_FOOTER,
        fg="#888",
        bg="#111120"
    ).pack(pady=5)

    return root


# ---------------------------------------------------------------------------
# Entrypoint
# ---------------------------------------------------------------------------

def main() -> None:
    app = _build_gui()
    app.mainloop()


if __name__ == "__main__":
    main()
