'''
	This is the default state to render .md files and
	push through a Jinja template. More to be added.
'''
from flask import Flask, render_template
from flask_flatpages import FlatPages

DEBUG = True
FLATPAGES_EXTENSION = '.md'

app = Flask(__name__)
pages = FlatPages(app)
app.config.from_object(__name__)

@app.route('/')
def index():
	return 'Index'

#Not related to /profile/<path:name>
@app.route('/pages/<path:name>')
def page(name):
	page = pages.get_or_404(name)
	return render_template('page.html', page=page)

if __name__ == "__main__":
	app.run(debug=True)