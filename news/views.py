from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import News
from datetime import datetime


class NewsList(ListView):
    model = News
    ordering = 'name'
    template_name = 'default.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        # С помощью super() мы обращаемся к родительским классам
        # и вызываем у них метод get_context_data с теми же аргументами,
        # что и были переданы нам.
        # В ответе мы должны получить словарь.
        context = super().get_context_data(**kwargs)
        # К словарю добавим текущую дату в ключ 'time_now'.
        context['time_now'] = datetime.utcnow()
        # Добавим ещё одну пустую переменную,
        # чтобы на её примере рассмотреть работу ещё одного фильтра.
        context['next_news'] = "Свежие новости каждый день!"
        return context

    def news_view(request):
        news = News.objects.all()
        news_count = len(news)
        return render(request, 'default.html', {'news': news, 'news_count': news_count})


class NewsDetail(DetailView):
    model = News
    template_name = 'news.html'
    context_object_name = 'news'
# Create your views here.
