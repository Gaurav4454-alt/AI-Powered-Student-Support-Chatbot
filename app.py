from flask import Flask, request, render_template_string
import google.generativeai as genai

app = Flask(__name__)

genai.configure(api_key="YOUR_API_KEY")
model = genai.GenerativeModel("gemini-1.5-flash")

HTML = """
<h1>🎓 EduAssist AI</h1>

<form action="/chat">
  <input name="msg" placeholder="Ask your doubt..." style="width:300px;padding:10px">
  <button>Ask</button>
</form>

<p><b>Answer:</b> {{reply}}</p>
"""

@app.route("/")
def home():
    return render_template_string(HTML, reply="")

@app.route("/chat")
def chat():
    user = request.args.get("msg")
    response = model.generate_content(user)
    return render_template_string(HTML, reply=response.text)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
