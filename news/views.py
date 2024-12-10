from django.shortcuts import render
from .models import News, Category

def news_list_view(request):
    news_list = News.objects.all()
    news5 = News.objects.all()[:5]
    local_one = News.objects.filter(category__name = 'Mahalliy')[0]
    local_news = News.objects.filter(category__name = 'Mahalliy')[1:5]
    xorij_one = News.objects.filter(category__name = 'Xorij')[0]
    xorij_news = News.objects.filter(category__name = 'Xorij')[1:5]
    technology_one = News.objects.filter(category__name = 'Texnologiya')[0]
    technology_news = News.objects.filter(category__name = 'Texnologiya')[1:5]
    sport_one = News.objects.filter(category__name = 'Sport')[0]
    sport_news = News.objects.filter(category__name = 'Sport')[1:5]

    context = {
        'news_list': news_list,
        'news5': news5,
        'local_one': local_one,
        'local_news': local_news,
        'xorij_one': xorij_one,
        'xorij_news': xorij_news,
        'technology_one': technology_one,
        'technology_news': technology_news,
        'sport_one': sport_one,
        'sport_news': sport_news
    }

    return render(request, 'index.html', context)

def news_detail_view(request, slug):
    news_detail = News.objects.get(slug=slug)
    three_news = News.objects.filter(category__name = news_detail.category.name).exclude(id=news_detail.id)[:3]


    context = {
        'news_detail': news_detail,
        'three_news': three_news
    }

    return render(request, 'single_page.html', context)

def contact_view(request):
    context = {

    }
    return render(request, 'contact.html', context)

def about_us_view(request):
    context = {

    }

    return render(request, 'about_us.html', context)

def local_news_view(request):
    news_list = News.objects.filter(category__name = 'Mahalliy')

    context = {'news_list': news_list}

    return render(request, 'local_news.html', context)

def xorij_news_view(request):
    news_list = News.objects.filter(category__name = 'Xorij')

    context = {'news_list': news_list}

    return render(request, 'xorij_news.html', context)

def texnologiya_news_view(request):
    news_list = News.objects.filter(category__name = 'Texnologiya')

    context = {'news_list': news_list}

    return render(request, 'texnologiya_news.html', context)

def sport_news_view(request):
    news_list = News.objects.filter(category__name = 'Sport')

    context = {'news_list': news_list}

    return render(request, 'sport_news.html', context)