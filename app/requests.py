import urllib.request,json
from .models import News




#Getting api key
api_key = None

#Getting the news base url
base_url = None

def configure_request(app):
    global api_key,base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']

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
    
    return news_results




def get_news(id):
    get_news_details_url = base_url.format(id,api_key)


    with urllib.request.urlopen(get_news_details_url) as url:
        news_details_data = url.read()
        news_details_response = json.loads(news_details_data)

        news_object = None
        if news_details_response:
            id = news_details_response.get('id')
            name = news_details_response.get('name')
            author = news_details_response.get('author')
            title = news_details_response.get('title')
            description = news_details_response.get('description')
            url = news_details_response.get('url')

            news_object =News(id,name,author,title,description,url)

    return news_object

            
        
def search_news(news_name):
    search_news_url = 'https://newsapi.org/v2/top-headlines?country=us&category={}&apiKey={}'.format(api_key,news_name)
    with urllib.request.urlopen(search_news_url) as url:
        search_news_data = url.read()
        search_news_response = json.loads(search_news_data)

        search_news_results = None

        if search_news_response['results']:
            search_news_list = search_news_response['results']
            search_news_results = process_results(search_news_list)


    return search_news_results


        


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
        name = news_item.get('name')
        author = news_item.get('author')
        poster = news_item.get('title')
        description = news_item.get('description')
        url = news_item.get('url')


        if poster:


            news_object = News(id,name,author,poster,description,url)
            news_results.append(news_object)

    return news_results 