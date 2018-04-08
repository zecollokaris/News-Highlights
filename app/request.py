from app import app
import urllib.request,json
from .models import news

News = news.News

#Getting api key
api_key = app.config['NEWS_API_KEY']

#Getting the news base url
base_url = app.config["NEWS_API_BASE_URL"]



def get_newss(category):

    '''Function that gets the json response to our url request'''

    get_newss_url = base_url.format(category,api_key)
    
    with urllib.request.urlopen(get_newss_url) as url:
        get_newss_data = url.read()
        get_newss_response = json.loads(get_newss_data)

        news_results = None

        if get_newss_response['results']:
            news_results_list = get_newss_response['results']
            news_results = process_results(news_results_list)


    



def process_results(news_list):
    '''Function that process news result and transfort them to a list of Objects
    Args:
        news_list: A list of dictionaries that contain news details

    Returns :
        news_results: A list of news objects
    '''
    news_results = []
    for news_item in news_list:
        id = news_item.get('id')
        title = news_item.get('original_title')
        overview = news_item.get('overview')
        poster = news_item.get('poster_path')
        vote_average = news_item.get('vote_average')
        vote_count = news_item.get('vote_count')


        if poster:
            news_object = News(id,title,overview,poster,vote_average,vote_count)
            news_results.append(news_object)

    return news_results 