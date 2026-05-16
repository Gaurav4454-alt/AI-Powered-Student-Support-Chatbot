from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
<title>EduAssist AI</title>

<style>
body {
    font-family: Arial;
    background: #0f172a;
    color: white;
    text-align: center;
}

.container {
    width: 60%;
    margin: auto;
    margin-top: 50px;
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
    padding: 12px 20px;
    border-radius: 8px;
    border: none;
    background: #38bdf8;
    color: black;
    cursor: pointer;
}

.chat {
    margin-top: 20px;
    text-align: left;
    background: #111827;
    padding: 15px;
    border-radius: 10px;
}

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

<h1>🎓 EduAssist AI</h1>

<div class="box">

<form action="/chat">
    <input name="msg" placeholder="Ask your question...">
    <button>Send</button>
</form>

<div class="chat">
<p><b>You:</b> {{user}}</p>
<p><b>Bot:</b> {{reply}}</p>
</div>

</div>
</div>

<div class="footer">
Made by Gaurav | AI Student Support Bot
</div>

</body>
</html>
"""

def get_answer(msg):
    msg = msg.lower()

    if "exam" in msg:
        return "Focus on PYQs, revision and short notes."
    elif "python" in msg:
        return "Python is used for AI, web development and automation."
    elif "project" in msg:
        return "Try AI chatbot, portfolio website or automation tool."
    elif "hello" in msg:
        return "Hello! I am EduAssist AI 🤖"
    else:
        return "I can help with exams, coding and projects."

@app.route("/")
def home():
    return render_template_string(HTML, user="", reply="Ask me anything!")

@app.route("/chat")
def chat():
    msg = request.args.get("msg")
    reply = get_answer(msg)
    return render_template_string(HTML, user=msg, reply=reply)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
