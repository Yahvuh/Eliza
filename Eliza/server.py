'''
	This is the default state to render .md files and
	push through a Jinja template. More to be added.
'''
from flask import Flask, render_template
from flask_flatpages import FlatPages

DEBUG = True
#Defaults to /pages, so now /Eliza is root
FLATPAGES_ROOT = '.'
FLATPAGES_EXTENSION = '.md'

app = Flask(__name__)
item = FlatPages(app)
app.config.from_object(__name__)

@app.route('/')
def index():
	return 'Index'

#Look at this hack
@app.route('/<path:folderPath>/<path:filePath>')
def page(folderPath, filePath):
	page = item.get_or_404(folderPath + '/' + filePath)
	return render_template('page.html', page=page)

@app.route('/<path:folderPath>/<path:filePath>')
def profile():
	profile = item.get_or_404(folderPath + '/' + filePath)
	return render_template('profile.html', profile=profile)

if __name__ == "__main__":
	app.run(debug=True)