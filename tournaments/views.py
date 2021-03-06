from django.shortcuts import render
from .models import Reports
from django.core.paginator import Paginator, EmptyPage


def tournaments_list(request):
    tournaments = Reports.objects.all()
    paginator = Paginator(tournaments, 6)
    page = request.GET.get('page', 1)
    try:
        sheet = paginator.page(page)
    except EmptyPage:
        sheet = paginator.page(1)
        page = 1
    page_range = list(sheet.paginator.page_range)
    context = {
        'tournaments': sheet.object_list,
        'page': page,
        'page_range': page_range,
        'previous_page_number': sheet.previous_page_number() if sheet.has_previous() else None,
        'next_page_number': sheet.next_page_number() if sheet.has_next() else None,
        'previous2': int(page) - 2,
        'next2': int(page) + 2,
    }
    return render(request, 'tournament_list.html', context)


def current_tournament(request, pk):
    tournament = Reports.objects.get(pk=pk)
    tournament.count += 1
    tournament.save()
    context = {
        'tournament': tournament,
    }
    return render(request, 'current_tournament.html', context)
