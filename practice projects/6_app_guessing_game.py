import tkinter as tk
import random

# Create window
root = tk.Tk()
root.title("Number Guessing Game 🎯")
root.geometry("350x250")

number_computer_guess = random.randint(1, 10)

label_result = tk.Label(root, text="Choose a number from 1 to 10", font=("Arial", 12))
label_result.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=5)

output = tk.Label(root, text="", font=("Arial", 12))
output.pack(pady=10)

def check_guess():
    global number_computer_guess
    try:
        number_we_guess = int(entry.get())
        if number_we_guess < 1 or number_we_guess > 10:
            output.config(text="Number must be between 1 and 10 ❗")
        elif number_we_guess == number_computer_guess:
            output.config(text=f"✅ You guessed right!\nComputer: {number_computer_guess}")
        else:
            output.config(text=f"❌ Wrong guess!\nComputer: {number_computer_guess}")
            number_computer_guess = random.randint(1, 10)  # Next round
    except:
        output.config(text="Please enter a valid number 🔢")

btn = tk.Button(root, text="Guess", command=check_guess, font=("Arial", 12))
btn.pack(pady=10)

root.mainloop()
