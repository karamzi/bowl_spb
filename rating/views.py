from django.shortcuts import render
from tournaments.models import Years


def rating(request):
    context = {
        'years': []
    }
    years = Years.objects.all()
    for year_item in years:
        year = {
            'year': year_item.year,
            'men': year_item.statistic_year.filter(sex='men'),
            'women': year_item.statistic_year.filter(sex='women'),
            'rating': year_item.rating,
        }
        context['years'].append(year)
    return render(request, 'rating.html', context)
