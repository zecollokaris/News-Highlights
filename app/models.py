class News:
    '''News class to define News Objects'''

    def __init__(self,id,name,author,title,description,url,urlToImage,publishedAt):
        self.id =id
        self.name = name
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
       
class Source:

    '''Source class to define Source Objects'''

    def __init__(self,id,name,description,url,category,title):
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.title = title




  