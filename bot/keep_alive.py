from flask import Flask
from waitress import serve
from threading import Thread

# デプロイ対応用(https://www.utsuboublog.com/entry/discord-bot-replit)
app = Flask('')

@app.route('/')
def home():
    return "I'm alive"
def run():
    app.run(host='0.0.0.0', port=8080)
    serve(app, host='0.0.0.0', port=8080)
def keep_alive():
    t = Thread(target=run)
    t.start()