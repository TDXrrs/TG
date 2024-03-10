from flask import Flask 
from threading import Thread
app = Flask('')
@app.route('/')
def ping():
    return "pong"
def run():
    app.run(host='0.0.0.0',port=8000,debug=True)
def server():
    t = Thread(target=run)
    t.start()
