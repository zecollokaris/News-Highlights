from flask import render_template
from .config import DevConfig
from app import app

from .request import get_newss
from .request import get_newss,get_news


#Views
@app.route('/news/<int:id>')
def news():

    '''Veiw news page function that returns the news details page and its data'''

    # Getting popular News
    news = get_news(id)
    title= f'{news.title}'
    return render_template('news.html',title = title,news = news)