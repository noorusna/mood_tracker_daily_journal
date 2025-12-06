from flask import Flask, render_template, request
from collections import Counter
from datetime import datetime, timedelta

app = Flask(__name__)

# In-memory storage for mood entries
# Each entry is a dict: {"mood": "happy", "date": datetime}
mood_entries = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        mood = request.form.get("mood")
        if mood:
            mood_entries.append({"mood": mood.lower(), "date": datetime.now()})
    
    # Filter moods from last 7 days
    one_week_ago = datetime.now() - timedelta(days=7)
    last_week_entries = [e for e in mood_entries if e["date"] >= one_week_ago]

    # Count frequency of each mood
    mood_counts = Counter(e["mood"] for e in last_week_entries)

    # Determine most frequent mood
    most_frequent = mood_counts.most_common(1)[0][0] if mood_counts else None

    return render_template(
        "index.html",
        mood_counts=mood_counts,
        most_frequent=most_frequent
    )

@app.route("/page1")
def page1():
    return render_template("page1.html", mood_entries=mood_entries)

@app.route("/page2")
def page2():
    return render_template("page2.html", mood_entries=mood_entries)

if __name__ == "__main__":
    app.run(debug=True)

