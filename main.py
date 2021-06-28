import tkinter as tk
import pyautogui


class AFK_Kick_Window:
    """A class that requires a root window to be passed"""
    def __init__(self, root):
        self.root = root
        self.set_up_root()

        self.title_frame = tk.Frame(root)
        self.title_frame.pack()

        self.main_frame = tk.Frame(root, bg="black")
        self.main_frame.pack(pady=5)

        self.title = tk.Label(self.title_frame, text="Anti AFK Tool", font=("Rubrik", 25), bg="black", fg="white")
        self.title.pack()

        tk.Label(root, text="Press any button to stop the commands", font=("Rubrik", 15), bg="black", fg="white").pack(side=tk.BOTTOM)

        self.keyboard_control_button = tk.Button(self.main_frame, text="Keyboard Input", font=("Rubrik", 20), width=12)
        self.keyboard_control_button.grid(row=0, column=0, padx=5, pady=5)

        self.mouse_control_button = tk.Button(self.main_frame, text="Mouse Input", font=("Rubrik", 20), width=12)
        self.mouse_control_button.grid(row=0, column=1, padx=5, pady=5)

    def set_up_root(self):
        """Set up the root window's settings"""
        self.root.title("AFK Movement Tool")
        self.root.geometry("450x150")
        self.root.resizable(0, 0)
        self.root.config(bg="black")


if __name__ == "__main__":
    root = tk.Tk()
    AFK_Kick_Window(root)
    root.mainloop()
