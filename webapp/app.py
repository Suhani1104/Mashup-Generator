from flask import Flask, render_template, request
from mashup_core import create_mashup, MashupError
import zipfile
import os
import re
import smtplib
from email.message import EmailMessage

app = Flask(__name__)

def valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        singer = request.form["singer"]
        n = request.form["videos"]
        duration = request.form["duration"]
        email = request.form["email"]

        if not valid_email(email):
            return render_template("index.html", error="Invalid Email ID")

        try:
            n = int(n)
            duration = int(duration)

            if n <= 10:
                return render_template("index.html", error="Number of videos must be > 10")

            if duration <= 20:
                return render_template("index.html", error="Duration must be > 20 sec")

            output_file = "mashup.mp3"
            create_mashup(singer, n, duration, output_file)

            zip_name = "mashup.zip"
            with zipfile.ZipFile(zip_name, "w") as zipf:
                zipf.write(output_file)

            send_email(email, zip_name)

            return render_template("index.html", success="Mashup sent to email!")

        except MashupError as e:
            return render_template("index.html", error=str(e))

        except Exception as e:
            return render_template("index.html", error=f"Unexpected Error {e}")

    return render_template("index.html")

def send_email(to_email, file_path):
    sender = os.environ.get("EMAIL_USER")
    password = os.environ.get("EMAIL_PASS")

    msg = EmailMessage()
    msg["Subject"] = "Your Mashup"
    msg["From"] = sender
    msg["To"] = to_email
    msg.set_content("Your mashup is attached.")

    with open(file_path, "rb") as f:
        msg.add_attachment(f.read(), maintype="application", subtype="zip", filename="mashup.zip")

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender, password)
        server.send_message(msg)

if __name__ == "__main__":
    app.run()
