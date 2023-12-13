import os
import random
import tkinter as tk
from tkinter import messagebox, filedialog
import pyperclip


def generate_username(name):
    first_name_initial = name.split()[0][0].upper()
    last_name = name.split()[1].lower()
    username = first_name_initial + last_name
    return username


def generate_password(length=13):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def get_next_user_number(file_path):
    # Визначити номер наступного користувача
    user_number = 1
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            lines = file.readlines()
            user_number = len(lines) // 5 + 1  # Кожен користувач займає 5 рядків

    return user_number


def on_generate_button_click():
    name_input = entry_name.get()
    email_input = entry_email.get()
    password_length = 10
    username_result = generate_username(name_input)
    password_result = generate_password(password_length)

    user_number = get_next_user_number(file_path)

    result_text = f"First name/Last name: {name_input}\n" \
                  f"Email: {email_input}\n" \
                  f"Username: {username_result}\n" \
                  f"Password: {password_result}\n\n"

    # Додати номер користувача до файлу
    result_text = f"User_{user_number}\n" + result_text

    result_text_widget.config(state=tk.NORMAL)
    result_text_widget.delete("1.0", tk.END)  # Очистка текстового віджета
    result_text_widget.insert(tk.END, result_text)
    result_text_widget.config(state=tk.DISABLED)

    # Перевірка та створення каталогу, якщо його немає
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Зберегти результати у файл на робочому столі
    with open(file_path, "a") as file:
        file.write(result_text)

    messagebox.showinfo("Файл збережено", f"Результати додано у файл {file_path}")

    # Копіювати результати у буфер обміну
    pyperclip.copy(result_text)


# Створення вікна Tkinter
window = tk.Tk()
window.title("UserGen")

# Створення та розміщення елементів у вікні
label_name = tk.Label(window, text="Enter First name/Last Name:")
label_name.pack(pady=10)

entry_name = tk.Entry(window)
entry_name.pack(pady=10)

label_email = tk.Label(window, text="Enter email:")
label_email.pack(pady=10)

entry_email = tk.Entry(window)
entry_email.pack(pady=10)

file_path = os.path.join(os.path.expanduser("~"), "Desktop", "generated_data.txt")

generate_button = tk.Button(window, text="Generate", command=on_generate_button_click)
generate_button.pack(pady=10)

result_text_widget = tk.Text(window, height=8, width=60, wrap=tk.WORD, state=tk.DISABLED)
result_text_widget.pack(pady=10)

# Запуск головного циклу Tkinter
window.mainloop()
