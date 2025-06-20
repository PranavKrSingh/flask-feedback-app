
# 📝 Flask Feedback App

A simple and elegant web application built using **Flask** and **Flask-WTF** to collect, store, and display user feedback. It demonstrates core web development concepts including form handling, server-side validation, session management, file I/O, and template rendering.

---

## 🚀 Live Demo

> _Currently not deployed. To test locally, follow the instructions below._

---

## 📂 Project Structure

```

flask-feedback-app/
│
├── app.py                     # Main Flask application logic
├── forms.py                   # WTForms class for form validation
├── requirements.txt           # Python package dependencies
├── feedback.csv               # Auto-created to store submitted feedback
│
├── templates/                 # HTML templates (Jinja2)
│   ├── base.html              # Layout template (header/footer)
│   ├── feedback.html          # Main feedback form page
│   ├── thankyou.html          # Confirmation page after submission
│   ├── submissions.html       # Table view of all submissions
│   └── 404.html               # Custom 404 error page
│
├── static/
│   └── css/
│       └── style.css          # Custom styling

````

---

## 🧠 Features

✅ Feedback form with:
- Name, Email, Message fields  
- Validation using **Flask-WTF**  
- Bootstrap UI for styling

✅ Saves feedback to a CSV file  
✅ Displays thank-you page with timestamp  
✅ `/submissions` route shows all stored feedback  
✅ Custom 404 error page  
✅ Clean, modular, and extensible code  

---

## 📸 Screenshots

<details>
<summary>🖼 Click to expand</summary>

- **Feedback Form**
  ![form](https://via.placeholder.com/600x300?text=Feedback+Form+UI)

- **Thank You Page**
  ![thankyou](https://via.placeholder.com/600x300?text=Thank+You+Page)

- **Submissions Table**
  ![table](https://via.placeholder.com/600x300?text=Submissions+Page)

</details>

---

## ⚙️ Installation

1. **Clone the repository**  
```bash
git clone https://github.com/PranavKrSingh/flask-feedback-app.git
cd flask-feedback-app
````

2. **Create virtual environment (optional but recommended)**

```bash
python -m venv venv
source venv/bin/activate   # For Linux/Mac
venv\Scripts\activate      # For Windows
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Run the application**

```bash
python app.py
```

5. **Visit in your browser**
   [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 📦 Dependencies

* [Flask](https://palletsprojects.com/p/flask/)
* [Flask-WTF](https://flask-wtf.readthedocs.io/)
* [email-validator](https://pypi.org/project/email-validator/)

Install via:

```bash
pip install flask flask-wtf email-validator
```

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙋‍♂️ Author

**Pranav Kumar Singh**
📧 [LinkedIn](https://www.linkedin.com/in/pranavkumarsingh32/)
🌐 [GitHub](https://github.com/PranavKrSingh)

---

## 💡 Future Enhancements

* Store data in SQLite or MySQL instead of CSV
* Email confirmation to admin
* Deployment on platforms like Render or Heroku
* Export CSV file from the submissions page

---

## 💬 Feedback

If you find this project helpful, feel free to give it a ⭐ on GitHub!
Pull requests and suggestions are welcome.

