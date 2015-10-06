from Eliza import app
from flask import render_template
from flask import Markup

@app.route('/')
def index():
	return 'Index'

#<path: allows slashes
#path> is the actual route
@app.route('/pages/<path:path>')
def page(path):
	return render_template('page.html', title='testTitle',
										content='testContent')