from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
import json

from django.shortcuts import render
from tournaments.models import Years
from rating.models import AllRating, Rating
from main.models import Profile


def statistic(request):
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
    return render(request, 'statistics.html', context)


def rating(request):
    context = {
        'years': []
    }
    years = Years.objects.all()
    for year_item in years:
        if not year_item.rating_year.all():
            continue
        man_rating = year_item.rating_year.get(sex='men').rating
        man_rating = json.loads(man_rating)
        woman_rating = year_item.rating_year.get(sex='women').rating
        woman_rating = json.loads(woman_rating)
        year = {
            'man_rating': man_rating['data'],
            'woman_rating': woman_rating['data'],
            'year': year_item.year,
            'rating': year_item.rating
        }
        context['years'].append(year)
    return render(request, 'rating.html', context)


@csrf_exempt
def upload_rating_ajax(request):
    data = json.loads(request.body)
    year = Years.objects.get(year=data['year'])
    rating, _ = AllRating.objects.get_or_create(year=year, sex=data['sex'])
    rating.rating = json.dumps(data, ensure_ascii=False)
    rating.save()
    single_rating = Rating.objects.filter(league=data['sex'])
    for item in single_rating:
        item.delete()
    for item in data['data'][1:9]:
        try:
            player = Profile.objects.get(name=item[1])
        except ObjectDoesNotExist:
            return JsonResponse(status=400, data={
                'status': 'error',
                'message': f'player: {item[1]} has not been found'
            }, json_dumps_params={'ensure_ascii': False})
        Rating.objects.create(player=player, score=item[-1], league=data['sex'])
    return JsonResponse({
        'status': 'OK',
    })
