from flask import Flask, abort, redirect, render_template, request, url_for
from repositories import builds_repo
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

cart = []
current_user = {'user_id':1};

@app.get('/')
def index():
    return render_template('index.html')

@app.get('/startBuild')
def showStartBuild():
    content = request.args.get('content', 'motherboard')
    if content not in ['motherboard', 'cpu', 'storage', 'power', 'graphics', 'cooling', 'memory', 'casing'] or content is None:
        return 'Bad Request', 400
    all_parts = builds_repo.get_all_parts_by_part_type(content)
    return render_template('startBuild.html', data=all_parts)

@app.get('/parts/<int:part_id>')
def showSinglePart(part_id):
    part = builds_repo.get_part_by_id(part_id)
    return render_template('singlePart.html', part=part)

@app.get('/faq')
def showFAQ():
    return render_template('faq.html')

@app.route('/preBuilts')
def showPreBuilts():
    #for navigating the vertical bar. Default to gaming.
    content = request.args.get('content', 'gaming')
    #temporary data for testing.
    image_url = 'https://ralfvanveen.com/wp-content/uploads//2021/06/Placeholder-_-Begrippenlijst.svg'
    data = builds_repo.get_all_builds_by_build_type(content)
    #Pass the data to be shown on the cards
    return render_template('preBuilts.html', data=data)

@app.get('/cart')
def showCart():
    #Loop through the items and add up the prices
    total = 0.0
    for item in cart:
        total += float(item['price'])
    #Pass in the cart and the totaled prices
    return render_template('cart.html', cart = cart, estimate = total)

@app.post('/remove_from_cart')
def remove_from_cart():
    #grab the id of the item to be removed
    item_id = int(request.form['item_id'])
    #look through cart and delete the target item
    for item in cart:
        if item['part_id'] == item_id:
            cart.remove(item)
            break
    #Show updated cart
    return redirect('/cart')

@app.post('/add_to_cart')
def add_to_cart():
    #grab the item to be added
    part_id = request.form.get('part_id')
    if part_id is not None:
        cart.append(builds_repo.get_part_by_id(part_id))
    return redirect(request.referrer or url_for('index'))

@app.get('/signUp')
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
    does_existing_user = builds_repo.does_username_exist(username)
    if does_existing_user:
        abort(400)
    builds_repo.create_user(username, password)

    return redirect(url_for('showLogin'))

@app.get('/login')
def showLogin():
    return render_template('login.html')

@app.post('/save_build')
def save_build():
    #grab the item to be added
    build_id = request.form['build_id']
    if build_id is not None:
        builds_repo.save_build(build_id, current_user['user_id'])
    return redirect(request.referrer or url_for('index'))