from flask import render_template,request,redirect,url_for

from app import app

from .request import get_newss,get_news


#Views
@app.route('/')
def index():

    '''Veiw root page function that returns the index page and its data'''

    
    # Getting popular News
    popular_news = get_newss('popular')
    upcoming_news = get_newss('upcoming')
    now_showing_news = get_newss('now_showing')
    
    title= 'Home - Welcome to the best News Review Website Online'
    
    search_news = request.args.get('news_query')
    
    if search_news:
        return redirect(url_for('search',news_name = search_news))
    else:
        return render_template('index.html', title = title, popular = popular_news, upcoming = upcoming_news, now_showing = now_showing_news)


@app.route('/news/<int:id>')
def news(id):

    '''
    View news page function that returns the news details page and its data
    '''
    news = get_news(id)
    title = f'{news.title}'

    return render_template('news.html',title = title,news = news)



@app.route('/search/<news_name>')
def search(news_name):

    '''Veiw function to display the search results'''

    news_name_list = news_name.split(" ")
    news_name_format = "+".join(news_name_list)
    searched_newss = search_news(news_name_format)
    title = f'search results for {news_name}'
    return render_template('search.html',newss = searched_newss)