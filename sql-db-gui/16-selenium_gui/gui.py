import tkinter as tk
from tkinter import messagebox
import threading
from automation import run_automation


class AutomationGUI:

    def __init__(self, root):
        self.root = root
        self.root.title("DemoQA Automation")
        self.root.geometry("400x450")

        self.create_widgets()

    def create_widgets(self):

        labels = [
            "Username",
            "Password",
            "Full Name",
            "Email",
            "Current Address",
            "Permanent Address"
        ]

        self.entries = {}

        for label in labels:
            tk.Label(self.root, text=label).pack(pady=5)

            entry = tk.Entry(
                self.root,
                width=40,
                show="*" if label == "Password" else None
            )
            entry.pack()

            self.entries[label] = entry

        tk.Button(
            self.root,
            text="Run Automation",
            command=self.start_thread,
            bg="green",
            fg="white"
        ).pack(pady=20)

    def start_thread(self):
        threading.Thread(target=self.run).start()

    def run(self):
        try:
            run_automation(
                self.entries["Username"].get(),
                self.entries["Password"].get(),
                self.entries["Full Name"].get(),
                self.entries["Email"].get(),
                self.entries["Current Address"].get(),
                self.entries["Permanent Address"].get(),
            )

            messagebox.showinfo("Success", "Automation Completed Successfully!")

        except Exception as e:
            messagebox.showerror("Error", str(e))


if __name__ == "__main__":
    root = tk.Tk()
    app = AutomationGUI(root)
    root.mainloop()