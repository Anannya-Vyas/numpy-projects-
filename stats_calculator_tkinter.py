import numpy as np
import tkinter as tk
from tkinter import ttk

# ---------------- LOGIC ---------------- #
def process_input(event=None):
    try:
        values = entry.get().split()
        count = len(values)

        progress["value"] = count
        counter_label.config(text=f"{count} / 20 numbers entered 💗")

        if count == 20:
            numbers = np.array(list(map(float, values)))

            mean_val = np.mean(numbers)
            median_val = np.median(numbers)
            min_val = np.min(numbers)
            std_val = np.std(numbers)

            result_label.config(
                text=(
                    f"🌸 Mean: {mean_val:.2f}\n"
                    f"🎀 Median: {median_val:.2f}\n"
                    f"🍓 Minimum: {min_val}\n"
                    f"✨ Std Deviation: {std_val:.2f}"
                ),
                fg="#b4005a"
            )

            entry.config(state="disabled", bg="#f5d0e6")

        elif count > 20:
            result_label.config(text="❌ Too many numbers!", fg="red")

    except ValueError:
        result_label.config(text="❌ Numbers only please!", fg="red")


# ---------------- WINDOW ---------------- #
root = tk.Tk()
root.title("Pretty NumPy Stats Calculator 💖")
root.geometry("560x420")
root.configure(bg="#fbe7f3")

# ---------------- SHADOW (3D EFFECT) ---------------- #
shadow = tk.Frame(root, bg="#e3a5c7")
shadow.place(relx=0.5, rely=0.5, anchor="center", width=500, height=340)

card = tk.Frame(root, bg="white")
card.place(relx=0.5, rely=0.5, anchor="center", width=480, height=320)

# ---------------- TITLE ---------------- #
title = tk.Label(
    card,
    text="🌈 NumPy Stats Calculator",
    font=("Segoe UI", 18, "bold"),
    bg="white",
    fg="#d63384"
)
title.pack(pady=(15, 5))

subtitle = tk.Label(
    card,
    text="Enter 20 numbers (space separated)",
    font=("Segoe UI", 10),
    bg="white",
    fg="#888888"
)
subtitle.pack()

# ---------------- ENTRY ---------------- #
entry = tk.Entry(
    card,
    font=("Segoe UI", 12),
    width=42,
    bd=2,
    relief="groove",
    bg="#fff0f7"
)
entry.pack(pady=12)
entry.bind("<KeyRelease>", process_input)

# ---------------- PROGRESS BAR ---------------- #
style = ttk.Style()
style.theme_use("clam")
style.configure(
    "pink.Horizontal.TProgressbar",
    troughcolor="#ffe1f0",
    background="#ff69b4",
    thickness=18
)

progress = ttk.Progressbar(
    card,
    style="pink.Horizontal.TProgressbar",
    maximum=20,
    length=320
)
progress.pack(pady=5)

counter_label = tk.Label(
    card,
    text="0 / 20 numbers entered 💗",
    font=("Segoe UI", 9),
    bg="white",
    fg="#aa4a77"
)
counter_label.pack()

# ---------------- RESULT ---------------- #
result_label = tk.Label(
    card,
    font=("Segoe UI", 11),
    bg="white",
    justify="center"
)
result_label.pack(pady=15)

root.mainloop()


# import numpy as np
# import tkinter as tk

# def process_input(event=None):
#     try:
#         values = entry.get().split()
#         count = len(values)

#         status_label.config(text=f"Numbers entered: {count}/20")

#         if count == 20:
#             numbers = np.array(list(map(float, values)))

#             mean_val = np.mean(numbers)
#             median_val = np.median(numbers)
#             min_val = np.min(numbers)
#             std_val = np.std(numbers)

#             result_label.config(
#                 text=(
#                     f"Mean: {mean_val:.2f}\n"
#                     f"Median: {median_val:.2f}\n"
#                     f"Minimum: {min_val}\n"
#                     f"Std Deviation: {std_val:.2f}"
#                 )
#             )

#             entry.config(state="disabled")

#         elif count > 20:
#             result_label.config(text="❌ Too many numbers! Enter only 20.")

#     except ValueError:
#         result_label.config(text="❌ Invalid input detected")

# # Window setup
# root = tk.Tk()
# root.title("NumPy Stats Calculator (Tkinter)")
# root.geometry("500x350")

# # UI elements
# tk.Label(
#     root,
#     text="Enter 20 numbers separated by spaces",
#     font=("Arial", 12)
# ).pack(pady=10)

# entry = tk.Entry(root, width=55)
# entry.pack(pady=5)
# entry.bind("<KeyRelease>", process_input)

# status_label = tk.Label(root, text="Numbers entered: 0/20")
# status_label.pack(pady=5)

# result_label = tk.Label(root, font=("Arial", 10), fg="blue")
# result_label.pack(pady=15)

# root.mainloop()
