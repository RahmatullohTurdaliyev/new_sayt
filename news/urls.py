from django.contrib import admin
from django.urls import path
from .views import news_list_view, news_detail_view, contact_view, about_us_view, local_news_view, xorij_news_view, texnologiya_news_view, sport_news_view


urlpatterns = [
    path('', news_list_view, name='home_page'),
    path('contact/', contact_view, name='contact_link'),
    path('about/', about_us_view, name='about_us_link'),
    path('local/', local_news_view, name='local_news'),
    path('xorij/', xorij_news_view, name='xorij_news'),
    path('texnologiya/', texnologiya_news_view, name='texnologiya_news'),
    path('sport/', sport_news_view, name='sport_news'),
    path('<slug>/', news_detail_view, name='detail_link'),

]