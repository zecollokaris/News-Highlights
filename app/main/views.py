from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_newss,get_news



#Views
@main.route('/')
def index():
    
 
        return render_template('index.html')

@main.route('/news/<int:id>')
def news(id):

    '''
    View news page function that returns the news details page and its data
    '''
    news = get_news(id)
    title = f'{news.title}'

    return render_template('news.html',title = title,news = news)




