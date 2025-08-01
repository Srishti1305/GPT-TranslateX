import os
from flask import Flask, render_template, request, session
from translator import translate_text
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "some-default-secret")

@app.route("/", methods=["GET", "POST"])
def index():
    translated_text = ""
    detected_lang = ""

    if "history" not in session:
        session["history"] = []

    if request.method == "POST":
        if request.form.get("action") == "clear":
            session["history"] = []
        else:
            original_text = request.form["text"]
            target_lang = request.form["language"]
            translated_text, detected_lang = translate_text(original_text, target_lang)

            session["history"].insert(0, {
                "text": original_text,
                "translated": translated_text,
                "source": detected_lang,
                "target": target_lang
            })

            session["history"] = session["history"][:5]

    return render_template("index.html",
                           translated_text=translated_text,
                           detected_lang=detected_lang,
                           history=session.get("history", []))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
