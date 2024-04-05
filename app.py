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
    #for navigating the vertical bar. Default to gaming.
    content = request.args.get('content', 'gaming')
    #temporary data for testing.
    image_url = 'https://ralfvanveen.com/wp-content/uploads//2021/06/Placeholder-_-Begrippenlijst.svg'
    if content == 'gaming':
        data = [{'name': 'pc1', 'price': '145.00', 'rating': 4.8, 'image_url': image_url},
                {'name': 'pc2', 'price': '270.00', 'rating': 3.4, 'image_url': image_url},
                {'name': 'pc3', 'price': '500.50', 'rating': 2.1, 'image_url': image_url},
                {'name': 'pc4', 'price': '200.00', 'rating': 4.5, 'image_url': image_url},
                {'name': 'pc5', 'price': '310.00', 'rating': 3.6, 'image_url': image_url}]
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
    #Pass the data to be shown on the cards
    return render_template('preBuilts.html', data=data)

link = 'https://www.amazon.com/AMD-5700X-16-Thread-Unlocked-Processor/dp/B09VCHQHZ6/ref=sr_1_3?crid=B5DDE9787RRV&dib=eyJ2IjoiMSJ9.sjQ8HZCO8DmL1xXA9iggT5SUorojRT-O0Gs_tq1QYfkD_fvu9bzjXUTSPzM5_qnKn14qY7RY3REET3vUIY3xJFw65rQGcDXBDi0wBEh0JLcb3Q5geHzdV7lhid5mMHJP6HBxYf0aFB0rIYq2wDainVU2jKrEQ9Xcc7zArdSUr_Zqyl64h5yMnorw8Gwob2w4faS5CA_6wMyDtEi3ElexAhJBiIqbFhlvkWNMpF7Qgvw.OwWyTWiSI_9DQHMvOIBxMMgjFt0wPHwIKo3lReMYhM8&dib_tag=se&keywords=cpu&qid=1712112592&sprefix=cpu%2Caps%2C77&sr=8-3&th=1'
cart = [{'id': 1, 'item_type': 'CPU', 'name': 'part1', 'price': '130.00', 'item_link': link},
        {'id': 2, 'item_type': 'GPU', 'name': 'part2', 'price': '250.00', 'item_link': link},
        {'id': 3, 'item_type': 'RAM', 'name': 'part3', 'price': '80.00', 'item_link': link},
        {'id': 4, 'item_type': 'Motherboard', 'name': 'part4', 'price': '180.00', 'item_link': link},
        {'id': 5, 'item_type': 'SSD', 'name': 'part5', 'price': '100.00', 'item_link': link},
        {'id': 6, 'item_type': 'Power Supply', 'name': 'part6', 'price': '70.00', 'item_link': link},
        {'id': 7, 'item_type': 'Case', 'name': 'part7', 'price': '50.00', 'item_link': link}]

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
        if item['id'] == item_id:
            cart.remove(item)
            break
    #Show updated cart
    return redirect('/cart')

@app.post('/add_to_cart')
def add_to_cart():
    #grab the item to be added
    item = request.form['item']
    cart.append(item)
    return redirect(request.referrer or url_for('index'))

@app.get('/signUp')
def showSignUp():
    return render_template('signUp.html')

@app.get('/login')
def showLogin():
    return render_template('login.html')
