import tkinter as tk
from tkinter import messagebox, ttk
import json
import os
import csv
import datetime

CONTACT_FILE = "contacts.json"
USER_FILE = "users.json"

# ---------- FILE SETUP ----------
for file in [CONTACT_FILE, USER_FILE]:
    if not os.path.exists(file):
        with open(file, "w") as f:
            json.dump({}, f)

def load_data(file):
    try:
        with open(file, "r") as f:
            return json.load(f)
    except:
        return {}

def save_data(file, data):
    with open(file, "w") as f:
        json.dump(data, f, indent=4)

users = load_data(USER_FILE)
contacts = load_data(CONTACT_FILE)
current_user = None

# ================= LOGIN =================
def login():
    global current_user, contacts

    u = entry_user.get()
    p = entry_pass.get()

    if u in users and users[u] == p:
        current_user = u
        contacts = load_data(f"{u}_contacts.json")
        login_window.destroy()
        open_main_app()
    else:
        messagebox.showerror("Error", "Invalid login!")

def register():
    u = entry_user.get()
    p = entry_pass.get()

    if u in users:
        messagebox.showerror("Error", "User already exists!")
        return

    users[u] = p
    save_data(USER_FILE, users)

    save_data(f"{u}_contacts.json", {})
    messagebox.showinfo("Success", "User Registered!")

# ================= MAIN APP =================
def open_main_app():

    def save_contacts():
        save_data(f"{current_user}_contacts.json", contacts)

    def refresh_list(data=None):
        tree.delete(*tree.get_children())
        data = data if data else contacts
        for name, c in data.items():
            tree.insert("", tk.END, values=(name, c["age"], c["mobile"], c["email"]))

    def clear_fields():
        entry_name.delete(0, tk.END)
        entry_age.delete(0, tk.END)
        entry_email.delete(0, tk.END)
        entry_mobile.delete(0, tk.END)

    def add_contact():
        name = entry_name.get().strip()
        age = entry_age.get().strip()
        email = entry_email.get().strip()
        mobile = entry_mobile.get().strip()

        if not name:
            return messagebox.showerror("Error", "Name required")

        if name in contacts:
            return messagebox.showwarning("Warning", "Duplicate contact!")

        if not mobile.isdigit() or len(mobile) != 10:
            return messagebox.showerror("Error", "Invalid mobile!")

        if "@" not in email:
            return messagebox.showerror("Error", "Invalid email!")

        contacts[name] = {
            "age": age,
            "email": email,
            "mobile": mobile,
            "created": str(datetime.datetime.now())
        }

        save_contacts()
        refresh_list()
        clear_fields()

    def delete_contact():
        selected = tree.focus()
        if not selected:
            return

        confirm = messagebox.askyesno("Confirm", "Delete contact?")
        if not confirm:
            return

        name = tree.item(selected)["values"][0]
        del contacts[name]

        save_contacts()
        refresh_list()

    def update_contact():
        selected = tree.focus()
        if not selected:
            return

        old_name = tree.item(selected)["values"][0]

        name = entry_name.get()
        age = entry_age.get()
        email = entry_email.get()
        mobile = entry_mobile.get()

        if not mobile.isdigit() or len(mobile) != 10:
            return messagebox.showerror("Error", "Invalid mobile!")

        contacts.pop(old_name)
        contacts[name] = {
            "age": age,
            "email": email,
            "mobile": mobile
        }

        save_contacts()
        refresh_list()
        clear_fields()

    def search_contact():
        q = entry_search.get().lower()

        filtered = {
            n: c for n, c in contacts.items()
            if q in n.lower() or
               q in c["mobile"] or
               q in c["email"].lower()
        }

        refresh_list(filtered)

    def export_contacts():
        with open("contacts.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Name", "Age", "Mobile", "Email"])
            for n, c in contacts.items():
                writer.writerow([n, c["age"], c["mobile"], c["email"]])

        messagebox.showinfo("Success", "Exported!")

    def import_contacts():
        try:
            with open("contacts.csv", "r") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    contacts[row["Name"]] = {
                        "age": row["Age"],
                        "mobile": row["Mobile"],
                        "email": row["Email"]
                    }
            save_contacts()
            refresh_list()
        except:
            messagebox.showerror("Error", "Import failed")

    def count_contacts():
        total = len(contacts)
        with_email = sum(1 for c in contacts.values() if c["email"])
        messagebox.showinfo("Stats",
                            f"Total: {total}\nWith Email: {with_email}")

  # (Only corrected part shown — rest same)
    def count_contacts():
        total = len(contacts)
        with_email = sum(1 for c in contacts.values() if c["email"])
        messagebox.showinfo("Stats",
                            f"Total: {total}\nWith Email: {with_email}")

    # ✅ FIXED INDENTATION
    def fill_fields(event):
        selected = tree.focus()

        if not selected:
            return

        values = tree.item(selected, "values")

        if not values or len(values) < 4:
            return

        clear_fields()
        entry_name.insert(0, values[0])
        entry_age.insert(0, values[1])
        entry_mobile.insert(0, values[2])
        entry_email.insert(0, values[3])

    # ---------- UI SAME ----------
    main = tk.Tk()
    main.title("Contact Book Pro")
    main.geometry("900x550")
    main.configure(bg="#f4f6f8")

    left_frame = tk.Frame(main, bg="#2c3e50", width=300)
    left_frame.pack(side=tk.LEFT, fill=tk.Y)

    tk.Label(left_frame, text="Contact Book", bg="#2c3e50",
             fg="white", font=("Arial", 16, "bold")).pack(pady=20)

    def label(text):
        return tk.Label(left_frame, text=text, bg="#2c3e50", fg="white")

    label("Name").pack(anchor="w", padx=20)
    entry_name = tk.Entry(left_frame)
    entry_name.pack(fill="x", padx=20)

    label("Age").pack(anchor="w", padx=20)
    entry_age = tk.Entry(left_frame)
    entry_age.pack(fill="x", padx=20)

    label("Email").pack(anchor="w", padx=20)
    entry_email = tk.Entry(left_frame)
    entry_email.pack(fill="x", padx=20)

    label("Mobile").pack(anchor="w", padx=20)
    entry_mobile = tk.Entry(left_frame)
    entry_mobile.pack(fill="x", padx=20)

    tk.Button(left_frame, text="➕ Create", command=add_contact,
              bg="#27ae60", fg="white").pack(fill="x", padx=20, pady=5)

    tk.Button(left_frame, text="✏ Update", command=update_contact,
              bg="#2980b9", fg="white").pack(fill="x", padx=20, pady=5)

    tk.Button(left_frame, text="🗑 Delete", command=delete_contact,
              bg="#c0392b", fg="white").pack(fill="x", padx=20, pady=5)

    tk.Button(left_frame, text="📊 Count", command=count_contacts,
              bg="#8e44ad", fg="white").pack(fill="x", padx=20, pady=5)

    tk.Button(left_frame, text="📤 Export", command=export_contacts,
              bg="#16a085", fg="white").pack(fill="x", padx=20, pady=5)

    tk.Button(left_frame, text="📥 Import", command=import_contacts,
              bg="#d35400", fg="white").pack(fill="x", padx=20, pady=5)

    tk.Button(left_frame, text="🚪 Exit", command=main.destroy,
              bg="#7f8c8d", fg="white").pack(fill="x", padx=20, pady=10)

    right_frame = tk.Frame(main, bg="#ecf0f1")
    right_frame.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)

    search_frame = tk.Frame(right_frame, bg="#ecf0f1")
    search_frame.pack(pady=10)

    entry_search = tk.Entry(search_frame, width=30)
    entry_search.pack(side=tk.LEFT, padx=5)
    entry_search.bind("<KeyRelease>", lambda e: search_contact())

    tk.Button(search_frame, text="Search", command=search_contact,
              bg="#3498db", fg="white").pack(side=tk.LEFT)

    tk.Button(search_frame, text="Show All",
              command=lambda: refresh_list(),
              bg="#95a5a6", fg="white").pack(side=tk.LEFT)

    columns = ("Name", "Age", "Mobile", "Email")
    tree = ttk.Treeview(right_frame, columns=columns, show="headings")

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=150)

    tree.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)
    tree.bind("<<TreeviewSelect>>", fill_fields)

    refresh_list()
    main.mainloop()

# ================= LOGIN UI =================
login_window = tk.Tk()
login_window.title("Login")
login_window.geometry("300x220")

tk.Label(login_window, text="Username").pack(pady=5)
entry_user = tk.Entry(login_window)
entry_user.pack()

tk.Label(login_window, text="Password").pack(pady=5)
entry_pass = tk.Entry(login_window, show="*")
entry_pass.pack()

tk.Button(login_window, text="Login", command=login,
          bg="green", fg="white").pack(pady=10)

tk.Button(login_window, text="Register", command=register,
          bg="blue", fg="white").pack()

login_window.mainloop()