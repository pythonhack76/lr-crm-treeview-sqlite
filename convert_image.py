from PIL import Image
import tkinter as tk
from tkinter import filedialog
from pathlib import Path

def convert_png_to_ico(input_file, output_folder):
    try:
        img = Image.open(input_file)
        input_file_path = Path(input_file)
        output_file = f"{output_folder}/{input_file_path.stem}.ico"
        img.save(output_file, format="ICO")
        result_label.config(text=f"Conversione completata: {input_file} => {output_file}")
    except Exception as e:
        result_label.config(text=f"Si è verificato un errore: {e}")

def browse_input_file():
    file_path = filedialog.askopenfilename(filetypes=[("PNG Files", "*.png")])
    input_file_entry.delete(0, tk.END)
    input_file_entry.insert(0, file_path)

def browse_output_folder():
    folder_path = filedialog.askdirectory()
    output_folder_entry.delete(0, tk.END)
    output_folder_entry.insert(0, folder_path)

# Creazione della finestra principale
root = tk.Tk()
root.title("Convertitore PNG to ICO")

# Etichette e campi di input
input_label = tk.Label(root, text="Seleziona il file PNG di input:")
input_label.pack()
input_file_entry = tk.Entry(root)
input_file_entry.pack()
input_browse_button = tk.Button(root, text="Sfoglia", command=browse_input_file)
input_browse_button.pack()

output_label = tk.Label(root, text="Seleziona la cartella di destinazione:")
output_label.pack()
output_folder_entry = tk.Entry(root)
output_folder_entry.pack()
output_browse_button = tk.Button(root, text="Sfoglia", command=browse_output_folder)
output_browse_button.pack()

convert_button = tk.Button(root, text="Converti", command=lambda: convert_png_to_ico(input_file_entry.get(), output_folder_entry.get()))
convert_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
