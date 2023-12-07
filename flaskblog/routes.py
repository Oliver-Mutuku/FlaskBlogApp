from flask import render_template, url_for, flash, redirect
from flaskblog.models import User, Post
from flaskblog.forms import RegistrationForm, LogInForm
from flaskblog import app


posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First Post content',
        'date_posted': 'April 20, 2018'
    },

    {
        'author': 'john Doe',
        'title': 'Blog Post 2',
        'content': 'Second Post content',
        'date_posted': 'April 21, 2018'
    }

]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title="About")


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()     # To create an instance of our form, don't forget the parentheses
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LogInForm()
    if form.validate_on_submit():
        if form.email.data == "admin@blog.com" and form.password.data == 'password':
            flash(f'You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash(f'Login unsuccessful. Please check email and password.', 'danger')
    return render_template('login.html', title='Login', form=form)
