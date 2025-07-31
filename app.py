from flask import Flask, render_template, request
from translator import translate_text

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    translated_text = ""
    if request.method == "POST":
        original_text = request.form["text"]
        target_lang = request.form["language"]
        translated_text = translate_text(original_text, target_lang)
    return render_template("index.html", translated_text=translated_text)

if __name__ == "__main__":
    app.run(debug=True)
