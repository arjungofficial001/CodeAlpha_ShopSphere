# ShopSphere 🛍️

A simple full-stack e-commerce web application developed as part of the **CodeAlpha Full Stack Development Internship – Task 1**.

ShopSphere allows customers to browse products, search for products, view product details, manage a shopping cart, create an account, place orders, and view their order history.

---

## 📌 Project Overview

**ShopSphere** is a Django-based e-commerce application designed to demonstrate the fundamentals of full-stack web development.

The application includes:

* Product listing and search
* Product details
* Shopping cart management
* User registration and authentication
* Checkout and order processing
* Stock management
* Customer order history
* Django administration panel
* Responsive user interface

---

## ✨ Features

### 🛍️ Product Management

* Display available products
* Product categories
* Product descriptions
* Product pricing
* Product stock availability
* Product detail pages
* Product search
* Optional product images

### 🛒 Shopping Cart

* Add products to cart
* Increase product quantity
* Decrease product quantity
* Remove products from cart
* Automatic total calculation
* Stock-limit validation
* Empty-cart handling

### 👤 User Authentication

* User registration
* User login
* User logout
* Secure password handling through Django authentication
* Login-protected checkout
* Login-protected order history

### 📦 Order Processing

* Checkout page
* Order summary
* Shipping address collection
* Order creation
* Order item creation
* Automatic stock reduction
* Order status management
* Order confirmation page
* Customer order history

### ⚙️ Admin Panel

Django's built-in administration panel allows administrators to manage:

* Products
* Users
* Orders
* Order items
* Product stock
* Order status

### 🔎 Product Search

Users can search products by:

* Product name
* Product category

### 📱 Responsive Design

The interface is designed to work across:

* Desktop
* Laptop
* Tablet
* Mobile devices

---

## 🛠️ Technologies Used

### Frontend

* HTML5
* CSS3
* JavaScript

### Backend

* Python
* Django

### Database

* SQLite

### Development Tools

* Visual Studio Code
* Git
* GitHub

---

## 📁 Project Structure

```text
ShopSphere/
│
├── config/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── store/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── tests.py
│
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── product_detail.html
│   ├── cart.html
│   ├── login.html
│   ├── register.html
│   ├── checkout.html
│   ├── order_success.html
│   └── my_orders.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   │
│   └── js/
│       └── script.js
│
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

# ⚙️ Installation & Setup

Follow the steps below to run ShopSphere on a Windows computer.

## 1. Prerequisites

Install the following software before starting:

* **Python 3.11 or newer**
* **Git**
* **Visual Studio Code** (recommended)

Verify Python:

```powershell
python --version
```

Verify Git:

```powershell
git --version
```

---

## 2. Clone the Repository

Open **PowerShell** or **Command Prompt**.

Navigate to the location where you want to store the project.

Example:

```powershell
cd C:\Users\YourName\Desktop
```

Clone the repository:

```powershell
git clone https://github.com/YOUR-USERNAME/CodeAlpha_ShopSphere.git
```

Enter the project directory:

```powershell
cd CodeAlpha_ShopSphere
```

---

## 3. Open the Project in Visual Studio Code

Run:

```powershell
code .
```

If the `code` command is unavailable, open Visual Studio Code manually and select:

**File → Open Folder → CodeAlpha_ShopSphere**

---

## 4. Create a Virtual Environment

Create a Python virtual environment:

```powershell
python -m venv venv
```

This creates a separate environment for the project's Python dependencies.

---

## 5. Activate the Virtual Environment

For Windows PowerShell:

```powershell
venv\Scripts\Activate.ps1
```

After activation, the terminal should display something similar to:

```text
(venv) PS C:\Users\YourName\Desktop\CodeAlpha_ShopSphere>
```

For Windows Command Prompt:

```cmd
venv\Scripts\activate.bat
```

---

## 6. Install Dependencies

Make sure the virtual environment is activated.

Then run:

```powershell
pip install -r requirements.txt
```

The required Django version and other project dependencies will be installed automatically.

---

## 7. Apply Database Migrations

ShopSphere uses SQLite as its database.

Run:

```powershell
python manage.py migrate
```

This creates the required database tables.

---

## 8. Create an Administrator Account

Create a Django administrator account:

```powershell
python manage.py createsuperuser
```

Django will ask for:

```text
Username:
Email address:
Password:
Password (again):
```

The password will not be displayed while typing. This is normal.

---

## 9. Start the Development Server

Run:

```powershell
python manage.py runserver
```

You should see a message similar to:

```text
Starting development server at http://127.0.0.1:8000/
```

Open the application in your browser:

```text
http://127.0.0.1:8000/
```

---

# 🔐 Admin Panel

The Django administration panel is available at:

```text
http://127.0.0.1:8000/admin/
```

Log in using the administrator account created during installation.

From the admin panel, administrators can manage:

* Products
* Users
* Orders
* Order Items
* Stock
* Order Status

---

# ➕ Adding Products

After logging into the admin panel:

**Products → Add Product**

Enter:

* Product Name
* Description
* Price
* Stock
* Category
* Optional Image URL

Click **Save**.

The product will then appear on the ShopSphere homepage.

---

# 🛒 Application Flow

The main customer workflow is:

```text
Homepage
    ↓
Browse Products
    ↓
Search Products
    ↓
View Product Details
    ↓
Add to Cart
    ↓
Manage Cart Quantity
    ↓
Login / Register
    ↓
Checkout
    ↓
Enter Shipping Address
    ↓
Place Order
    ↓
Order Confirmation
    ↓
My Orders
```

---

# 🗄️ Database Models

ShopSphere uses three main application models.

## Product

Stores information about products.

Fields include:

* Name
* Description
* Price
* Image
* Stock
* Category
* Creation date

---

## Order

Stores customer order information.

Fields include:

* Customer
* Total amount
* Order status
* Shipping address
* Creation date

---

## OrderItem

Stores individual products included in an order.

Fields include:

* Order
* Product
* Quantity
* Purchase price

---

# 🔒 Security

ShopSphere uses Django's built-in security and authentication functionality.

The application includes:

* Django authentication
* Password hashing
* CSRF protection
* Login-protected checkout
* Login-protected order history
* Server-side stock validation
* Database transaction handling during order creation

---

# 💻 Main Pages

| Page            | Description                                     |
| --------------- | ----------------------------------------------- |
| Home            | Displays products and product search            |
| Product Details | Displays detailed information about a product   |
| Cart            | Manages selected products and quantities        |
| Register        | Creates a customer account                      |
| Login           | Authenticates existing customers                |
| Checkout        | Collects shipping information and places orders |
| Order Success   | Displays successful order confirmation          |
| My Orders       | Displays the customer's previous orders         |
| Admin           | Manages products, users and orders              |

---

# 🧪 Testing the Application

After starting the development server, use the following flow to test the application.

### Test 1 – Products

1. Open the homepage.
2. Confirm products are displayed.
3. Search for a product.
4. Open a product's details page.

### Test 2 – Shopping Cart

1. Add a product to the cart.
2. Open the cart.
3. Increase the quantity.
4. Decrease the quantity.
5. Remove the product.
6. Confirm the cart total updates correctly.

### Test 3 – User Authentication

1. Open Register.
2. Create a new account.
3. Confirm the user is logged in.
4. Log out.
5. Log back in using the same account.

### Test 4 – Checkout

1. Add a product to the cart.
2. Open Checkout.
3. Enter a shipping address.
4. Place the order.
5. Confirm the order success page appears.

### Test 5 – My Orders

1. Open **My Orders**.
2. Confirm the newly created order is displayed.
3. Check the order number, products, quantity, total and status.

### Test 6 – Admin

1. Open the Django admin panel.
2. Log in as an administrator.
3. Check the Products section.
4. Check the Orders section.
5. Change an order status if required.

---

# 📱 Responsive Design

The frontend includes responsive layouts for different screen sizes.

The application adapts to:

* Desktop screens
* Laptop screens
* Tablets
* Mobile phones

---

# 🎓 CodeAlpha Internship

This project was developed as:

**Task 1 – Simple E-commerce Store**

for the:

**CodeAlpha Full Stack Development Internship**

The project demonstrates full-stack development using:

**HTML + CSS + JavaScript + Django + SQLite**

---

# 👨‍💻 Developer

**Arjun**

Developed for the CodeAlpha Full Stack Development Internship.

---

# 📄 License

This project was created for educational and internship purposes.
