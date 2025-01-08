# 📝 To Do List Website
A "To Do List" web application built using HTML, CSS, Python, and Django Framework. This project enables users to efficiently manage their daily tasks, providing features like creating tasks, editing tasks, marking tasks as done, and reviewing or deleting tasks from the history.

# 🌟 Features
-  User Authentication:
Register, login, and logout functionality.
-  Create Tasks:
Users can create a list of tasks with descriptions.
-  Edit Tasks:
Modify task details as needed.
-  Mark as Done:
Mark tasks as completed after completion.
-  Task History:
View completed tasks and delete them if necessary.
-  Search Tasks:
Easily search for tasks using keywords.

# 💻 Tech Stack
**Frontend** <br>
-  **HTML5:** Structure and layout of web pages.
-  **CSS3:** Design and styling for a visually appealing interface.

**Backend**<br>
-  **Python:** Backend logic and functionality.
-  **Django Framework:** For dynamic web application development.

**Database**<br>
-  **SQLite (default Django database):** Used for storing tasks, user information, and history.

# 📂 Project Structure

├── todo_list/             # Main Django project folder.  <br>
│   ├── settings.py        # Project settings.  <br>
│   ├── urls.py            # URL configuration.  <br>
│   └── wsgi.py            # WSGI entry point.  <br>
├── app/                   # App folder for managing tasks.  <br>
│   ├── migrations/        # Database migrations.  <br>
│   ├── templates/         # HTML files for views.  <br>
│   ├── static/            # CSS and other static files.<br>  
│   ├── models.py          # Database models.  <br>
│   ├── views.py           # Logic for routes and user actions.  <br>
│   └── urls.py            # App-specific URL routing.  <br>
└── manage.py              # Django management script.  <br>

# 🚀 How It Works
-  **Login (log_in):** Authenticates users to access their task lists.
-  **Register (register):** Allows users to create new accounts.
-  **Task Index (index):** Displays all active tasks for the logged-in user.
-  **Create Task (create):** Enables users to add new tasks with descriptions.
-  **Edit Task (edit):** Facilitates updating existing task details.
-  **Mark as Done (display):** Moves completed tasks to the history table.
-  **History (history):** Shows completed tasks and provides delete functionality.

# 🛠 Future Enhancements
-  **Notification System:** Remind users about pending tasks.
-  **Priority Levels:** Assign priorities (e.g., High, Medium, Low) to tasks.
-  **Deadline Management:** Allow setting deadlines and send alerts.
-  **Mobile-Friendly Design:** Optimize layout for better usability on mobile devices.


# UI VIEW

![Screenshot 2024-12-17 101326](https://github.com/user-attachments/assets/bd3d02a0-1b60-445b-b708-bfa529feac3e)
![Screenshot 2024-12-17 101348](https://github.com/user-attachments/assets/c9dcc372-56cc-4390-8df1-4dc3ee8b33e2)
![Screenshot 2024-12-17 101405](https://github.com/user-attachments/assets/91e92246-f452-40ff-b3a6-1dffb4719a59)
![Screenshot 2024-12-17 101424](https://github.com/user-attachments/assets/d837b9f0-ef97-402c-8e4d-c54874330424)
![Screenshot 2024-12-17 101454](https://github.com/user-attachments/assets/ea4554a7-99ff-4051-8f71-93c492b22955)
![Screenshot 2024-12-17 101513](https://github.com/user-attachments/assets/e3bd090a-3704-4fa1-95dd-9e9a9ad1fc49)
