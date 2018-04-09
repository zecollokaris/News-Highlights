from flask import render_template
from .config import DevConfig
from app import app

from .request import get_newss
from .request import get_newss,get_news,search_news


#Views
@app.route('/search/<news_name>')
def news(news_name):

    '''Veiw function to display the search results'''

    news_name_list = news.split(" ")
    news_name_format = "+".join(news_name_list)
    searched_newss = search_news(news_name_format)
    title = f'search results for {news_name}'
    return render_template('search.html,newss = searched_newss')