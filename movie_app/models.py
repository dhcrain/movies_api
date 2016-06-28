from django.db import models

# Create your models here.


class Rater(models.Model):
    age = models.IntegerField()
    gender = models.CharField(max_length=1)
    occupation = models.CharField(max_length=30)
    zip_code = models.CharField(max_length=5)


class Movie(models.Model):
    movie_title = models.CharField(max_length=50)
    release_date = models.CharField(max_length=15)
    video_release_date = models.CharField(max_length=15, default="")      # empty is OK
    imdb_url = models.CharField(max_length=300)
    unknown = models.CharField(max_length=50)
    action = models.IntegerField()
    adventure = models.IntegerField()
    animation = models.IntegerField()
    childrens = models.IntegerField()
    comedy = models.IntegerField()
    crime = models.IntegerField()
    documentry = models.IntegerField()
    drama = models.IntegerField()
    fantasy = models.IntegerField()
    film_noir = models.IntegerField()
    horror = models.IntegerField()
    musical = models.IntegerField()
    mystery = models.IntegerField()
    romance = models.IntegerField()
    sci_fi = models.IntegerField()
    thriller = models.IntegerField()
    war = models.IntegerField()
    western = models.IntegerField()


class Rating(models.Model):
    user_id = models.ForeignKey(Rater)
    item_id = models.ForeignKey(Movie)
    rating = models.IntegerField()
    timestamp = models.IntegerField()
