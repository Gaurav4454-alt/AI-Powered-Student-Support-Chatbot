from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML = """
<h1>🎓 EduAssist AI - Student Support Bot</h1>

<form action="/chat">
  <input name="msg" placeholder="Ask your question..." style="width:300px;padding:10px">
  <button>Ask</button>
</form>

<hr>

<p><b>User:</b> {{user}}</p>
<p><b>Bot:</b> {{reply}}</p>
"""

def get_answer(msg):
    msg = msg.lower()

    if "exam" in msg:
        return "Prepare with previous year papers and focus on important topics."
    elif "python" in msg:
        return "Python is a programming language used for AI, web and automation."
    elif "project" in msg:
        return "You can build AI chatbot, website or automation system for hackathon."
    elif "hello" in msg:
        return "Hello! I am EduAssist AI, your student support assistant."
    else:
        return "I can help with exams, projects, coding and study guidance."

@app.route("/")
def home():
    return render_template_string(HTML, user="", reply="")

@app.route("/chat")
def chat():
    msg = request.args.get("msg")
    reply = get_answer(msg)
    return render_template_string(HTML, user=msg, reply=reply)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
