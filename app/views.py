'''
Autor: Wentao Lin
Description: 
Date: 2020-12-26 12:35:14
LastEditTime: 2020-12-30 22:20:39
LastEditors: Wentao Lin
'''

from flask import render_template, flash, redirect, session, url_for, request, g, make_response
from flask.helpers import send_from_directory
from flask_admin.contrib.sqla import ModelView
from werkzeug.utils import secure_filename
import os
import uuid

from app import app, db, admin
from .models import User, Goods, Address, Order, shopping_cart, shopping_order
from .forms import Signup, AddAddress, AddCommodity, ChangePassword



admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Goods, db.session))
admin.add_view(ModelView(Address, db.session))
admin.add_view(ModelView(Order, db.session))



@app.route("/", methods=['GET', 'POST'])
def homepage():
    if Goods.query.filter(Goods.type == "home appliances").count() < 4:
        home_appliances = Goods.query.filter(Goods.type == "home appliances").all()
        number = 4 - Goods.query.filter(Goods.type == "home appliances").count()
        home_appliances_number = []
        for i in range(number):
            home_appliances_number.append("0")
    else:
        home_appliances = Goods.query.filter(Goods.type == "home appliances").limit(4)
        home_appliances_number = []
   
    if Goods.query.filter(Goods.type == "kitchen ware").count() < 4:
        kitchen_wares = Goods.query.filter(Goods.type == "kitchen ware").all()
        number = 4 - Goods.query.filter(Goods.type == "kitchen ware").count()
        kitchen_wares_number = []
        for i in range(number):
            kitchen_wares_number.append("0")
    else:
        kitchen_wares = Goods.query.filter(Goods.type == "kitchen ware").limit(4)
        kitchen_wares_number = []
   
    if Goods.query.filter(Goods.type == "garden stuff").count() < 4:
        garden_stuffs = Goods.query.filter(Goods.type == "garden stuff").all()
        number = 4 - Goods.query.filter(Goods.type == "garden stuff").count()
        garden_stuffs_number = []
        for i in range(number):
            garden_stuffs_number.append("0")
    else:
        garden_stuffs = Goods.query.filter(Goods.type == "garden stuff").limit(4)
        garden_stuffs_number = []
   
    if Goods.query.filter(Goods.type == "clothes").count() < 4:
        clothes = Goods.query.filter(Goods.type == "clothes").all()
        number = 4 - Goods.query.filter(Goods.type == "clothes").count()
        clothes_number = []
        for i in range(number):
            clothes_number.append("0")
    else:
        clothes = Goods.query.filter(Goods.type == "clothes").limit(4)
        clothes_number = []
   
    if Goods.query.filter(Goods.type == "books").count() < 4:
        books = Goods.query.filter(Goods.type == "books").all()
        number = 4 - Goods.query.filter(Goods.type == "books").count()
        books_number = []
        for i in range(number):
            books_number.append("0")
    else:
        books = Goods.query.filter(Goods.type == "books").limit(4)
        books_number = []
  
    if Goods.query.filter(Goods.type == "drinks").count() < 4:
        drinks = Goods.query.filter(Goods.type == "drinks").all()
        number = 4 - Goods.query.filter(Goods.type == "drinks").count()
        drinks_number = []
        for i in range(number):
            drinks_number.append("0")
    else:
        drinks = Goods.query.filter(Goods.type == "drinks").limit(4)
        drinks_number = []
  
    if Goods.query.filter(Goods.type == "furniture").count() < 4:
        furnitures = Goods.query.filter(Goods.type == "furniture").all()
        number = 4 - Goods.query.filter(Goods.type == "furniture").count()
        furnitures_number = []
        for i in range(number):
            furnitures_number.append("0")
    else:
        furnitures = Goods.query.filter(Goods.type == "furniture").limit(4)
        furnitures_number = []
  
    if Goods.query.filter(Goods.type == "toys").count() < 4:
        toys = Goods.query.filter(Goods.type == "toys").all()
        number = 4 - Goods.query.filter(Goods.type == "toys").count()
        toys_number = []
        for i in range(number):
            toys_number.append("0")
    else:
        toys = Goods.query.filter(Goods.type == "toys").limit(4)
        toys_number = []

    username = request.cookies.get("username")
    number_cart = 0
    if username == '' or username == None:
        number_cart = 0
    else:
        cart = User.query.filter(User.username == username).first().goods
        for i in cart:
            number_cart += 1
    if request.method == "POST":
        if username == '' or username == None:
            flash("Haven't Login!!")
        else:
            user = User.query.filter(User.username == username).first()
            id = request.form.get("good_id")
            good = Goods.query.get(id)
            user.goods.append(good)
            db.session.commit()
            return redirect("/")


    return render_template('index.html',
                            title='homepage',
                            home_appliances = home_appliances,
                            home_appliances_number = home_appliances_number,
                            kitchen_wares = kitchen_wares,
                            kitchen_wares_number = kitchen_wares_number,
                            garden_stuffs = garden_stuffs,
                            garden_stuffs_number = garden_stuffs_number,
                            clothes = clothes,
                            clothes_number = clothes_number,
                            books = books,
                            books_number = books_number,
                            drinks = drinks,
                            drinks_number = drinks_number,
                            furnitures = furnitures,
                            furnitures_number = furnitures_number,
                            toys = toys,
                            toys_number = toys_number,
                            number_cart = number_cart
                            )


@app.route("/sign-up", methods=['GET', 'POST'])
def signup():
    form = Signup()
    if request.method == 'GET':
        form = Signup()
        return render_template('signup.html', form=form)
    else:
        form = Signup(formdata=request.form)
        if form.validate_on_submit():
            # Determine if the user name has been used
            usernames = User.query.all()
            for username in usernames:
                if username.username == form.username.data:
                    flash('This username "' + username.username + '" already been used.')
                    return redirect("/sign-up")

            # Decide if user want to sell something
            sell = request.values.getlist("sell")
            if sell == ["sell-goods"]:
                u = User(username = form.username.data, password = form.password.data, sell = True)
            else:
                u = User(username = form.username.data, password = form.password.data, sell = False)
            db.session.add(u)
            db.session.commit()
            return redirect('/')
        return render_template('signup.html',
                                form=form
                                )

@app.route('/setcookie', methods=['POST', 'GET'])
def setcookie():
    username = ''
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['pwd']
        users = User.query.all()
        value = 0
        
        # judge the username is exist, username and password are match
        for user in users:
            if user.username == username:
                value = 1
                if user.password == password:
                    break
                else:
                    flash('The username and password do not match.')
                    app.logger.error('The username and password do not match.')
                    return redirect("/")
        if value == 0:
            flash('The username is not registered.')
            return redirect("/")
                     
    resp = make_response(redirect("/"))
    resp.set_cookie('username', username)

    return resp

@app.route("/mypage")
def my():
    username = request.cookies.get("username")
    user = User.query.filter(User.username == username).first()
    number_cart = 0
    if username == '' or username == None:
        number_cart = 0
    else:
        cart = User.query.filter(User.username == username).first().goods
        for i in cart:
            number_cart += 1
    if user == None:
        sell = False
    else:
        sell = user.sell
    return render_template("my.html",
                            title = "My Page",
                            username = username,
                            sell = sell,
                            number_cart = number_cart
                            )

@app.route("/add_address", methods=['POST', 'GET'])
def add_address():
    form = AddAddress()
    username = request.cookies.get("username")
    number_cart = 0
    if username == '' or username == None:
        number_cart = 0
    else:
        cart = User.query.filter(User.username == username).first().goods
        for i in cart:
            number_cart += 1
    if request.method == "POST":
        if form.validate_on_submit():
            address = form.house.data + ", " + form.street.data + ", " + form.city.data +  ", " + form.province.data + ", " + form.country.data + ", " + form.postcode.data
            a = Address(place = address)
            user = User.query.filter(User.username == username).first()
            a.user = user.userId
            db.session.add(a)
            db.session.commit()
            return redirect("/show_addresses")
    return render_template("add-address.html",
                            title = "Add Address",
                            username = username,
                            form = form,
                            number_cart = number_cart
                            )    

@app.route("/show_addresses", methods=['POST', 'GET'])
def show_addresses():
    username = request.cookies.get("username")   
    user = User.query.filter(User.username == username).first()
    number_cart = 0
    if username == '' or username == None:
        number_cart = 0
    else:
        cart = User.query.filter(User.username == username).first().goods
        for i in cart:
            number_cart += 1
    if user != None:
        addresses = Address.query.filter(Address.user == user.userId).all()
    else:
        addresses = ''
    if request.method == 'POST':
        # get the botton corresponding data's id
        id = request.form.get("id")
        p = Address.query.filter(Address.addressId == id).first()
        db.session.delete(p)
        db.session.commit()
        return redirect("/show_addresses")
    return render_template("show-addresses.html",
                            title = "Show Addresses",
                            username = username,
                            addresses = addresses,
                            number_cart = number_cart
                            )      

@app.route("/create_commodity", methods=['POST', 'GET'])
def create_commodity():
    username = request.cookies.get("username")
    number_cart = 0
    if username == '' or username == None:
        number_cart = 0
    else:
        cart = User.query.filter(User.username == username).first().goods
        for i in cart:
            number_cart += 1
    form = AddCommodity()
    if request.method == "POST":
        if form.validate_on_submit():
            i = form.image.data
            filename = random_filename(i.filename)
            basepath = os.path.dirname(__file__)
            upload_path = os.path.join(basepath, 'static/img/upload',secure_filename(filename))
            i.save(upload_path)
            upload_path = 'static/img/upload/' + filename
            user = User.query.filter(User.username == username).first()
            g = Goods(image=upload_path,title=form.title.data, price=form.price.data, number=form.number.data, type=form.classify.data, sell_goods=user.userId)
            db.session.add(g)
            db.session.commit()
            flash("Create '" + g.title + "' successful!!!")
            return redirect("/create_commodity")
    return render_template("add-commodity.html",
                            title = "Add Commodity",
                            username = username,
                            form = form,
                            number_cart = number_cart
                            )

def random_filename(filename):
    ext = os.path.splitext(filename)[1]
    new_filename = uuid.uuid4().hex + ext
    return new_filename

@app.route("/change_password", methods=['GET', 'POST'])
def change_password():
    form = ChangePassword()
    username = request.cookies.get("username")
    number_cart = 0
    if username == '' or username == None:
        number_cart = 0
    else:
        cart = User.query.filter(User.username == username).first().goods
        for i in cart:
            number_cart += 1
    user = User.query.filter(User.username == username).first()
    if user == None:
        sell = False
    else:
        sell = user.sell
    if request.method == 'POST':
        if form.validate_on_submit():
            if user.password == form.password.data:
                user.password = form.new_password.data
                # Decide if user want to sell something
                sell = request.values.getlist("sell")
                if sell == ["sell-goods"]:
                    user.sell = True
                db.session.add(user)
                db.session.commit()
                flash("Change password success!")
                return redirect('/mypage')
            else:
                flash("The password is wrong!")
                return redirect('/change_password')
    return render_template('change-password.html',
                            form = form,
                            username = username,
                            sell = sell,
                            number_cart = number_cart
                            )

@app.route("/show_commodity")
def show_commodity():
    username = request.cookies.get("username")
    number_cart = 0
    if username == '' or username == None:
        number_cart = 0
    else:
        cart = User.query.filter(User.username == username).first().goods
        for i in cart:
            number_cart += 1
    user = User.query.filter(User.username == username).first()
    goods = Goods.query.filter(Goods.sell_goods == user.userId).all()
    return render_template('my-commodity.html',
                            username = username,
                            goods = goods,
                            number_cart = number_cart
                            )

@app.route("/home_appliances", methods=['POST', 'GET'])
def home_appliances():
    username = request.cookies.get("username")
    number_cart = 0
    if username == '' or username == None:
        number_cart = 0
    else:
        cart = User.query.filter(User.username == username).first().goods
        for i in cart:
            number_cart += 1
    if request.method == "POST":
        if username == '':
            flash("Haven't Login!!")
        else:
            user = User.query.filter(User.username == username).first()
            id = request.form.get("good_id")
            good = Goods.query.get(id)
            user.goods.append(good)
            db.session.commit()
            return redirect("/home_appliances")

    goods = Goods.query.filter(Goods.type == "home appliances").all()
    return render_template("all_goods.html",
                            title = "Home Appliances",
                            goods = goods,
                            number_cart = number_cart
                            )
        
@app.route("/kitchen_ware", methods=['POST', 'GET'])
def kitchen_ware():
    username = request.cookies.get("username")
    number_cart = 0
    if username == '' or username == None:
        number_cart = 0
    else:
        cart = User.query.filter(User.username == username).first().goods
        for i in cart:
            number_cart += 1
    if request.method == "POST":
        if username == '':
            flash("Haven't Login!!")
        else:
            user = User.query.filter(User.username == username).first()
            id = request.form.get("good_id")
            good = Goods.query.get(id)
            user.goods.append(good)
            db.session.commit()
            return redirect("/kitchen_ware")

    goods = Goods.query.filter(Goods.type == "kitchen ware").all()
    return render_template("all_goods.html",
                            title = "Kitchen Ware",
                            goods = goods,
                            number_cart = number_cart
                            )
                            
@app.route("/garden_stuff", methods=['POST', 'GET'])
def garden_stuff():
    username = request.cookies.get("username")
    number_cart = 0
    if username == '' or username == None:
        number_cart = 0
    else:
        cart = User.query.filter(User.username == username).first().goods
        for i in cart:
            number_cart += 1
    if request.method == "POST":
        if username == '':
            flash("Haven't Login!!")
        else:
            user = User.query.filter(User.username == username).first()
            id = request.form.get("good_id")
            good = Goods.query.get(id)
            user.goods.append(good)
            db.session.commit()
            return redirect("/garden_stuff")

    goods = Goods.query.filter(Goods.type == "garden stuff").all()
    return render_template("all_goods.html",
                            title = "Garden Stuff",
                            goods = goods,
                            number_cart = number_cart
                            )

@app.route("/clothes", methods=['POST', 'GET'])
def clothes():
    username = request.cookies.get("username")
    number_cart = 0
    if username == '' or username == None:
        number_cart = 0
    else:
        cart = User.query.filter(User.username == username).first().goods
        for i in cart:
            number_cart += 1
    if request.method == "POST":
        if username == '' or username == None:
            flash("Haven't Login!!")
        else:
            user = User.query.filter(User.username == username).first()
            id = request.form.get("good_id")
            good = Goods.query.get(id)
            user.goods.append(good)
            db.session.commit()
            return redirect("/clothes")

    goods = Goods.query.filter(Goods.type == "clothes").all()
    return render_template("all_goods.html",
                            title = "Clothes",
                            goods = goods,
                            number_cart = number_cart
                            )

@app.route("/books", methods=['POST', 'GET'])
def books():
    username = request.cookies.get("username")
    number_cart = 0
    if username == '' or username == None:
        number_cart = 0
    else:
        cart = User.query.filter(User.username == username).first().goods
        for i in cart:
            number_cart += 1
    if request.method == "POST":
        if username == '':
            flash("Haven't Login!!")
        else:
            user = User.query.filter(User.username == username).first()
            id = request.form.get("good_id")
            good = Goods.query.get(id)
            user.goods.append(good)
            db.session.commit()
            return redirect("/books")

    goods = Goods.query.filter(Goods.type == "books").all()
    return render_template("all_goods.html",
                            title = "Books",
                            goods = goods,
                            number_cart = number_cart
                            )

@app.route("/drinks", methods=['POST', 'GET'])
def drinks():
    username = request.cookies.get("username")
    number_cart = 0
    if username == '' or username == None:
        number_cart = 0
    else:
        cart = User.query.filter(User.username == username).first().goods
        for i in cart:
            number_cart += 1
    if request.method == "POST":
        if username == '':
            flash("Haven't Login!!")
        else:
            user = User.query.filter(User.username == username).first()
            id = request.form.get("good_id")
            good = Goods.query.get(id)
            user.goods.append(good)
            db.session.commit()
            return redirect("/drinks")

    goods = Goods.query.filter(Goods.type == "drinks").all()
    return render_template("all_goods.html",
                            title = "Drinks",
                            goods = goods,
                            number_cart = number_cart
                            )

@app.route("/furniture", methods=['POST', 'GET'])
def furniture():
    username = request.cookies.get("username")
    number_cart = 0
    if username == '' or username == None:
        number_cart = 0
    else:
        cart = User.query.filter(User.username == username).first().goods
        for i in cart:
            number_cart += 1
    if request.method == "POST":
        if username == '':
            flash("Haven't Login!!")
        else:
            user = User.query.filter(User.username == username).first()
            id = request.form.get("good_id")
            good = Goods.query.get(id)
            user.goods.append(good)
            db.session.commit()
            return redirect("/furniture")

    goods = Goods.query.filter(Goods.type == "furniture").all()
    return render_template("all_goods.html",
                            title = "Furniture",
                            goods = goods,
                            number_cart = number_cart
                            )

@app.route("/toys", methods=['POST', 'GET'])
def toys():
    username = request.cookies.get("username")
    number_cart = 0
    if username == '' or username == None:
        number_cart = 0
    else:
        cart = User.query.filter(User.username == username).first().goods
        for i in cart:
            number_cart += 1
    if request.method == "POST":
        if username == '':
            flash("Haven't Login!!")
        else:
            user = User.query.filter(User.username == username).first()
            id = request.form.get("good_id")
            good = Goods.query.get(id)
            user.goods.append(good)
            db.session.commit()
            return redirect("/toys")
            
    goods = Goods.query.filter(Goods.type == "toys").all()
    return render_template("all_goods.html",
                            title = "Toys",
                            goods = goods,
                            number_cart = number_cart
                            )
                            
@app.route("/shopping_cart", methods=['POST', 'GET'])
def shopping_cart():
    username = request.cookies.get("username")
    number_cart = 0
    goods = []
    addresses = []
    if username == '' or username == None:
        number_cart = 0
    else:
        cart = User.query.filter(User.username == username).first().goods
        for i in cart:
            number_cart += 1
        goods = User.query.filter(User.username == username).first().goods
        user= User.query.filter(User.username == username).first()
        addresses = Address.query.filter(Address.user == user.userId).all()
        if request.method == "POST":
            if "pay" in request.form:
                goods = User.query.filter(User.username == username).first().goods
                order = Order(user = username)
                for good in reversed(goods):
                    order.goods.append(good)
                    user.goods.remove(good)
                db.session.add(order)
                db.session.commit()
            if 'id' in request.form:
                id = request.form.get("id")
                good = Goods.query.filter(Goods.goodsId == id).first()
                user.goods.remove(good)
                db.session.commit()
            return redirect("/order")
    return render_template("shopping-cart.html",
                            title = "Shopping cart",
                            goods = goods,
                            username = username,
                            addresses = addresses,
                            number_cart = number_cart
                            )

@app.route("/search_page")
def search_page():
    username = request.cookies.get("username")
    number_cart = 0
    if username == '' or username == None:
        number_cart = 0
    else:
        cart = User.query.filter(User.username == username).first().goods
        for i in cart:
            number_cart += 1
    return render_template("searchpage.html",
                            title = "Search Page",
                            number_cart = number_cart
                            )
                
@app.route("/order")
def order():
    username = request.cookies.get("username")
    number_cart = 0
    if username == '' or username == None:
        number_cart = 0
    else:
        cart = User.query.filter(User.username == username).first().goods
        for i in cart:
            number_cart += 1
    orders = Order.query.filter(Order.user == username).all()
    return render_template("order.html",
                            title = "Search Page",
                            number_cart = number_cart,
                            username = username,
                            orders = orders
                            )        
        
        
        

