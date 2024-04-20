from flask import Flask, abort, redirect, render_template, request, url_for, session
from repositories import builds_repo
from dotenv import load_dotenv
from flask_bcrypt import Bcrypt
load_dotenv()

app = Flask(__name__)

app.secret_key = 'secret_wah'

bcrypt = Bcrypt(app)

cart = []
current_user = {'user_id':1};

@app.get('/')
def index():
    return render_template('index.html', cart = cart, user = current_user)

@app.get('/startBuild/<part_type>')
def showStartBuild(part_type = 'motherboard', query='', search_by = 'component', sort_by='price'):
    if part_type not in ['motherboard', 'cpu', 'storage', 'power', 'graphics', 'cooling', 'memory', 'casing'] or part_type == None:
        return 'Bad Request', 400

    all_parts = builds_repo.get_all_parts_by_part_type(part_type)

    #search parameters
    search_query = request.args.get('q', None)
    search_by = request.args.get('sh')
    sort_by = request.args.get('st', 'price')
    if(search_query != None):
        #Setting the type of search
        if(search_by == 'component'):
            all_parts = builds_repo.get_component_parts_by_search(search_query.lower(), part_type)
        elif(search_by == 'all'):
            all_parts = builds_repo.get_all_parts_by_search(search_query.lower())
        else:
            pass
    #sorting list by selected
    if(sort_by != None and sort_by != ''):
        match sort_by:
            case 'price':
                all_parts = sorted(all_parts, key=lambda d: d['price'])
            case 'rating':
                all_parts = sorted(all_parts, key=lambda d: d['rating'], reverse = True)
            case 'nameAZ':
                all_parts = sorted(all_parts, key=lambda d: d['part_name'])
            case 'nameZA':
                all_parts = sorted(all_parts, key=lambda d: d['part_name'], reverse = True)
            case "brand":
                all_parts = sorted(all_parts, key=lambda d: d['brand'])
    return render_template('startBuild.html', data=all_parts, part_type=part_type, query=search_query, search_by=search_by, sort_by=sort_by, cart = cart, user = current_user)

@app.get('/parts/<int:part_id>')
def showSinglePart(part_id):
    part = builds_repo.get_part_by_id(part_id)
    return render_template('singlePart.html', part=part, cart = cart, user = current_user)

@app.get('/faq')
def showFAQ():
    return render_template('faq.html', cart = cart, user = current_user)

@app.route('/preBuilts')
def showPreBuilts():
    #for navigating the vertical bar. Default to gaming.
    content = request.args.get('content', 'gaming')
    #temporary data for testing.
    image_url = 'https://ralfvanveen.com/wp-content/uploads//2021/06/Placeholder-_-Begrippenlijst.svg'
    data = builds_repo.get_all_builds_by_build_type(content)
    #Pass the data to be shown on the cards
    return render_template('preBuilts.html', data=data, cart = cart, user = current_user)

@app.get('/cart')
def showCart():
    #Loop through the items and add up the prices
    total = 0.0
    for item in cart:
        total += float(item['price'])
    #Pass in the cart and the totaled prices
    return render_template('cart.html', estimate = total, cart = cart, user = current_user)

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
    return render_template('signUp.html', cart = cart, user = current_user)

@app.post('/signUp')
def createUser():
    username = request.form.get('username')
    password = request.form.get('password')
    print(username)
    print(password)
    if not username or not password:
        abort(400)
    does_username_exist = builds_repo.does_username_exist(username)
    if does_username_exist:
        abort(400)
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    builds_repo.create_user(username, hashed_password)
    if session:
        return redirect(url_for('index'))

    return redirect(url_for('showLogin'))

@app.post('/login')
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    if not username or not password:
        abort(400)
    user = builds_repo.get_user_by_username(username)
    if user is None:
        abort(401)
    stored_hashed_passowrd = user['hashed_password']
    if not bcrypt.check_password_hash(stored_hashed_passowrd, password):
        abort(401)
    session['user_id'] = user['user_id']
    print("hello there")
    if session:
        return redirect(url_for('index'))
    return redirect(url_for('index'))


@app.get('/login')
def showLogin():
    return render_template('login.html', cart = cart, user = current_user)

@app.post('/')
def logout():
    del session[current_user]
    return redirect('/')

@app.route('/show_saves')
def show_saves():
    #temporary data for testing.
    image_url = 'https://ralfvanveen.com/wp-content/uploads//2021/06/Placeholder-_-Begrippenlijst.svg'
    data = builds_repo.get_all_saves_from_user_id(current_user['user_id'])
    #Pass the data to be shown on the cards
    if 'user_id' not in session:
        return redirect("/")
    return render_template('savedBuilds.html', data=data, cart = cart, user = current_user)

@app.post('/save_build')
def save_build():
    #grab the item to be added
    build_id = request.form['build_id']
    if build_id is not None:
        builds_repo.save_build(build_id, current_user['user_id'])
    return redirect(request.referrer or url_for('index'))

@app.post('/remove_save')
def remove_save():
    #grab the item to be added
    build_id = request.form['build_id']
    if build_id is not None:
        builds_repo.remove_saved_build(build_id, current_user['user_id'])
    return redirect(request.referrer or url_for('index'))