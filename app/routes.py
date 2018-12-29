from flask import render_template
from app import app
from app.forms import LoginForm
from flask import render_template, flash, redirect

@app.route('/')
@app.route('/index')
def index():
	user = {'username': 'Arjit'}
	posts = [ 
	    {
	        'author': {'username': 'John'},
	        'body': 'Its beatuiful Life'
	    },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }	
	]
	return render_template('index.html', title = 'Home', user = user, posts = posts )
	#return " <H1> Hello " + user['username'] + " !! </H1>"

@app.route('/login', methods = ['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
		return redirect('/index')
	return render_template('login.html', title='Sign In', form=form)