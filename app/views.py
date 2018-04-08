from flask import render_template
from app import app
from .request import get_newss


#Views
@app.route('/')
def index():

    '''Veiw root page function that returns the index page and its data'''

    #Getting popular News
    popular_news = get_newss('popular')
    upcoming_news = get_newss('upcoming')
    now_showing_news = get_newss('now_showing')
    title= 'Home -Welcome to the best News Review Website Online'
    return render_template('index.html', title = title, popular = popular_news, upcoming = upcoming_news, now_showing = now_showing_news)