from django.shortcuts import render
from .models import News
from django.core.paginator import Paginator, EmptyPage


def news_list(request):
    news = News.objects.all()
    paginator = Paginator(news, 6)
    page = request.GET.get('page', 1)
    try:
        sheet = paginator.page(page)
    except EmptyPage:
        sheet = paginator.page(1)
        page = 1
    page_range = list(sheet.paginator.page_range)
    context = {
        'news': sheet.object_list,
        'page': page,
        'page_range': page_range,
        'previous_page_number': sheet.previous_page_number() if sheet.has_previous() else None,
        'next_page_number': sheet.next_page_number() if sheet.has_next() else None,
        'previous2': int(page) - 2,
        'next2': int(page) + 2,
    }
    return render(request, 'news_list.html', context)


def current_news(request, pk):
    news = News.objects.get(pk=pk)
    news.count += 1
    news.save()
    context = {
        'news': news,
    }
    return render(request, 'current_news.html', context)
