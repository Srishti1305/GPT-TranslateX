import os
from flask import Flask, render_template, request
from translator import translate_text

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    translated_text = ""
    detected_lang = ""
    if request.method == "POST":
        original_text = request.form["text"]
        target_lang = request.form["language"]
        translated_text, detected_lang = translate_text(original_text, target_lang)
    return render_template("index.html", translated_text=translated_text, detected_lang=detected_lang)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
