from flask import render_template
from app import app

# Views
@app.route('/')
def index():
    title = "Welcome to NewsApp"

    return render_template('index.html')
@app.route('/news/<news_id>')
def movie(news_id):

    
    return render_template('news.html',id = news_id)