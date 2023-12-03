from flask import Flask, render_template, url_for, flash, redirect
app = Flask(__name__)
from forms import RegistrationForm, LogInForm
from email_validator import validate_email, EmailNotValidError

app.config['SECRET_KEY'] = '4a95a87d5b0f3af5855f9cc161de54f2'


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


if __name__ == "__main__":
    app.run(debug=True)
