import psutil
import tkinter as tk
from tkinter import ttk
from plyer import notification  # pip install plyer

class BatteryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🔋 Battery Level Checker")
        self.root.geometry("625x625")
        self.root.configure(bg="#0a0a2a")
        self.root.resizable(False, False)

        # Heading
        tk.Label(
            root,
            text="Battery Level Checker",
            font=("Poppins", 18, "bold"),
            fg="#00FFCC",
            bg="#0a0a2a"
        ).pack(pady=15)

        # Battery info labels
        self.percent_label = tk.Label(
            root, text="Battery Level: --%", font=("Poppins", 14),
            fg="white", bg="#0a0a2a"
        )
        self.percent_label.pack(pady=10)

        self.status_label = tk.Label(
            root, text="Status: --", font=("Poppins", 14),
            fg="white", bg="#0a0a2a"
        )
        self.status_label.pack(pady=5)

        # Battery progress bar
        self.style = ttk.Style()
        self.style.configure(
            "TProgressbar",
            thickness=25,
            troughcolor="#1a1a40",
            background="#00FF99"
        )

        self.progress = ttk.Progressbar(
            root, orient="horizontal",
            length=300, mode="determinate",
            style="TProgressbar"
        )
        self.progress.pack(pady=20)

        self.alert_shown = False
        self.update_battery_info()

    def update_battery_info(self):
        battery = psutil.sensors_battery()

        if battery is None:
            self.percent_label.config(text="No Battery Detected")
            return

        percent = battery.percent
        plugged = battery.power_plugged

        # Update text
        self.percent_label.config(text=f"Battery Level: {percent}%")
        self.status_label.config(text=f"Status: {'Plugged In 🔌' if plugged else 'On Battery 🔋'}")

        # Update progress bar
        self.progress["value"] = percent

        # Color logic
        if percent < 20:
            color = "#FF4D4D"  # red
        elif percent < 70:
            color = "#FFD700"  # yellow
        else:
            color = "#00FF99"  # green

        self.style.configure("TProgressbar", background=color)

        # Popup notification if below 50%
        if percent < 70 and not self.alert_shown:
            notification.notify(
                title="⚠️ Battery Low Warning",
                message=f"Battery is at {percent}%. Please plug in your charger!",
                timeout=6
            )
            self.alert_shown = True
        elif percent >= 70:
            self.alert_shown = False

        # Refresh every 10 seconds
        self.root.after(10000, self.update_battery_info)


# -------------------- Run App --------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = BatteryApp(root)
    root.mainloop()
