from flask import render_template
from . import main

@main.app_errorhandler(404)
def four_Ow_four(error):
    '''Function to render the 404 error page
    '''
    return render_template('fourOwfour.html'),404

@main.app_errorhandler(500)
def five_Ow_five(error):
    return render_template('fiveOwfive.html'),500