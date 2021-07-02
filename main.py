import tkinter as tk
import pyautogui
import threading
import time


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

        self.keyboard_control_button = tk.Button(self.main_frame, text="Keyboard Input", font=("Rubrik", 20), width=12)
        self.keyboard_control_button.grid(row=0, column=0, padx=5, pady=5)

        self.mouse_control_button = tk.Button(self.main_frame, text="Mouse Input", font=("Rubrik", 20), width=12, command=self.mouse_control_window)
        self.mouse_control_button.grid(row=0, column=1, padx=5, pady=5)

    def set_up_root(self):
        """Set up the root window's settings"""
        self.root.title("AFK Movement Tool")
        self.root.geometry("450x150")
        self.root.resizable(0, 0)
        self.root.config(bg="black")

    def mouse_control_window(self):
        mouse_window = tk.Toplevel()
        mouse_window.title("Mouse Control")
        mouse_window.geometry("450x450")
        mouse_window.resizable(0, 0)
        mouse_window.config(bg="black")

        title_frame = tk.Frame(mouse_window)
        title_frame.pack()

        main_frame = tk.Frame(mouse_window, bg="black")
        main_frame.pack(pady=5)

        slider_frame = tk.Frame(main_frame, bg="black")
        slider_frame.grid(row=0, column=0)

        title = tk.Label(title_frame, text="Mouse Control", font=("Rubrik", 25), bg="black", fg="white")
        title.pack()

        cps_label = tk.Label(slider_frame, text="CPS:", font=("Rubrik", 20), bg="black", fg="white")
        cps_label.grid(row=0, column=0, padx=15)

        cps_slider = tk.Scale(slider_frame, from_=0, to_=100)
        cps_slider.grid(row=0, column=1, padx=15)

        cps_active_button = tk.Button(slider_frame, text="AutoClick", font=("Rubrik", 20), bg="white", fg="black", command=lambda:self.auto_click(cps_slider.get()))
        cps_active_button.grid(row=0, column=2, padx=20)

        tk.Label(mouse_window, text="Slam mouse into any corner of your screen to disable autoclicker", font=("Rubrik", 10), bg="black", fg="white").pack(side=tk.BOTTOM)

        mouse_window.mainloop()

    def auto_click(self, num_clicks):
        while True:
            for i in range(num_clicks):
                pyautogui.click()
                time.sleep(0.01)


if __name__ == "__main__":
    root = tk.Tk()
    AFK_Kick_Window(root)
    root.mainloop()
