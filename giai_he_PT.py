import numpy as np
import tkinter as tk
from tkinter import Entry, Label, Button, messagebox

# Khởi tạo cửa sổ Tkinter
root = tk.Tk()
root.title("Ứng dụng giải hệ phương trình tuyến tính")

# Khai báo biến toàn cục
variables_entry = Entry(root)
coeff_entries = []
constant_entries = []
solve_button = None
solution_label = None

def clear_entries():
    global variables_entry, solve_button
    # Xóa các phần tử GUI hiện tại
    variables_entry.pack_forget()
    for row in coeff_entries:
        for entry in row:
            entry.pack_forget()
    for entry in constant_entries:
        entry.pack_forget()
    solve_button.pack_forget()
    solution_label.pack_forget()

def solve_equation():
    try:
        # Lấy số biến (n)
        n = int(variables_entry.get())

        # Tạo ma trận A từ các giá trị nhập vào
        A = np.zeros((n, n))
        for i in range(n):
            for j in range(n):
                A[i][j] = float(coeff_entries[i][j].get())

        # Tạo vector cột B từ các giá trị nhập vào
        B = np.zeros((n, 1))
        for i in range(n):
            B[i] = float(constant_entries[i].get())

        # Giải hệ phương trình
        X = np.linalg.solve(A, B)

        # Hiển thị nghiệm trên giao diện
        solution_label.config(text="Nghiệm của hệ phương trình (X): " + ", ".join(map(str, X)))

    except ValueError as e:
        messagebox.showerror("Lỗi", "Giá trị nhập không hợp lệ. Vui lòng kiểm tra lại.")

def create_entries():
    global variables_entry, solve_button, solution_label

    # Xóa giao diện hiện tại (nếu có)
    clear_entries()

    # Tạo nhãn và ô nhập dữ liệu cho số biến
    variables_label = Label(root, text="Số biến (n):")
    variables_label.pack()
    variables_entry.pack()

    # Tạo ô nhập dữ liệu mới dựa trên số biến
    n = int(variables_entry.get())
    for i in range(n):
        row_entries = []
        for j in range(n):
            coeff_label = Label(root, text=f"Hệ số {i + 1}{j + 1}:")
            coeff_label.pack()
            coeff_entry = Entry(root)
            coeff_entry.pack()
            row_entries.append(coeff_entry)
        coeff_entries.append(row_entries)

    for i in range(n):
        const_label = Label(root, text=f"Hằng số {i + 1}:")
        const_label.pack()
        const_entry = Entry(root)
        const_entry.pack()
        constant_entries.append(const_entry)

    solve_button = Button(root, text="Giải", command=solve_equation)
    solve_button.pack()

    solution_label = Label(root, text="")
    solution_label.pack()

# Tạo nút "Tạo" và khởi chạy giao diện
create_button = Button(root, text="Tạo", command=create_entries)
create_button.pack()

root.mainloop()