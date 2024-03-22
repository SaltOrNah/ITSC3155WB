from flask import Flask, abort, redirect, render_template, request

app = Flask(__name__)

@app.get('/')
def index():
    return render_template('index.html')

@app.get('/startBuild')
def showStartBuild():
    return render_template('startBuild.html')

@app.get('/faq')
def showFAQ():
    return render_template('faq.html')

@app.get('/preBuilts')
def showPreBuilts():
    return render_template('preBuilts.html')

@app.get('/browse')
def showBrowse():
    return render_template('browse.html')

@app.get('/cart')
def showCart():
    return render_template('cart.html')

@app.get('/signUp')
def showSignUp():
    return render_template('signUp.html')

@app.get('/login')
def showLogin():
    return render_template('login.html')