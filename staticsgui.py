import tkinter as tk
import statistics

# function
def calculate():
    try:
        data = entry.get()
        nums = list(map(float, data.split(",")))

        mean_val = statistics.mean(nums)
        median_val = statistics.median(nums)
        mode_val = statistics.mode(nums)

        result_label.config(
            text=f"Mean: {mean_val}\nMedian: {median_val}\nMode: {mode_val}"
        )

    except:
        result_label.config(text="Enter valid numbers (comma separated)")

# GUI
window = tk.Tk()
window.title("Statistics Calculator")
window.geometry("400x300")

title = tk.Label(window, text="Statistics Calculator", font=("Arial", 14))
title.pack(pady=10)

label = tk.Label(window, text="Enter numbers (comma separated):")
label.pack()

entry = tk.Entry(window, width=40)
entry.pack(pady=10)

btn = tk.Button(window, text="Calculate", command=calculate)
btn.pack(pady=10)

result_label = tk.Label(window, text="")
result_label.pack(pady=10)

window.mainloop()
