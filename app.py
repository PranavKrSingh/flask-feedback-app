from flask import Flask, render_template, redirect, url_for, flash, session
from forms import FeedbackForm
import csv
from datetime import datetime

app = Flask(__name__)
app.secret_key = "my-secret-key"

@app.route("/", methods=["GET", "POST"])
def feedback():
    form = FeedbackForm()
    if form.validate_on_submit():
        name = form.username.data
        email = form.email.data
        message = form.message.data

        # save to CSV
        with open("feedback.csv", "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now().isoformat(), name, email, message])

        # save to session
        session["user"] = name
        session["email"] = email
        session["message"] = message
        session["time"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        return redirect(url_for("thankyou"))

    return render_template("feedback.html", form=form)

@app.route("/thankyou")
def thankyou():
    user = session.get("user")
    email = session.get("email")
    message = session.get("message")
    time = session.get("time")

    if not user or not message:
        return redirect(url_for("feedback"))

    return render_template("thankyou.html", user=user, email=email, message=message, time=time)

@app.route("/submissions")
def submissions():
    entries = []
    try:
        with open("feedback.csv", newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                entries.append({
                    "time": row[0],
                    "user": row[1],
                    "email": row[2],
                    "message": row[3]
                })
    except FileNotFoundError:
        pass
    return render_template("submissions.html", entries=entries)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

if __name__ == "__main__":
    app.run(debug=True)
