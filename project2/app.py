# Import required libraries and modules
from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json

def inject_datetime():
    return {'datetime': datetime}

# Initialize the Flask application
app = Flask(__name__)

# Configure database URI and other settings
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:hrs7453377@localhost/ecommerce'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'secret'

# Initialize SQLAlchemy with the Flask app
db = SQLAlchemy(app)

# Define the User model/table
class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    orders = db.relationship('Order', backref='user', lazy=True)

    # ... (password property and check_password method) ...

# Define the Product model/table
class Product(db.Model):
    __tablename__ = 'products'
    product_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Numeric(10, 2), nullable=False)
    image_filename = db.Column(db.String(255))
    price_details = db.Column(db.Text)
    category = db.Column(db.String(50), nullable=False)
    
# Define the Order model/table
class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    total_amount = db.Column(db.Numeric(10, 2), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    def set_items(self, item_list):
        self.items = json.dumps(item_list)

    def get_items(self):
        return json.loads(self.items) if self.items else []
    
# Home page that displays all unique product categories
@app.route('/')
def index():
    categories = list(set([p.category for p in Product.query.all()]))
    return render_template('index.html', categories=categories)

# Page that shows products under a specific category
@app.route('/category/<string:category>')
def show_category(category):
    products = Product.query.filter_by(category=category).all()
    return render_template('category.html', products=products, category=category)

# Add a product to the shopping cart
@app.route('/add_to_cart/<int:product_id>', methods=['GET'])
def add_to_cart(product_id):
    quantity = int(request.args.get(f'quantity_{product_id}', 1))
    cart = session.get('cart', {})
    cart[str(product_id)] = cart.get(str(product_id), 0) + quantity
    session['cart'] = cart
    return redirect(url_for('cart'))

# Display the shopping cart with totals and fees
@app.route('/cart')
def cart():
    cart_data = session.get('cart', {})
    total = 0
    cart_items = []
    for pid_str, qty in cart_data.items():
        pid = int(pid_str)
        product = Product.query.get(pid)  # Assuming 'Product' is your model
        if product:
            total += product.price * qty
            cart_items.append({'product': product, 'quantity': qty})
        else:
            print(f"Warning: Product with ID {pid} not found.")
            # Optionally remove from cart:
            # del cart_data[pid_str]
            # session['cart'] = cart_data
    return render_template('cart.html', cart_items=cart_items, total=total)

# Remove an item from the shopping cart
@app.route('/remove_from_cart/<int:product_id>')
def remove_from_cart(product_id):
    cart = session.get('cart', {})
    cart.pop(str(product_id), None)
    session['cart'] = cart
    return redirect(url_for('cart'))

# User registration form and logic
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        if User.query.filter_by(username=request.form['username']).first() or User.query.filter_by(email=request.form['email']).first():
            flash("Username or Email already taken.")
            return redirect(url_for('register'))

        user = User(
            first_name=request.form['first_name'],
            last_name=request.form['last_name'],
            username=request.form['username'],
            password=request.form['password'],  # Setting plain text password
            email=request.form['email'],
            address=request.form['address']
        )
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html')

# User login form and logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form['username'], password=request.form['password']).first()
        if user:
            session['user_id'] = user.user_id
            return redirect(url_for('checkout'))
        flash("Invalid credentials")
    return render_template('login.html')

# Checkout page that displays the cart and allows order submission

# Checkout page that displays the cart and allows order submission
@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    cart = session.get('cart', {})
    items = []
    total = decimal.Decimal('0.00')
    for pid_str, qty in cart.items():
        product = Product.query.get(int(pid_str))
        if product:
            items.append({
                'id': product.product_id,
                'name': product.name,
                'quantity': qty,
                'price': product.price
            })
            total += product.price * qty
        else:
            print(f"Warning: Product with ID {pid_str} not found.")

    tax_rate = decimal.Decimal('0.1')
    tax = round(total * tax_rate, 2)
    shipping = decimal.Decimal('5.00')
    grand_total = total + tax + shipping

    if request.method == 'POST':
        user_id = session['user_id']
        new_order = Order(user_id=user_id, total_amount=grand_total)
        # If you were storing items as JSON:
        # new_order.items = json.dumps([{'product_id': item['id'], 'name': item['name'], 'quantity': item['quantity'], 'price': float(item['price'])} for item in items])

        db.session.add(new_order)
        db.session.commit()
        order_id = new_order.id
        session['cart'] = {}  # Clear the cart
        return redirect(url_for('order_complete', order_id=order_id))

    return render_template('checkout.html', items=items, total=total, tax=tax, shipping=shipping, grand_total=grand_total)
import decimal  # Make sure to import the decimal module at the top of your file 

# Confirmation page after order submission
@app.route('/order_complete/<int:order_id>')
def order_complete(order_id):
    return render_template('order_complete.html', order_id=order_id)

@app.route('/logout')
def logout():
    session.pop('user_id', None)  # Remove the user ID from the session
    flash('You have been logged out.')
    return redirect(url_for('index')) # Redirect to the homepage after logout

# Run the app and create tables
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)