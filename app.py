from flask import Flask, abort, redirect, render_template, request, url_for
from dotenv import load_dotenv
from repositories import user_repository


load_dotenv()

app = Flask(__name__)

@app.get('/')
def index():
    return render_template('index.html')

@app.get('/startBuild')
def showStartBuild():
    content = request.args.get('content', 'motherboard')
    image_url = 'https://ralfvanveen.com/wp-content/uploads//2021/06/Placeholder-_-Begrippenlijst.svg'
    if content == 'motherboard':
        data = [{'name': 'motherboard1', 'price': '70.00', 'rating': 4.8, 'brand': 'Intel', 'image_url': image_url},
                {'name': 'motherboard2', 'price': '120.00', 'rating': 3.4, 'brand': 'Intel', 'image_url': image_url},
                {'name': 'motherboard3', 'price': '69.50', 'rating': 2.1, 'brand': 'Intel', 'image_url': image_url},
                {'name': 'motherboard4', 'price': '100.00', 'rating': 4.5, 'brand': 'Intel', 'image_url': image_url},
                {'name': 'motherboard5', 'price': '90.00', 'rating': 3.6, 'brand': 'Intel', 'image_url': image_url},
                {'name': 'motherboard6', 'price': '89.99', 'rating': 3.3, 'brand': 'Intel', 'image_url': image_url}]
    elif content == 'cpu':
        data = [{'name':'cpu1', 'price':'180.00', 'rating':4.2, 'brand': 'Intel', 'image_url': image_url},
                {'name':'cpu2', 'price':'320.00', 'rating':3.9, 'brand': 'Intel', 'image_url': image_url},
                {'name':'cpu3', 'price':'450.00', 'rating':3.1, 'brand': 'Intel', 'image_url': image_url}]
    elif content == 'storage':
        data = [{'name':'storage1', 'price':'200.00', 'rating':4.5, 'brand': 'Intel', 'image_url': image_url},
                {'name':'storage2', 'price':'290.00', 'rating':3.7, 'brand': 'Intel', 'image_url': image_url},
                {'name':'storage3', 'price':'550.00', 'rating':2.9, 'brand': 'Intel', 'image_url': image_url}]
    elif content == 'power':
        data = [{'name':'power1', 'price':'160.00', 'rating':4.0, 'brand': 'Intel', 'image_url': image_url},
                {'name':'power2', 'price':'310.00', 'rating':3.6, 'brand': 'Intel', 'image_url': image_url},
                {'name':'power3', 'price':'480.00', 'rating':3.3, 'brand': 'Intel', 'image_url': image_url}]
    elif content == 'graphics':
        data = [{'name':'graphics1', 'price':'180.00', 'rating':4.2, 'brand': 'Intel', 'image_url': image_url},
                {'name':'graphics2', 'price':'320.00', 'rating':3.9, 'brand': 'Intel', 'image_url': image_url},
                {'name':'graphics3', 'price':'450.00', 'rating':3.1, 'brand': 'Intel', 'image_url': image_url}]
    elif content == 'cooling':
        data = [{'name':'cooling1', 'price':'200.00', 'rating':4.5, 'brand': 'Intel', 'image_url': image_url},
                {'name':'cooling2', 'price':'290.00', 'rating':3.7, 'brand': 'Intel', 'image_url': image_url},
                {'name':'cooling3', 'price':'550.00', 'rating':2.9, 'brand': 'Intel', 'image_url': image_url}]
    elif content == 'memory':
        data = [{'name':'memory1', 'price':'160.00', 'rating':4.0, 'brand': 'Intel', 'image_url': image_url},
                {'name':'memory2', 'price':'310.00', 'rating':3.6, 'brand': 'Intel', 'image_url': image_url},
                {'name':'memory3', 'price':'480.00', 'rating':3.3, 'brand': 'Intel', 'image_url': image_url}]
    elif content == 'casing':
        data = [{'name':'casing1', 'price':'160.00', 'rating':4.0, 'brand': 'Intel', 'image_url': image_url},
                {'name':'casing2', 'price':'310.00', 'rating':3.6, 'brand': 'Intel', 'image_url': image_url},
                {'name':'casing3', 'price':'480.00', 'rating':3.3, 'brand': 'Intel', 'image_url': image_url}]
    elif content == 'accessories':
        data = [{'name':'accessories1', 'price':'160.00', 'rating':4.0, 'brand': 'Intel', 'image_url': image_url},
                {'name':'accessories2', 'price':'310.00', 'rating':3.6, 'brand': 'Intel', 'image_url': image_url},
                {'name':'accessories3', 'price':'480.00', 'rating':3.3, 'brand': 'Intel', 'image_url': image_url}]
    else:
        abort(404)

    return render_template('startBuild.html', data=data)

@app.get('/faq')
def showFAQ():
    return render_template('faq.html')

@app.route('/preBuilts')
def showPreBuilts():
    content = request.args.get('content', 'gaming')
    image_url = 'https://ralfvanveen.com/wp-content/uploads//2021/06/Placeholder-_-Begrippenlijst.svg'
    if content == 'gaming':
        data = [{'name': 'pc1', 'price': '145.00', 'rating': 4.8, 'image_url': image_url},
                {'name': 'pc2', 'price': '270.00', 'rating': 3.4, 'image_url': image_url},
                {'name': 'pc3', 'price': '500.50', 'rating': 2.1, 'image_url': image_url},
                {'name': 'pc4', 'price': '200.00', 'rating': 4.5, 'image_url': image_url},
                {'name': 'pc5', 'price': '310.00', 'rating': 3.6, 'image_url': image_url},
                {'name': 'pc6', 'price': '480.00', 'rating': 3.3, 'image_url': image_url},
                {'name': 'pc7', 'price': '180.00', 'rating': 4.2, 'image_url': image_url},
                {'name': 'pc8', 'price': '320.00', 'rating': 3.9, 'image_url': image_url},
                {'name': 'pc9', 'price': '450.00', 'rating': 3.1, 'image_url': image_url},
                {'name': 'pc10', 'price': '160.00', 'rating': 4.0, 'image_url': image_url},
                {'name': 'pc11', 'price': '290.00', 'rating': 3.7, 'image_url': image_url},
                {'name': 'pc12', 'price': '550.00', 'rating': 2.9, 'image_url': image_url}]
    elif content == 'recording':
        data = [{'name':'pc1', 'price':'180.00', 'rating':4.2, 'image_url': image_url},
                {'name':'pc2', 'price':'320.00', 'rating':3.9, 'image_url': image_url},
                {'name':'pc3', 'price':'450.00', 'rating':3.1, 'image_url': image_url}]
    elif content == 'office':
        data = [{'name':'pc1', 'price':'200.00', 'rating':4.5, 'image_url': image_url},
                {'name':'pc2', 'price':'290.00', 'rating':3.7, 'image_url': image_url},
                {'name':'pc3', 'price':'550.00', 'rating':2.9, 'image_url': image_url}]
    elif content == 'school':
        data = [{'name':'pc1', 'price':'160.00', 'rating':4.0, 'image_url': image_url},
                {'name':'pc2', 'price':'310.00', 'rating':3.6, 'image_url': image_url},
                {'name':'pc3', 'price':'480.00', 'rating':3.3, 'image_url': image_url}]
    return render_template('preBuilts.html', data=data)

@app.route('/signUp')
def showSignUp():
    return render_template('signUp.html')

@app.post('/signUp')
def createUser():
    username = request.form.get('username')
    password = request.form.get('password')
    print(username)
    print(password)
    if not username or not password:
        abort(400)
    does_existing_user = user_repository.does_username_exist(username)
    if does_existing_user:
        abort(400)
    user_repository.create_user(username, password)

    return redirect(url_for('showLogin'))

@app.get('/login')
def showLogin():
    return render_template('login.html')

@app.get('/faq')
def showFaq():
    return render_template('faq.html')