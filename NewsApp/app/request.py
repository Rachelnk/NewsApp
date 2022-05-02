from unicodedata import category
from app import app
import urllib.request, json
from .models import news, articles
News = news.News
Article = articles.Article
#  getting api key
api_key = app.config['NEWS_API_KEY']
# Getting the news source base url
source_base_url = app.config["NEWS_SOURCES_BASE_URL"]
articles_base_url = app.config['NEWS_ARTICLES_BASE_URL']


def get_news(category):
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = source_base_url.format(category)
    # get_news_url = 'https://newsapi.org/v2/sources?apiKey=e9bccdcb8e164e9d8e5420ea88db15c5'

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['sources']:
            news_results_list = get_news_response['sources']
            news_results = process_results(news_results_list)


    return news_results
def process_results(news_results):
  '''
  Function  that processes the news result and transform them to a list of Objects
  '''
  news_list = []
  for news_item in news_results:
    id =news_item.get('id')
    name =news_item.get('name')
    description =news_item.get('description')
    url =news_item.get('url')
    category = news_item.get('category')
    country =news_item.get('country')

    source_object = News(id, name, description, url, category, country)
    news_list.append(source_object)
    
  return news_list

def get_articles(news):
    get_articles_url = articles_base_url.format(news,api_key)

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        articles_results = None
        if get_articles_response['articles']:
            articles_results_list = get_articles_response['articles']
            articles_results = process_articles(articles_results_list)
			      

    return articles_results

def process_articles(articles_results):
        '''
	      Function  that processes the articles result and transform them to a list of Objects
	      '''
        articles_list = []
        for article_item in articles_results:
                author = article_item.get('author')
                title = article_item.get('title')
                description = article_item.get('description')
                url = article_item.get('url')
                image = article_item.get('urlToImage')
                date = article_item.get('publishedAt')
                if date and author and image:
                        article_object = Article(author,title,description,url,image,date)
                        articles_list.append(article_object)
        return articles_list

#search function to search for articles according to the source name
def search_source(source_name):
    search_news_url = source_base_url.format(source_name)
    
    with urllib.request.urlopen(search_news_url) as url:
        search_news_data = url.read()
        search_news_response = json.loads(search_news_data)

        search_news_results = None

        if search_news_response['sources']:
            search_news_list = search_news_response['sources']
            search_news_results = process_results(search_news_list)


    return search_news_results

	      
        

