import tkinter as tk
from tkinter import messagebox

def caesar_cipher(text, shift, mode):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            if mode == 'encrypt':
                result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
            elif mode == 'decrypt':
                result += chr((ord(char) - shift_base - shift) % 26 + shift_base)
        else:
            result += char
    return result

def process_text(mode):
    message = message_entry.get("1.0", tk.END).strip()
    try:
        shift = int(shift_entry.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Shift must be an integer.")
        return

    result = caesar_cipher(message, shift, mode)
    output_entry.delete("1.0", tk.END)
    output_entry.insert(tk.END, result)

# Create GUI window
root = tk.Tk()
root.title("Caesar Cipher")

# Message input
tk.Label(root, text="Enter your message:").pack()
message_entry = tk.Text(root, height=4, width=50)
message_entry.pack()

# Shift input
tk.Label(root, text="Enter shift value:").pack()
shift_entry = tk.Entry(root)
shift_entry.pack()

# Buttons
encrypt_button = tk.Button(root, text="Encrypt", command=lambda: process_text('encrypt'))
encrypt_button.pack(pady=5)

decrypt_button = tk.Button(root, text="Decrypt", command=lambda: process_text('decrypt'))
decrypt_button.pack(pady=5)

# Output area
tk.Label(root, text="Result:").pack()
output_entry = tk.Text(root, height=4, width=50)
output_entry.pack()

# Run GUI loop
root.mainloop()