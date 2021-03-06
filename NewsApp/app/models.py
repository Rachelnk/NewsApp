class News:
    '''
    News class to define news objects
    '''
    def __init__(self, id, name, description, sourceurl, category, country):
        self.id = id
        self.name = name
        self.description = description
        self.sourceurl = sourceurl
        self.category = category
        self.country = country      

      
class Article:
	'''
	Article Class to define Article Objects
	'''
	def __init__(self,author,title,description,url,image,date):
		'''
		Function to initialize Article Objects
		It defines the properties each Article object will hold.
		'''
		self.author = author
		self.title = title
		self.description = description
		self.url = url
		self.image = image
		self.date = date