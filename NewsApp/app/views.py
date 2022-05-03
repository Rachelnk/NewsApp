from flask import render_template, request, redirect, url_for
# from app import app
from . import main

from app.request import get_news, get_articles, search_source

# Views
@main.route('/')
def index():
    general_news = get_news('general')
    sports_news = get_news('sports')
    business_news = get_news('business')
    technology_news = get_news('technology')
    entertainment = get_news('entertainment')
    # health_news = get_news('health')
    science_news = get_news ('science')
    
    title = "Home- Get your latest news higlights from NewsApp"
    search_source = request.args.get('news_query')
    if search_source:
        return redirect(url_for('search', name = search_source))
    else:
     return render_template('index.html', entertainment = entertainment, business = business_news, general = general_news, science = science_news, technology = technology_news, sports = sports_news)
@main.route('/source/<id>')
def source(id):
  articles = get_articles(id)
  source_id = id.upper()
  title= f'{source_id} - Top Articles'
   
  return render_template('source.html',title=title,id=source_id, articles=articles)
  # create search view function to display our search items.

@main.route('/search/<name>')
def search(name):
    '''
    View function to display the search results
    '''
    source_name_list = name.split(" ")
    source_name_format = "+".join(source_name_list)
    searched_sources = search_source(source_name_format)
    title = f'search results for {name}'
    return render_template('search.html',sources = searched_sources)
