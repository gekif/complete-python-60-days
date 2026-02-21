from datetime import datetime
from flask import Flask, render_template, request, flash, redirect, url_for, current_app
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
from config import Config


# ------------------------
# App Initialization
# ------------------------

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
mail = Mail(app)


# ------------------------
# Database Model
# ------------------------

class Form(db.Model):
    __tablename__ = "forms"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), nullable=False)
    date = db.Column(db.Date, nullable=False)
    occupation = db.Column(db.String(80), nullable=False)


# ------------------------
# Helper Functions
# ------------------------

def save_form(data: dict) -> None:
    """Save form data to database."""
    form = Form(**data)
    db.session.add(form)
    db.session.commit()


def send_confirmation_email(email: str, first_name: str, last_name: str, date: str) -> None:
    """Send confirmation email to user."""
    message_body = (
        f"Thank you for your submission, {first_name}.\n\n"
        f"Here are your data:\n"
        f"First Name: {first_name}\n"
        f"Last Name: {last_name}\n"
        f"Availability: {date}\n\n"
        f"Thank you!"
    )

    message = Message(
        subject="New Form Submission",
        sender=current_app.config["MAIL_USERNAME"],
        recipients=[email],
        body=message_body
    )

    try:
        mail.send(message)
    except Exception as e:
        current_app.logger.error(f"Email failed: {e}")


# ------------------------
# Routes
# ------------------------

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":

        form_data = {
            "first_name": request.form.get("first_name"),
            "last_name": request.form.get("last_name"),
            "email": request.form.get("email"),
            "date": datetime.strptime(request.form.get("date"), "%Y-%m-%d"),
            "occupation": request.form.get("occupation"),
        }

        save_form(form_data)

        send_confirmation_email(
            email=form_data["email"],
            first_name=form_data["first_name"],
            last_name=form_data["last_name"],
            date=request.form.get("date")
        )

        flash(
            f"{form_data['first_name']}, your form has been submitted successfully!",
            "success"
        )

        return redirect(url_for("index"))

    return render_template("index.html")


# ------------------------
# Run App
# ------------------------

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=5001)