from flask import render_template
from app import app

#Views
@app.route('/news/<int:news_id>')
def index():

    '''Veiw root page function that returns the index page and its data'''
    title= 'Home to the best News Review Website Online'
    return render_template('index.html',title = title)