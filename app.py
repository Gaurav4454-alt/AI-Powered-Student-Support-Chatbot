from flask import Flask, request, render_template_string
import wikipedia

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
    height: 350px;
    overflow-y: auto;
}

.user {
    color: #60a5fa;
}

.bot {
    color: #34d399;
}
</style>

</head>

<body>

<div class="container">

<h1>🎓 EduAssist AI</h1>

<div class="box">

<form action="/chat">
    <input name="msg" placeholder="Ask anything..." required>
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

<div style="position:fixed; bottom:10px; width:100%; text-align:center; font-size:12px; color:#9ca3af;">
© 2026 CLGMATE TEAM | EduAssist AI Project 🚀
</div>

</body>
</html>
"""

def get_answer(msg):
    try:
        answer = wikipedia.summary(msg, sentences=2)
        return answer
    except:
        return "Sorry, I could not find information about that."

@app.route("/")
def home():
    return render_template_string(HTML, chat=chat_history)

@app.route("/chat")
def chat():
    msg = request.args.get("msg")

    reply = get_answer(msg)

    chat_history.append({
        "user": msg,
        "bot": reply
    })

    return render_template_string(HTML, chat=chat_history)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
