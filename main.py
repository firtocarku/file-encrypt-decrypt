import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from cryptography.fernet import Fernet
import os

def encrypt_file(filepath):
    key = Fernet.generate_key()

    with open(filepath + '.key', 'wb') as filekey:
        filekey.write(key)

    with open(filepath + '.key', 'rb') as filekey:
        key = filekey.read()

    fernet = Fernet(key)

    with open(filepath, 'rb') as file:
        original = file.read()

    encrypted = fernet.encrypt(original)

    with open(filepath, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)

    print(filepath + " Encrypted!")

def decrypt_file(filepath):
    with open(filepath + '.key', 'rb') as filekey:
        key = filekey.read()

    fernet = Fernet(key)

    with open(filepath, 'rb') as enc_file:
        encrypted = enc_file.read()

    decrypted = fernet.decrypt(encrypted)

    with open(filepath, 'wb') as decrypted_file:
        decrypted_file.write(decrypted)

    if os.path.isfile(filepath + '.key'):
        os.remove(filepath + '.key')
    
    print(filepath + " Decrypted!")

def choose_file():
    filepath = filedialog.askopenfilename()
    return filepath

def encryptfile():
    filepath = choose_file()
    if filepath:
        encrypt_file(filepath)

def decryptfile():
    filepath = choose_file()
    if filepath:
        decrypt_file(filepath)

root = tk.Tk()
root.title("File Encryption/Decryption")
root.configure(bg='#1e1e1e')

window_width = 800
window_height = 600
root.geometry(f"{window_width}x{window_height}")

style = ttk.Style()
style.configure('Custom.TButton', font=('Helvetica', 14, 'bold'), background='#1e1e1e', foreground='#1e1e1e', borderwidth=0, relief='flat', padding=10)

button_frame = tk.Frame(root, bg='#1e1e1e')
button_frame.pack(expand=True)

button_width = 20
button_height = 4

button1 = ttk.Button(button_frame, text="Encrypt", command=encryptfile, style='Custom.TButton')
button1.pack(side=tk.LEFT, padx=(50, 10), pady=50)

button2 = ttk.Button(button_frame, text="Decrypt", command=decryptfile, style='Custom.TButton')
button2.pack(side=tk.RIGHT, padx=(10, 50), pady=50)

root.mainloop()
