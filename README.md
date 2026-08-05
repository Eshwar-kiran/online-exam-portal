# 🎓 Online Exam Portal

The Online Exam Portal is a lightweight web application designed to simplify the online examination process. It provides a secure authentication system, interactive exam interface, automatic evaluation, and instant result generation, making it suitable for educational institutions, coding assessments, and online quizzes.

## Tech Stack

The project was built using the following technologies:

- 🐍 **Python** – Core programming language
- 🌐 **Flask** – Lightweight Python web framework
- 🗄️ **SQLite** – Database for storing users and exam questions
- 🔐 **Werkzeug Security** – Password hashing and authentication
- 🎨 **HTML5** – Page structure
- 🎨 **CSS3** – Responsive UI and styling
- 🧩 **Jinja2** – Dynamic HTML templating
- 💾 **SQLAlchemy** – ORM for database operations

## Data Source

The application uses an **SQLite database (`exam.db`)**.

The database stores:

- User accounts
- Encrypted passwords
- Multiple-choice questions
- Correct answers

The current version includes predefined sample questions, but the system can easily be extended to support dynamic question management through an admin panel.

# Features / Highlights

## 📌 Business Problem

Traditional paper-based examinations require manual evaluation, are time-consuming, and provide delayed feedback.

Educational institutions require a secure, fast, and scalable platform where students can take exams remotely while receiving immediate results.

## 🎯 Goal of the Project

The objective of this project is to build a simple yet secure online examination platform that:

- Allows secure user authentication
- Conducts online multiple-choice examinations
- Evaluates responses automatically
- Displays instant results
- Provides a clean and user-friendly interface

## 🖥️ Walkthrough of the Application

### 🏠 Home Page

- Professional landing page
- Register/Login navigation
- Clean and responsive interface

### 👤 User Registration

- Create new user account
- Passwords securely hashed before storage
- Prevents duplicate usernames

### 🔐 Secure Login

- User authentication
- Password verification using hashing
- Session management after successful login
- Invalid credentials handled gracefully


### 📝 Online Examination

- Displays multiple-choice questions
- One answer per question
- Simple and distraction-free interface
- Submit answers with a single click


### 📊 Instant Result Evaluation

After submission, the system:

- Calculates score automatically
- Displays total marks
- Shows Pass/Fail status
- Encourages users with personalized feedback

### 🚪 Logout

- Securely ends user session
- Prevents unauthorized access after logout

# ✨ Key Features

- ✅ User Registration
- ✅ Secure Login System
- ✅ Password Hashing
- ✅ Session Management
- ✅ Online MCQ Examination
- ✅ Automatic Score Calculation
- ✅ Instant Result Generation
- ✅ Pass / Fail Evaluation
- ✅ Responsive User Interface
- ✅ SQLite Database Integration

# 📂 Project Structure

```
Online-Exam-Portal/
│
├── static/
│   └── (CSS, Images)
│
├── templates/
│   ├── index.html
│   ├── register.html
│   ├── login.html
│   ├── exam.html
│   └── result.html
│
├── instance/
│   └── exam.db
│
├── app.py
├── requirements.txt
├── README.md
```

# 🚀 Installation & Setup

Follow these steps to run the project on your local machine.

## 1. Clone the Repository

```bash
git clone https://github.com/yourusername/online-exam-portal.git
```

## 2. Open the Project Folder

```bash
cd online-exam-portal
```

## 3. (Optional but Recommended) Create a Virtual Environment

```bash
python -m venv .venv
```

## 4. Activate the Virtual Environment

### Windows

```bash
.venv\Scripts\activate
```

### macOS / Linux

```bash
source .venv/bin/activate
```

## 5. Install the Required Packages

```bash
pip install -r requirements.txt
```

## 6. Start the Application

```bash
python app.py
```

You should now see the **Online Exam Portal** homepage.


# 📸 Application Screenshots

- 🏠 Home Page
  
  ![home-page](https://github.com/Eshwar-kiran/online-exam-portal/blob/main/screenshots/snapshot_of_Homepage.png)
  
- 👤 Registration Page
  
  ![Registration-page](https://github.com/Eshwar-kiran/online-exam-portal/blob/main/screenshots/snapshot_of_Registration_page.png)
  
- 🔐 Login Page
  
  ![login-page](https://github.com/Eshwar-kiran/online-exam-portal/blob/main/screenshots/snapshot_of_Loginpage.png)
  
- 📝 Examination Page
  
  ![exam-1](https://github.com/Eshwar-kiran/online-exam-portal/blob/main/screenshots/snapshot_of_exampage-1.png)
  
  ![exam-2](https://github.com/Eshwar-kiran/online-exam-portal/blob/main/screenshots/snapshot_of_exampage-2.png)
  
- 📊 Result Page
  
  ![result-1](https://github.com/Eshwar-kiran/online-exam-portal/blob/main/screenshots/snapshot_of_Result-1.png)
  
  ![result-2](https://github.com/Eshwar-kiran/online-exam-portal/blob/main/screenshots/snapshot_of_Result-2.png)
  
# 💡 Learning Outcomes

Through this project, I gained hands-on experience with:

- Flask Web Development
- User Authentication
- Password Hashing
- Session Management
- SQLAlchemy ORM
- SQLite Database Design
- CRUD Operations
- HTML & CSS UI Design
- Jinja2 Templates
- Backend Development using Python

# 🔮 Future Enhancements

- 👨‍🏫 Admin Dashboard
- 📚 Multiple Subjects
- ⏳ Exam Timer
- 📈 Performance Analytics
- 📊 Student Progress Reports
- 📧 Email Notifications
- ☁️ MySQL/PostgreSQL Support
- 📱 Mobile Responsive UI
- 🎯 Randomized Questions
- 📄 Downloadable Score Reports (PDF)


# 📬 Contact

If you have any suggestions or feedback, feel free to connect with me.

⭐ **If you found this project useful, consider giving it a Star!**
