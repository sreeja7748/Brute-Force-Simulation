# 🔐 Brute Force Attack Simulation

A Flask-based web application that demonstrates how a **brute force attack** works on a login system. This project is built for educational and cybersecurity learning purposes, helping users understand authentication mechanisms, brute-force vulnerabilities, and the importance of secure login practices.

> ⚠️ **Disclaimer:** This project is intended solely for educational and ethical cybersecurity training. Do not use it against systems without explicit authorization.

---


## 📌 Features

- 👤 User Registration
- 🔑 User Login System
- 🛡️ Admin Login
- 📊 Admin Dashboard
- ⚡ Real-time login validation
- 🚪 Logout functionality
- 🎨 Responsive web interface using HTML, CSS, and Flask templates

---


## 🛠️ Technologies Used

- Python 3
- Flask
- HTML5
- CSS3
- Jinja2 Templates

---


## 📂 Project Structure

```
Brute_Force/
│
├── app.py
├── templates/
│   ├── products.html
│   ├── login.html
│   ├── login_success.html
│   └── dashboard.html
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
├── username.txt
└── README.md
```

---


## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/Brute_Force.git
cd Brute_Force
```

### 2. Create a virtual environment (Optional)

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux / macOS**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install flask
```

or

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python app.py
```

The application will start at:

```
http://127.0.0.1:5002
```

---

## 🔑 Default Admin Credentials

```
Username: admin
Password: adminpassword
```

*(These credentials are hardcoded for demonstration purposes.)*

---

## 📖 How It Works

1. Register a new user.
2. Login using your registered credentials.
3. Login as the administrator using the default admin account.
4. Explore the dashboard and observe how authentication is handled.
5. Understand how weak authentication systems can become vulnerable to brute-force attacks.

---


## 🎯 Learning Objectives

This project demonstrates:

- User authentication
- Session flow
- Flask routing
- Form handling
- Login validation
- Brute force attack concepts
- Secure coding awareness

---

## 🔒 Future Improvements

- Password hashing using bcrypt
- Database integration (SQLite/MySQL)
- Account lockout after multiple failed attempts
- Rate limiting
- CAPTCHA
- Logging of failed login attempts
- Two-Factor Authentication (2FA)
- Password strength validation

---

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a feature branch

```bash
git checkout -b feature-name
```

3. Commit your changes

```bash
git commit -m "Added new feature"
```

4. Push to your branch

```bash
git push origin feature-name
```

5. Open a Pull Request

---

## 📜 License

This project is intended for educational purposes. Feel free to modify and improve it for learning.

---
