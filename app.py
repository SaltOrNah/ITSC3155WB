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

@app.get('/cart')
def showCart():
    return render_template('cart.html')

@app.get('/signUp')
def showSignUp():
    return render_template('signUp.html')

@app.get('/login')
def showLogin():
    return render_template('login.html')