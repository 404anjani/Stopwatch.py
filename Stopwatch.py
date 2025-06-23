import tkinter as tk

class Stopwatch:
    def __init__(self, root):
        self.root = root
        self.root.title("Stopwatch")

        self.running = False
        self.time = 0

        self.label = tk.Label(root, text="00:00:00", font=("Arial", 40))
        self.label.pack(pady=20)

        self.start_button = tk.Button(root, text="Start", command=self.start, width=10)
        self.start_button.pack(side="left", padx=10, pady=10)

        self.stop_button = tk.Button(root, text="Stop", command=self.stop, width=10)
        self.stop_button.pack(side="left", padx=10, pady=10)

        self.reset_button = tk.Button(root, text="Reset", command=self.reset, width=10)
        self.reset_button.pack(side="left", padx=10, pady=10)

    def update(self):
        if self.running:
            self.time += 1
            minutes, seconds = divmod(self.time, 60)
            hours, minutes = divmod(minutes, 60)
            self.label.config(text=f"{hours:02d}:{minutes:02d}:{seconds:02d}")
            self.root.after(1000, self.update)

    def start(self):
        if not self.running:
            self.running = True
            self.update()

    def stop(self):
        self.running = False

    def reset(self):
        self.running = False
        self.time = 0
        self.label.config(text="00:00:00")

if __name__ == "__main__":
    root = tk.Tk()
    app = Stopwatch(root)
    root.mainloop()