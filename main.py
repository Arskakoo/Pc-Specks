import tkinter as tk
from tkinter import ttk
from src.component import FindComponents
from src.power import Powerusage

class DashboardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Dashboard")
        self.root.geometry("1020x580")

        self.components_instance = FindComponents()
        self.power_instance = Powerusage()

        # Create and configure the main frame
        self.main_frame = ttk.Frame(root, padding="10")
        self.main_frame.grid(row=0, column=0, sticky=(tk.N, tk.S, tk.W, tk.E))

        # Create labels to display information
        label = ttk.Label(self.main_frame, text='Dashboard', font=('Helvetica', 20))
        label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

        self.display_components()
        self.display_power()

    def display_components(self):
        label = ttk.Label(self.main_frame, text='Specs', font=('Helvetica', 14))
        label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
        # Create labels to display the component information
        os_label = ttk.Label(self.main_frame, text=f"OS: {self.components_instance.os}", style='Dashboard.TLabel', anchor="w")
        os_label.grid(row=2, column=0, padx=14, pady=2, sticky=tk.W)

        processor_label = ttk.Label(self.main_frame, text=f"Processor: {self.components_instance.processor}", style='Dashboard.TLabel', anchor="w")
        processor_label.grid(row=3, column=0, padx=14, pady=2, sticky=tk.W)

        ram_in_gb = self.components_instance.ram / (1024 ** 3)
        ram_label = ttk.Label(self.main_frame, text=f"RAM: {ram_in_gb:.2f} GB", style='Dashboard.TLabel', anchor="w")
        ram_label.grid(row=4, column=0, padx=14, pady=2, sticky=tk.W)

        net_label = ttk.Label(self.main_frame, text=f"Net: {', '.join(self.components_instance.net)}", style='Dashboard.TLabel', anchor="w")
        net_label.grid(row=5, column=0, padx=14, pady=2, sticky=tk.W)

        gpu_label = ttk.Label(self.main_frame, text=f"Graphics card: {self.components_instance.gpu}", style='Dashboard.TLabel', anchor="w")
        gpu_label.grid(row=6, column=0, padx=14, pady=2, sticky=tk.W)

    def display_power(self):
        self.power_label = ttk.Label(self.main_frame, text="Power usage", font=('Helvetica', 14))
        self.power_label.grid(row=8, column=0, padx=10, pady=10, sticky=tk.W)
        self.update_power_label()  # Initial update

    def update_power_label(self):
        label = ttk.Label(self.main_frame, text='Power usage', font=('Helvetica', 14))
        label.grid(row=8, column=0, padx=10, pady=10, sticky=tk.W)
        power_usage_percentage = self.power_instance.measure_power_usage()
        self.power_label.config(text=f"Power: {power_usage_percentage}%", font=('Helvetica', 10))
        self.power_label.grid(row=9, column=0, padx=14, pady=2, sticky=tk.W)
        # Schedule the next update in 500 milliseconds
        self.root.after(2500, self.update_power_label)

if __name__ == '__main__':
    root = tk.Tk()
    app = DashboardApp(root)
    root.mainloop()
