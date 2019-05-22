from flask import Flask, request, render_template,redirect
import cgi
import os
import re

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too

page_header = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-5" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta http-equiv="X-UA-Compatible" content="ie=edge" />
    <title>Validation Example</title>
    <link rel="stylesheet" href="/static/app.css" />
  </head>
  <body>
"""

welcomeMessage = """
<h1>Welcome to my super cool page!</h1>
<a href="/signup">Register</a> """


page_footer = """
 </body>
</html>
"""

# a registration form
register_form = """
<form action="/signup" id="form" method="POST">
      <h1>Register</h1>
      <label for="username">Username </label>
      <input type="text" name="username" id="username" value="{username}" />
      <p class="error">{usernameError}</p>
      <label for="password">Password </label>
      <input type="password" name="password" id="password" value="{password}" />
      <p class="error">{passwordError}</p>
      <label for="password">Verify Password </label>
      <input type="password" name="verify_password" id="verify_password" value="{verify_password}" />
      <p class="error">{verify_passwordError}</p>
      <label for="email">Email(optional)</label>
      <input type="text" name="email" id="email" value="{email}"/>
      <p class="error">{emailError}</p>
      <button type="submit">Register</button>
    </form>
"""
@app.route('/signup')
def signup():
    return register_form.format(username = '', password='', verify_password='', email='', usernameError = '',
             passwordError = '', verify_passwordError = '', emailError='' )

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
    '''else:
        hasNumber = False
        for char in password:
            if char.isdigit():
                hasNumber = True
        if not hasNumber:
            passwordError = "Password must contain a number"'''
    if verify_password == "" or verify_password != password:
        verify_passwordError = "Password do not match. Please try again."
        verify_password = ""
    if email != "":
        if not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-]+\.[a-zA-Z0-9-.]+$)", email):
            emailError = "Not a valid email address."
    

    if usernameError or passwordError or verify_passwordError or emailError :
        return register_form.format(username, usernameError, 
        password, passwordError, verify_password, verify_passwordError, email, emailError)
        '''print("there was an error!")
        content = page_header + register_form.format(username, usernameError, 
        password, passwordError, verify_password, verify_passwordError, email, emailError) + page_footer
        return content'''
    return "Welcome, " + username


@app.route("/")
def index():
    # build the response string
    content = page_header + welcomeMessage + page_footer
    return content

@app.route("/signup", methods=['GET'])
def register_page():
    # build the response string
    content = page_header + register_form.format("", "", "", "", "", "","","") + page_footer
    return content

app.run()
