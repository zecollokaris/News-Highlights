class Review:

    all_reviews = []

    def __init__(self,news_id,title,imageurl,review):
        self.news_id = news_id
        self.title = title
        self.imageurl = imageurl
        self.review = review


    def save_review(self):
        Review.all_reviews.append(self)


    @classmethod
    def clear_reviews(cls):
        Review.all_reviews.clear()

class News:
    '''News class to define News Objects'''

    def __init__(self,id,title,overview,image,vote_average,vote_count):
        self.id =id
        self.title = title
        self.overview = overview
        self.image = 'https://image.tmdb.org/t/p/w500/'+image
        self.vote_average = vote_average
        self.vote_count = vote_count