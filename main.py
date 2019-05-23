from flask import Flask, request, render_template,redirect
import cgi
import os
import jinja2
import re

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja2_env = jinja2.Environment(loader = jinja2.FileSystemLoader
(template_dir), autoescape=True)

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too

@app.route('/signup')
def signup():
    template = jinja2_env.get_template('signup.html')
    return template.render()

@app.route('/signup', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify_password']
    email = request.form['email']

    usernameError = ''
    passwordError = ''
    verify_passwordError =''
    emailError = ''
    emailError = ''

    if username == "":
        usernameError = "Please enter a valid username."
    elif len(username) <= 3 or len(username) > 20:
        usernameError = ""
    elif " " in username:
        usernameError = "Your username cannot contain any spaces."
        username = ""

    if password == "":
        passwordError = "Please enter a valid password."
    elif len(password) < 3 or len(password) > 20:
        passwordError = "Password must be at least 3 to 20 characters long."
    elif " " in password:
        passwordError = "Your cannot contain any spaces"
    
    if verify_password == "" or verify_password != password:
        verify_passwordError = "Password do not match. Please try again."
        verify_password = ""
    if email != "":
        if not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-]+\.[a-zA-Z0-9-.]+$)", email):
            emailError = "Not a valid email address."
    

    if usernameError or passwordError or verify_passwordError or emailError :
        template = jinja2_env.get_template('signup.html')
        return template.render(username=username, usernameError=usernameError, 
        password=password, passwordError=passwordError, verify_password=verify_password, 
        verify_passwordError=verify_passwordError, email=email, emailError=emailError)

    template = jinja2_env.get_template('Welcome.html')
    return template.render(username=username)
app.run()
