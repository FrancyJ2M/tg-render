from flask import Flask, request
import os

server = Flask(__name__)

@server.route("/")
def webhook():
    return "!", 200
       
server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 10000)))

