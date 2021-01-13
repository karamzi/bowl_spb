from django.shortcuts import render
from tournaments.models import Years
import json


def rating(request):
    context = {
        'years': []
    }
    years = Years.objects.all()
    for year_item in years:
        year = {
            'year': year_item.year,
            'tournaments': [],
            'rating': year_item.rating,
            'statistic': year_item.statistic,
        }
        tournaments = year_item.tournament_year.all()
        for tournament_item in tournaments:
            if tournament_item.results.all().count() > 0:
                tournament = {
                    'name': tournament_item.name,
                    'players': [],
                }
            else:
                continue
            for player in tournament_item.results.all():
                player = json.loads(player.results)
                tournament['players'].append(player)
            year['tournaments'].append(tournament)
        context['years'].append(year)
    return render(request, 'rating.html', context)
