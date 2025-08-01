import os
from flask import Flask, render_template, request, session
from translator import translate_text

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET_KEY", "your-secret-key")  # Needed for session

@app.route("/", methods=["GET", "POST"])
def index():
    translated_text = ""
    detected_lang = ""
    if "history" not in session:
        session["history"] = []

    if request.method == "POST":
        original_text = request.form["text"]
        target_lang = request.form["language"]
        translated_text, detected_lang = translate_text(original_text, target_lang)

        # Store latest translation in session history
        session["history"].insert(0, {
            "original": original_text,
            "translated": translated_text,
            "target": target_lang,
            "source": detected_lang
        })
        session["history"] = session["history"][:5]  # Keep only last 5

    return render_template("index.html", translated_text=translated_text, detected_lang=detected_lang, history=session["history"])
