import tkinter as tk
from tkinter import messagebox

class NotesApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Менеджер нотаток")
        self.root.geometry("400x500")
        self.root.configure(bg="#f0f0f0")

        self.label = tk.Label(self.root, text="Напишіть нотатку нижче:", bg="#f0f0f0", font=("Arial", 10, "bold"))
        self.label.pack(pady=(20, 5))

        self.entry = tk.Entry(self.root, width=35, font=("Arial", 12), bd=2)
        self.entry.pack(pady=5, padx=20)
        self.entry.bind('<Return>', lambda event: self.add_note())

        self.add_button = tk.Button(self.root, text="➕ додати нотатку", command=self.add_note,
                                    bg="#4caf50", fg="white", font=("Arial", 10, "bold"), width=20)
        self.add_button.pack(pady=10)

        self.listbox = tk.Listbox(self.root, width=40, height=12, font=("Arial", 11), selectmode=tk.SINGLE)
        self.listbox.pack(pady=10, padx=20)

        self.delete_button = tk.Button(self.root, text="🗑️ видалити обране", command=self.delete_note,
                                       bg="#f44336", fg="white", width=20)
        self.delete_button.pack(pady=5)

        self.clear_button = tk.Button(self.root, text="🧹 очистити все", command=self.clear_all,
                                      bg="#2196f3", fg="white", width=20)
        self.clear_button.pack(pady=5)

    def add_note(self):
        text = self.entry.get().strip()
        if text:
            self.listbox.insert(tk.END, text)
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Помилка", "Не можна додати порожню нотатку!")

    def delete_note(self):
        selection = self.listbox.curselection()
        if selection:
            index = selection[0]
            self.listbox.delete(index)
        else:
            messagebox.showinfo("Підсказка", "Будь ласка, спочатку оберіть нотатку зі списку")

    def clear_all(self):
        confirm = messagebox.askyesno("Підтвердження", "Ви впевнені, що хочете видалити всі нотатки?")
        if confirm:
            self.listbox.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = NotesApp(root)
    root.mainloop()
