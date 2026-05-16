from flask import Flask, request, render_template_string

app = Flask(__name__)

chat_history = []

HTML = """
<!DOCTYPE html>
<html>
<head>
<title>EduAssist AI</title>

<style>
body {
    font-family: Arial;
    background: #0b1220;
    color: white;
    text-align: center;
}

.container {
    width: 60%;
    margin: auto;
    margin-top: 40px;
}

.box {
    background: #1e293b;
    padding: 20px;
    border-radius: 15px;
}

input {
    width: 70%;
    padding: 12px;
    border-radius: 8px;
    border: none;
}

button {
    padding: 12px 18px;
    border-radius: 8px;
    border: none;
    background: #38bdf8;
    cursor: pointer;
}

.chat {
    margin-top: 20px;
    text-align: left;
    background: #111827;
    padding: 15px;
    border-radius: 10px;
    height: 300px;
    overflow-y: auto;
}

.user { color: #60a5fa; }
.bot { color: #34d399; }

.footer {
    position: fixed;
    bottom: 10px;
    width: 100%;
    font-size: 12px;
    color: gray;
}
</style>

</head>

<body>

<div class="container">

<h1>🎓 EduAssist AI (Final Version)</h1>

<div class="box">

<form action="/chat">
    <input name="msg" placeholder="Ask your question..." required>
    <button>Send</button>
</form>

<div class="chat">
{% for c in chat %}
<p class="user"><b>You:</b> {{c['user']}}</p>
<p class="bot"><b>Bot:</b> {{c['bot']}}</p>
<hr>
{% endfor %}
</div>

</div>
</div>

<div class="footer">
Made by CLGMATE TEAM | Hackathon Project 🚀
</div>

</body>
</html>
"""

def get_answer(msg):
    msg = msg.lower()

    if "exam" in msg:
        return "Focus on PYQs, revision and time management."
    elif "python" in msg:
        return "Python is used for AI, web apps and automation."
    elif "project" in msg:
        return "Build chatbot, portfolio or AI tools for hackathon."
    elif "hello" in msg:
        return "Hello! I am EduAssist AI 🤖"
    else:
        return "I can help with exams, coding and projects."

@app.route("/")
def home():
    return render_template_string(HTML, chat=chat_history)

@app.route("/chat")
def chat():
    msg = request.args.get("msg")
    reply = get_answer(msg)

    chat_history.append({"user": msg, "bot": reply})

    return render_template_string(HTML, cha
