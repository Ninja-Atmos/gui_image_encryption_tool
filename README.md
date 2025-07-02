# 🛡️ Image Encryption Tool (GUI) Created By Suvam

A secure and user-friendly GUI-based image encryption and decryption tool created using Python. Built with `tkinter` and `cryptography`, this tool allows you to safely encrypt your personal images and decrypt them with a private key.

---

## 🔧 Features

- ✅ Symmetric encryption using **Fernet (AES)**
- ✅ Supports **all common image formats**: JPG, PNG, BMP, GIF, TIFF, WebP, ICO, etc.
- ✅ Easy-to-use **Graphical User Interface**
- ✅ Secure key generation and management
- ✅ Custom social media icons with clickable links
- ✅ Futuristic and aesthetic design
- ✅ Cross-platform support (Windows, macOS, Linux)

---

## 📦 Tools & Technologies Used

- **Python 3**
- `tkinter` (GUI)
- `cryptography` (Fernet encryption)
- `Pillow` (for image icon handling)
- Custom UI styling and icons

---

## 🖥️ How It Works

1. On the first run, the tool generates a `secret.key` file. This key is used for both encryption and decryption.
2. Click `🔒 Encrypt Image` to:
   - Select an image file.
   - Encrypt it securely.
   - Save the `.enc` encrypted version.
3. Click `🔓 Decrypt Image` to:
   - Select a `.enc` file.
   - Decrypt it using the key.
   - Save the result as a valid image file.

⚠️ **IMPORTANT:** Do not delete or share your `secret.key` file. You cannot decrypt files without it!

---

## 🚀 How to Run

### 1. Clone the repository
```bash
git clone https://github.com/Ninja-Atmos/image-encryption-tool.git
cd image-encryption-tool
```

### 2. Install dependencies
```bash
pip install cryptography pillow
```

### 3. Run the tool
```bash
python3 gui_image_encryption_tool.py
```

---

## 📂 Project Structure

```
image-encryption-tool/
├── gui_image_encryption_tool.py     # Main Python GUI script
├── secret.key                       # Auto-generated encryption key
├── icons/                           # Folder with social icon PNGs
│   ├── github.png
│   ├── linkedin.png
│   ├── facebook.png
│   └── instagram.png
├── README.md
└── ...
```

---

## 🔗 Social Links
[GitHub](https://github.com/Ninja-Atmos)  
[LinkedIn](https://www.linkedin.com/in/suvam0961/)  
[Facebook](https://www.facebook.com/Suvam0961/)  
[Instagram](https://www.instagram.com/suvam__biswas/)

---

## ⭐ Show Your Support

If you like this project, consider giving it a ⭐ on GitHub and following me for more awesome tools! 😊
