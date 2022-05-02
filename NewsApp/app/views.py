from flask import render_template
from app import app
from app.request import get_news, get_articles

# Views
@app.route('/')
def index():
    general_news = get_news('general')
    sports_news = get_news('sports')
    business_news = get_news('business')
    technology_news = get_news('technology')
    entertainment = get_news('entertainment')
    health_news = get_news('health')
    science_news = get_news ('science')
    
    title = "Home- Get your latest news higlights from NewsApp"

    return render_template('index.html', entertainment = entertainment, business = business_news, general = general_news, science = science_news, technology = technology_news, sports = sports_news)
@app.route('/news/<news_id>')
def movie(news_id):

    
    return render_template('news.html',id = news_id)