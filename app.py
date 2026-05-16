from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>AI Powered Student Support Chatbot</h1>

    <form action="/chat">
        <input name='msg' placeholder='Ask your question'>
        <button>Send</button>
    </form>
    """

@app.route("/chat")
def chat():
    return """
    <h2>Chatbot Reply</h2>

    <p>Hello Student! Your query has been received successfully.</p>

    <a href="/">Go Back</a>
    """

app.run()
