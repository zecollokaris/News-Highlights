from flask import render_template
from app import app
from .request import get_newss


#Views
@app.route('/')
def index():

    '''Veiw root page function that returns the index page and its data'''
    
    #Getting popular News
    popular_newss = get_newss('popular')
    print(popular_newss)
    title= 'Home -Welcome to the best News Review Website Online'
    return render_template('index.html',title = title,popular = popular_newss)