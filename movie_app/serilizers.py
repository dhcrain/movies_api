
from rest_framework import serializers
from movie_app.models import Movie, Rater, Rating


class MovieSerilizer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ['id', 'movie_title', 'release_date', 'video_release_date',
                 'imdb_url', 'unknown', 'action', 'adventure', 'animation',
                 'childrens', 'comedy', 'crime', 'documentry', 'drama',
                 'fantasy', 'film_noir', 'horror', 'musical', 'mystery',
                 'romance', 'sci_fi', 'thriller', 'war', 'western']


class RaterSerilizer(serializers.ModelSerializer):

    class Meta:
        model = Rater
        fields = ['id', 'age', 'gender', 'occupation', 'zip_code']


class RatingsSerializer(serializers.ModelSerializer):
    # user_id = serializers.HyperlinkedIdentityField(view_name='rater_retrieve_update_destroy_api_view')
    # item_id = serializers.HyperlinkedIdentityField(view_name='movie_retrieve_update_destroy_api_view')

    class Meta:
        model = Rating
        fields = ['id', 'user_id', 'item_id', 'rating', 'timestamp']


# HyperlinkedModelSerializer










        pass
