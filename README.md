📒 Contact Book Pro (Python Tkinter App)
A real-world desktop contact management system built using Python and Tkinter.
Designed to simulate a mini CRM system with authentication, contact handling, and data persistence.

🧩 1. What This Project Does

This application is divided into three main layers:

🔐 Authentication System
User Registration
Secure Login
Separate data storage per user
📇 Contact Management System
Add new contacts
Update existing contacts
Delete contacts safely
Prevent duplicate entries
⚙️ Utility & Data Features
Real-time search filtering 🔍
CSV Import & Export 📂
Contact statistics (Total / Valid emails) 📊
Persistent JSON-based storage

👉 Think of it as a lightweight personal CRM system

⚠️ 2. Problems Faced During Development

While building this project, I faced several real-world challenges:

🔴 Data Handling Issues
Contacts not saving correctly per user
JSON file structure confusion
🔴 UI & Tkinter Problems
Treeview selection not updating input fields
Layout alignment issues in sidebar design
🔴 Logic & Validation Bugs
Duplicate contacts being created
Invalid email and mobile numbers slipping through
CSV import/export mismatches



🛠 3. How I Solved Them
🟢 Data Isolation Fix
Separated contacts per user using dynamic JSON files
Improved file handling logic
🟢 UI Fixes
Used proper event binding (TreeviewSelect)
Refined layout structure for better UX
🟢 Validation Improvements
Added strict checks for email & mobile
Prevented duplicate entries using key-based validation
🟢 Error Handling
Used try/except blocks for file operations
Improved stability during import/export


🚀 Tech Stack
Python 🐍
Tkinter (GUI) 🎨
JSON (Data Storage)
CSV (Import/Export)

📈 Key Learning Outcomes
Building real-world Python desktop apps
Handling file-based databases
GUI development with Tkinter
Debugging complex logical issues
Improving user experience design


🚧 Future Improvements
SQLite database integration 🗄
Password encryption 🔐
Modern UI (CustomTkinter upgrade)
Cloud sync feature ☁️
Mobile-friendly version 📱


This project helped me move from writing basic Python scripts to building structured, real-world applications.



Author!
Saachin Kunwar







