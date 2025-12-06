from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Simple function to give supportive feedback
def analyze_mood(user_message):
    user_message = user_message.lower()
    
    if "happy" in user_message or "good" in user_message or "great" in user_message:
        return "That's wonderful to hear! Keep spreading the positivity! 😊"
    elif "sad" in user_message or "down" in user_message or "unhappy" in user_message:
        return "I'm here for you. Remember, it's okay to feel sad sometimes. 💛"
    elif "stressed" in user_message or "anxious" in user_message or "worried" in user_message:
        return "Take a deep breath. Everything will be okay. You’ve got this! 🌿"
    elif "tired" in user_message or "exhausted" in user_message:
        return "Make sure to rest and take care of yourself. You deserve it! 💤"
    else:
        return "Thank you for sharing! Remember, every emotion is valid. 🌟"

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/page1", methods=["GET", "POST"])
def page1():
    ai_response = None
    if request.method == "POST":
        user_message = request.form.get("user_message")
        if user_message:
            ai_response = analyze_mood(user_message)
    return render_template("page1.html", ai_response=ai_response)

@app.route("/page2")
def page2():
    return render_template("page2.html")

if __name__ == "__main__":
    app.run(debug=True)
    