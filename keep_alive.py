from flask import Flask, render_template as rr_tt, redirect
from threading import Thread

app = Flask(__name__)

@app.route('/')
@app.route("/home")
def home():
    return rr_tt("index.html")

@app.route("/invite")
def invite():
  return redirect("https://discord.com/api/oauth2/authorize?client_id=790832263260012573&permissions=8&scope=bot")
  
@app.route("/support")
@app.route("/discord")
def support():
  return redirect("https://discord.gg/PKP4mG6E3G")
  

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()
