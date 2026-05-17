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
    margin-top: 10px;
}

.clear-btn {
    background: red;
    color: white;
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
    <button type="submit">Send</button>
</form>

<form action="/clear">
    <button type="submit" class="clear-btn">
        Clear Chat
    </button>
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

def smart_reply(msg):

    msg_lower = msg.lower()

    # Creator Questions
    if (
        "who created you" in msg_lower
        or "whose create you" in msg_lower
        or "who developed you" in msg_lower
        or "who develop you" in msg_lower
    ):
        return "I am an AI assistant developed by the Gaurav and Tambyass Team."

    # Smart manual answers
    elif "c++" in msg_lower:
        return "C++ is a powerful programming language used for software, games and system programming."

    elif "software developer" in msg_lower or "developer" in msg_lower:
        return "A software developer creates websites, applications and software using programming languages."

    elif "python" in msg_lower:
        return "Python is a popular programming language used for AI, automation and web development."

    elif "ai" in msg_lower:
        return "Artificial Intelligence enables machines to think and learn like humans."

    elif "machine learning" in msg_lower:
        return "Machine Learning is a branch of AI where systems learn from data."

    elif "hello" in msg_lower or "hi" in msg_lower:
        return "Hello! I am EduAssist AI 🤖"

    # Wikipedia fallback
    try:
        return wikipedia.summary(msg, sentences=2)

    except:
        return "Sorry, I could not understand your question properly."

@app.route("/")
def home():
    return render_template_string(HTML, chat=chat_history)

@app.route("/chat")
def chat():

    msg = request.args.get("msg")

    reply = smart_reply(msg)

    chat_history.append({
        "user": msg,
        "bot": reply
    })

    return render_template_string(HTML, chat=chat_history)

@app.route("/clear")
def clear():

    chat_history.clear()

    return render_template_string(HTML, chat=chat_history)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
