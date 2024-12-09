# TABLE OF CONTENTS

## I. Introduction

## II. Django Detail

## III. ER diagram

## IV. DFD (Data Flow Diagram

## V. Conclusion 
<br>

## 1.Introduction

The Online Food Delivery Website is designed to provide
a seamless and user-friendly platform for customers to
order food online. This platform allows users to browse
through a variety of food menus, place orders from
different categories, and make payments directly from
their devices. It aims to enhance the convenience and
speed of food ordering while offering a comprehensive
solution to manage customer orders.
This project is built using HTML, CSS, JavaScript,
Django, and Bootstrap to ensure an interactive and
responsive web experience. The website features a wellstructured architecture that supports multiple sections
including Home, Menu, Order, About, and Contact Us.
The Order section is further categorized into different
regional cuisines such as South Indian, North Indian, and
Bengali, offering a diverse range of food choices.
The system is designed with both users and administrators
in mind. Users can easily navigate the site, make food
selections, place orders, and get in touch with customer
support. Administrators have the ability to manage user
orders and update the menu to ensure a dynamic and upto-date offering.
The goal of this project is to provide a platform that
simplifies the food ordering process, making it efficient
and accessible for all users, while also allowing
administrators to maintain and enhance the overall user
experience.



### 2.What is Django?

Django is a high-level Python web framework that
enables developers to build robust, scalable, and secure
web applications quickly. It follows the Model-ViewTemplate (MVT) architectural pattern, which organizes
the development process efficiently. Django is known for
its "batteries-included" approach, meaning it comes with
built-in features such as an ORM (Object-Relational
Mapping), user authentication, form handling, and more.

### 2.1 Key Features of Django:

 Fast Development: It allows rapid
development of web applications.

 Security: Protects against common web
vulnerabilities like SQL injection, cross-site
scripting (XSS), and cross-site request
forgery (CSRF).

 Scalability: Suitable for projects ranging
from simple websites to large-scale
applications.

 Built-in Admin Interface: Django provides
an auto-generated admin panel to manage
your application data.

## 2.2 Creating a Virtual Environment in
Django?

### 2.2.1 What is a Virtual Environment?

A virtual environment is an isolated environment in
Python that allows you to install and manage
dependencies (libraries, packages) for a specific project
without affecting the global Python installation. It ensures
that different projects can have different versions of
dependencies.

### 2.2.2 Steps to Create and Activate a Virtual
Environment

I. Install virtual env (if not installed): Open
your terminal or command prompt and type:
i. ‘py -m venv myM’ (here my virtual
name is myM)

II. Activate the Virtual Environment:
i. ‘myM\Scripts\activate’

### 2.2.3 What Changes Does a Virtual
Environment Make?

I. Environment Isolation: When activated,
Python and pip commands use the local (isolated)
environment instead of the global one.

II. Custom pip Package Directory:
Dependencies are installed in the venv folder
instead of the global system.

III. Environment-Specific python and pip:
Activating the virtual environment overrides the
system’s Python and pip paths.

## 2.3 Installing Django Using pip

After creating and activating a virtual environment, the
next step is to install Django. This is done using Python's
package manager, pip.

### 2.3.1 What is pip?
pip stands for "Pip Installs Packages" and is a tool used to install
and manage Python libraries and frameworks.

## 2.4 Steps to Install Django:

1. Ensure the Virtual Environment is
Activated: Before installing Django, ensure you
have activated the virtual environment. The terminal
prompt will show the name of the virtual environment
(e.g., (myM)).

2. Run the Installation Command: Use the
following command to install Django:
“pip install Django”

## 2.5 Creating a Django Project
Once Django is installed, the next step is to create a new
Django project. A project serves as the container for your
web application and manages settings, URLs, and overall
configuration.

### 2.5.1 Command to Create a Project:
To create a Django project, use the Django-admin
command as follows:
‘django-admin startproject meal’

### 2.5.2 What Happens After Running This
Command?
When you run django-admin startproject meal, Django
creates the following directory structure:

# Explanation of Files and Folders:
 
meal/ (Outer Folder): This is the root folder of your project.
It contains all the files related to your Django project.
manage.py:
A Python script used to manage the project.
You can use it to run the server, create apps, and execute other management tasks.

meal/ (Inner Folder):
This folder contains the core settings and configurations for your Django project.
Files inside the inner meal/ folder:

__init__.py:
Indicates that this directory is a Python package.

settings.py:
Contains all the project settings, such as database configuration, middleware,
installed apps, etc.

urls.py:
Maps URLs to views. This is where you define the URL patterns for your project.

asgi.py:
Stands for Asynchronous Server Gateway Interface.
Used for handling asynchronous web requests.

wsgi.py:
Stands for Web Server Gateway Interface.
Used to deploy the application on a production server.

## 2.6 Navigating to the Project Folder

After creating the project, navigate to the outer folder (meal) to start working on
your project. Use the following commands:
‘cd meal’

## 2.7 Starting the Django Development Server

Once your Django project is set up, you can run a development server to test
your application locally. Use the following command:
‘py manage.py runserver’.
The command launches a lightweight server for development purposes. By
default, the server runs on http://127.0.0.1:8000/ (localhost, port 8000).

#### 2.7.1 How to Access the Server?

Open your web browser and visit:
‘http://127.0.0.1:8000/’
You’ll see Django's default welcome page, confirming the server is running.

## 2.8 Creating a Django App
 
In Django, an app is a modular component that handles specific functionality of
your project. For example, in your project meal, you might have an app for
handling orders. To create an app, use the following command:
‘python manage.py startapp orderr’

 2.8.1 What Happens After Running This Command?
 
Django creates a folder named orderr with the following structure:
Explanation of the Files and Folders:

1. orderr/ (App Folder):
 The root folder of your app containing all the files specific to this app.

3. Files in orderr/:
   
 __init__.py:
o Indicates that this directory is a Python package.

 admin.py:
o Used to register models so they can be managed via Django’s
admin interface.

 apps.py:
o Contains app configuration settings.

 models.py:
o Used to define the database schema by creating models.

 tests.py:
o Contains test cases for the app.

 views.py:
o Defines the logic for processing requests and returning responses.

5. migrations/:
   
 A folder to store migration files, which track database schema changes.

 __init__.py:
o Indicates that this is a Python package.

### 2.8.2 After creating the app, you need to:

Add the App to the Project:

 Open settings.py in your project folder.

 Add 'orderr', to the INSTALLED_APPS list.

## 2.9 Creating the template Folder:

 In your Django app (order), you created a folder named template.

 This folder is where you store all your HTML files, which define the
structure and content of your website’s pages.

2.9.1 Adding HTML Files in the template Folder:

1. home.html: The main landing page of your website.

2. menu.html: The page that shows the menu with the food items available
for order.

3. about.html: This page provides information about your website and the
services offered.

4. contact1.html: Contains a contact form where users can submit their
details or queries.

5. order.html: A page where users can place orders for food. This page has an
option for users to place their orders.

## 2.10 Django Views

When we create a new app (order), the views.py file contains only:
 ‘from django.shortcuts import render’

2.10.1 What You Need to Add:

For your Online Food Delivery website (meal1 project, orderr app), we added:

 Additional Imports:

 HttpResponse: For sending plain text or basic responses.

 redirect: To navigate users to a different page.

 User: To manage user accounts (e.g., create a user).

 authenticate, login, logout: To handle user authentication (if needed
later).

 Functions for Web Pages:

 aboutpage, io1page, style2page, orderpage, menupage:
o These functions render specific HTML templates like about.html,
menu.html, etc.

 contactpage:
o Handles a form submission (POST) to create a user and redirects to
the style2 page.
o If it's a GET request, it shows the contact1.html template.

#### 2.10.2 The views in your Online Food Delivery website
handle the logic for rendering templates and processing
user input. Here's a brief explanation of the views:

1. aboutpage(request):
Renders the about.html template.
Displays information about your website.

2. io1page(request):
Renders the io1.html template.
Likely displays a specific section or feature of your website.

3. style2page(request):
Renders the style2.html template.
Likely used for styling or specific content.

4. orderpage(request):
Renders the order.html template.
Allows users to place food orders.

5. menupage(request):
Renders the menu.html template.
Displays the food menu for users.

6. contactpage(request):
Handles contact form submissions:
POST Request: Captures the user's name and email from the form.
Creates a new user using Django’s User model (User.objects.create_user).
Saves the user to the database and redirects to the style2.html page.
GET Request: Renders the contact1.html template to display the contact form.

## 2.11 Meal1(website) URLs

In Django, before we can use certain functionality like working with the admin
site or routing URLs, we need to import specific modules and classes. These
imports are essential to make the features of Django available in your project.

2.11.1 

Here's how we write the imports, step-by-step:

 ‘from django.contrib import admin’

 This line allows you to use Django's built-in admin interface, which is a
powerful tool for managing your site’s data.

 You don't need to write code for managing your models manually, as
the admin interface provides an easy-to-use dashboard.

 ‘from django.urls import path’

 This is essential for URL routing. It allows you to create and manage
the paths (URLs) for your website. By using the path() function, you
can associate specific URLs (like /order/ or /menu/) with
corresponding views (functions that display pages or handle data).

 Without this import, Django wouldn't know how to handle incoming
web requests based on their URLs.

 ‘from order import views’

 In Django, views are the Python functions that handle user
requests and return a response (usually a webpage). By
importing views from the order app, you're able to link
specific URLs to the views that should be triggered when
those URLs are visited.

 For example, views.aboutpage will be used to display the
"about" page when the /about/ URL is accessed.

## 2.12 Make Migrations

In Django, migrations are how Django tracks changes to
your database schema (like adding, modifying, or deleting
models). When you make any changes to your models (like
adding new fields, creating new models, or changing
existing ones), Django needs to know about those changes
to update the database accordingly.
To achieve this, you use the makemigrations command. This
command tells Django to prepare migration files that
describe the changes to your models. It doesn’t actually
apply those changes to the database — it just prepares the
necessary files.

2.12.1 Steps for migration

 ‘python manage.py makemigrations’

Django will look at your models.py file, detect that you've
added a new field (description), and generate a migration
file in the migrations folder of your app.

 ‘python manage.py migrate’

This will apply all the pending migrations (including the one
that adds the description field) to the database, so your
database schema matches your updated models.

## 2.13 Create Superuser

 Run the following command to start the process of creating a
superuser:
‘python manage.py createsuperuser’

 Provide the Superuser Information: The system will ask you
for the following details:

o Username: The username of the superuser (e.g., admin).

o Email: The email address for the superuser

o Password: A strong password for the superuser.

 Confirmation: Once you’ve entered the information and
confirmed the password, Django will create the superuser and
provide a confirmation message like this:
‘Superuser created successfully’
This means the superuser has been created, and you can now log
into the Django Admin.

# 2.14

Logging into the Admin Site
Now that you’ve created a superuser, you can access the Django

admin site:

Step 1: Run the Django Development Server: If the server
is not already running, you need to start it with the following
command:
‘python manage.py runserver’

Step 2: 

Visit the Admin Site: Open your web browser and go
to the following URL to access the Django admin interface:
‘http://127.0.0.1:8000/admin/’

Step 3: 

Log in: Enter the username and password that you used
when creating the superuser. This will give you access to the
Django admin dashboard.

Example Code and Command Flow:

Here’s an example of how the command flow will look like when
you run createsuperuser:

### 3. ER Diagram Representation

Here is a simplified ER (Entity Relationship) diagram representing the
structure of your online food delivery website. Here's what it
illustrates:

1. Home: Central hub linking to Menu, Order, and other pages like About
and Contact Us.

2. Menu: Connects to the Order section, which includes food items.

3. Order: Contains Food Item and Order Details, representing the food
chosen by customers and the order specifics.

4. About: Linked to the Home page for informational purposes.

5. Contact Us: Linked to both Home and User, indicating that users can
contact through this section.

### 4.DFD Diagram
A data flow diagram (DFD) is a visual representation of how
data flows through a system, illustrating the movement of
information between various components or processes. In
essence, it maps out the paths data takes within the system,
from its source to its destination, highlighting the interactions
between different entities.

External Entities: User and Restaurant

Processes:

I. Registration or Login

II. Menu Browsing

III. Placing Order

IV. Payment

V. Order Confirmation

VI. Order Processing

VII. Delivery Assigned

VIII. Delivery Tracking

IX. Feedback

Data Stores:

I. User Database

II. Restaurant Database

III. Payment Gateway

IV. Order Confirmation Database

V. Delivery Status Database

Data Flows:

I. User Registration/Login Process:
Data Flow: User inputs (username, password) -> User Database

II. Menu Browsing Process:
Data Flow: Request for menus -> Restaurant Database

III. Placing Order Process:
Data Flow: Selected items -> Order Processing

IV. Payment Process:
Data Flow: Payment details -> Payment Gateway

V. Order Confirmation Process:
Data Flow: Confirmation details -> Order Confirmation Database

## 5. Conclusion

The Online Food Delivery Website provides a robust and intuitive platform for
users to explore and order food from various cuisines, offering a convenient and
efficient user experience. With features like easy navigation, a dynamic menu, a
smooth ordering process, and a responsive design, this website is designed to
meet the needs of both customers and administrators.
The integration of technologies such as Django, Bootstrap, and JavaScript
ensures a seamless performance across all devices. The system's backend
supports features like order management, user authentication, and contact forms
for customer support, while the frontend is tailored to be user-friendly and
aesthetically pleasing.
