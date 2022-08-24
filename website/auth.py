from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return render_template("logout.html")
    
@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        if len(email) < 4:
            flash('Email should have more than 3 characters.', category='error')
        elif len(firstName)< 2:
            flash('Name should have more than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords must match!', category='error')
        elif len(password1) <7:
            flash('Password must have at least 7 characters.', category='error')
        else:
            flash('Account created!', category='success')
            pass
    return render_template("signup.html")

