from flask import render_template
from app import app

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
	return render_template('index.html', title = 'Home', user1 = user, posts = posts )
	#return " <H1> Hello " + user['username'] + " !! </H1>"
