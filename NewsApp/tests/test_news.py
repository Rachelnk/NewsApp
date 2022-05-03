import unittest
from app.models import news, articles
News = news.news
Article = articles.articles

class NewsTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Movie class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_news = News(1234,'ABC News','A thrilling new Python Series','Your trusted source for breaking news, analysis, exclusive interviews, headlines, and videos at ABCNews.com.','https://abcnews.go.com','general','us')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))

class ArticleTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Movie class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_articles = Article('ABC News','Israel demands apology from Russia for unforgivable statements about the Holocaust','Israel lambasts Russian Foreign Minister Sergei Lavrov for claiming Adolf Hitler had Jewish origins, saying it is an "unforgivable"..','https://www.abc.net.au/news/2022-05-03/israel-russia-sergei-lavrov-zelenskyy-moscow/101032388','image.jpg', '2022-05-02')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_articles,Article))


if __name__ == '__main__':
    unittest.main()