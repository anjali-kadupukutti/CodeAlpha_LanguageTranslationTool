import tkinter as tk
from tkinter import ttk, messagebox
from deep_translator import GoogleTranslator

# List of languages
languages = {
    "English": "en",
    "Hindi": "hi",
    "Telugu": "te",
    "Tamil": "ta",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Arabic": "ar",
    "Chinese": "zh-CN",
    "Japanese": "ja"
}

def translate_text():
    text = input_box.get("1.0", tk.END).strip()
    if text == "":
        messagebox.showwarning("Warning", "Please enter some text!")
        return
    source = languages[source_lang.get()]
    target = languages[target_lang.get()]
    result = GoogleTranslator(source=source, target=target).translate(text)
    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, result)

def copy_text():
    root.clipboard_clear()
    root.clipboard_append(output_box.get("1.0", tk.END))
    messagebox.showinfo("Copied", "Translation copied to clipboard!")

# Window setup
root = tk.Tk()
root.title("Language Translation Tool")
root.geometry("600x500")
root.config(bg="#f0f0f0")

# Title
tk.Label(root, text="Language Translation Tool", font=("Arial", 18, "bold"), bg="#f0f0f0").pack(pady=10)

# Source language
tk.Label(root, text="Source Language:", bg="#f0f0f0").pack()
source_lang = ttk.Combobox(root, values=list(languages.keys()), state="readonly", width=20)
source_lang.set("English")
source_lang.pack(pady=5)

# Input box
tk.Label(root, text="Enter Text:", bg="#f0f0f0").pack()
input_box = tk.Text(root, height=5, width=60)
input_box.pack(pady=5)

# Target language
tk.Label(root, text="Target Language:", bg="#f0f0f0").pack()
target_lang = ttk.Combobox(root, values=list(languages.keys()), state="readonly", width=20)
target_lang.set("Hindi")
target_lang.pack(pady=5)

# Translate button
tk.Button(root, text="Translate", command=translate_text, bg="#4CAF50", fg="white", font=("Arial", 12, "bold"), padx=10, pady=5).pack(pady=10)

# Output box
tk.Label(root, text="Translated Text:", bg="#f0f0f0").pack()
output_box = tk.Text(root, height=5, width=60)
output_box.pack(pady=5)

# Copy button
tk.Button(root, text="Copy Translation", command=copy_text, bg="#2196F3", fg="white", font=("Arial", 10), padx=10, pady=5).pack(pady=5)

root.mainloop()
