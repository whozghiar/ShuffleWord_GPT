import tkinter as tk
from tkinter import filedialog, messagebox
from file_handler import extract_text_from_file, save_text_to_file
from shuffle_logic import shuffle_text

def process_text_input(text_input):
    """Traite le texte entré par l'utilisateur et invite à enregistrer le fichier."""
    try:
        text = text_input.get("1.0", tk.END).strip()
        if not text:
            messagebox.showwarning("Attention", "Veuillez entrer du texte avant de traiter.")
            return

        shuffled = shuffle_text(text)
        save_file_dialog(shuffled)
    except Exception as e:
        messagebox.showerror("Erreur", f"Erreur lors du traitement : {e}")

def process_file_input():
    """Traite le fichier téléversé par l'utilisateur et invite à enregistrer le fichier."""
    try:
        filepath = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("PDF files", "*.pdf"), ("Word documents", "*.docx")])
        if not filepath:
            messagebox.showwarning("Attention", "Aucun fichier sélectionné.")
            return

        text = extract_text_from_file(filepath)
        shuffled = shuffle_text(text)
        save_file_dialog(shuffled)
    except Exception as e:
        messagebox.showerror("Erreur", f"Erreur lors du traitement du fichier : {e}")

def save_file_dialog(text):
    """Ouvre une boîte de dialogue pour enregistrer le fichier dans le format choisi."""
    try:
        filetypes = [
            ("Fichier texte", "*.txt"),
            ("Document ODT", "*.odt")
        ]
        filepath = filedialog.asksaveasfilename(filetypes=filetypes, defaultextension=filetypes)
        if not filepath:
            messagebox.showinfo("Info", "Enregistrement annulé.")
            return

        file_format = filepath.split(".")[-1]
        save_text_to_file(text, filepath, file_format)
        messagebox.showinfo("Succès", f"Fichier enregistré avec succès : {filepath}")
    except Exception as e:
        messagebox.showerror("Erreur", f"Erreur lors de l'enregistrement : {e}")

def create_gui():
    """Crée l'interface graphique de l'application."""
    window = tk.Tk()
    window.title("Mélangeur de lettres")

    # Options : Texte ou fichier
    mode_frame = tk.Frame(window)
    mode_frame.pack(pady=10)

    tk.Label(mode_frame, text="Choisissez une option :").pack()

    # Texte manuel
    text_frame = tk.Frame(window)
    file_frame = tk.Frame(window)

    def show_text_mode():
        file_frame.pack_forget()
        text_frame.pack()

    def show_file_mode():
        text_frame.pack_forget()
        file_frame.pack()

    tk.Button(mode_frame, text="Entrer du texte", command=show_text_mode).pack(side=tk.LEFT, padx=5)
    tk.Button(mode_frame, text="Téléverser un fichier", command=show_file_mode).pack(side=tk.RIGHT, padx=5)

    # Zone de texte
    tk.Label(text_frame, text="Entrez votre texte ci-dessous :").pack()
    text_input = tk.Text(text_frame, height=10, width=50)
    text_input.pack()

    tk.Button(text_frame, text="Mélanger les mots", command=lambda: process_text_input(text_input)).pack(pady=5)

    # Téléversement de fichier
    file_label = tk.Label(file_frame, text="Aucun fichier sélectionné.")
    file_label.pack()

    tk.Button(file_frame, text="Choisir un fichier", command=process_file_input).pack(pady=5)

    window.mainloop()
