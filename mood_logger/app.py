from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Simple storage for moods (in-memory)
mood_entries = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        mood = request.form.get("mood")
        journal = request.form.get("journal")
        if mood and journal:
            mood_entries.append({"mood": mood, "journal": journal})
        return redirect(url_for("index"))
    return render_template("index.html", mood_entries=mood_entries)

@app.route("/page1")
def page1():
    return render_template("page1.html", mood_entries=mood_entries)

@app.route("/page2")
def page2():
    return render_template("page2.html", mood_entries=mood_entries)

# Only one main block!
if __name__ == "__main__":
    app.run(debug=True)
