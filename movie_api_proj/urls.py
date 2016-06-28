"""movie_api_proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from movie_app.views import MovieListCreateAPIView, MovieRetrieveUpdateDestroyAPIView, RaterListCreateAPIView, RaterRetrieveUpdateDestroyAPIView, RatingsListCreateAPIView, RatingsRetrieveUpdateDestroyAPIView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/movies/$', MovieListCreateAPIView.as_view(), name='movie_list_create_api_view'),
    url(r'^api/movies/(?P<pk>\d+)/$', MovieRetrieveUpdateDestroyAPIView.as_view(), name='movie_retrieve_update_destroy_api_view'),
    url(r'^api/raters/$', RaterListCreateAPIView.as_view(), name='rater_list_create_api_view'),
    url(r'^api/raters/(?P<pk>\d+)/$', RaterRetrieveUpdateDestroyAPIView.as_view(), name='rater_retrieve_update_destroy_api_view'),
    url(r'^api/ratings/$', RatingsListCreateAPIView.as_view(), name='ratings_list_create_api_view'),
    url(r'^api/ratings/(?P<pk>\d+)/$', RatingsRetrieveUpdateDestroyAPIView.as_view(), name='ratings_retrieve_update_destroy_api_view'),

]
