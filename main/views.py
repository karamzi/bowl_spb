import datetime
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, HttpResponse
from .models import Profile, Results, StudentsTournaments
from tournaments.models import Tournaments, Calendar, Years, Regulation
from rating.models import Rating, Statistics
from news.models import News
import json
from django.views.decorators.csrf import csrf_exempt


def index(request):
    news = News.objects.all()[:3]
    month_list = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Ноябрь',
                  'Октябрь', 'Декабрь']
    if 'month' in request.GET:
        month = int(request.GET['month'])
    else:
        month = datetime.datetime.now().month
    date_from = datetime.date(datetime.datetime.now().year, month, 1)
    date_to = datetime.date(datetime.datetime.now().year + month // 12, month % 12 + 1, 1) + datetime.timedelta()
    calendar = Calendar.objects.filter(date_start__gte=date_from, date_start__lt=date_to)
    is_tournament = True
    if not calendar:
        calendar = Calendar.objects.filter(date_start__gte=date_from)[0]
        calendar = [calendar]
        is_tournament = False
    man = Rating.objects.filter(league='man', active=True)[:6]
    woman = Rating.objects.filter(league='woman', active=True)[:6]
    context = {
        'news': news,
        'month_list': month_list,
        'current_month': month_list[month - 1],
        'calendar': calendar,
        'is_tournament': is_tournament,
        'man': man,
        'woman': woman,
    }
    return render(request, 'index.html', context)


def profile(request, pk):
    player = Profile.objects.get(pk=pk)
    context = {
        'years': [],
        'player': player.name,
    }
    years = Years.objects.all()
    for year_item in years:
        try:
            statistic = year_item.statistic_year.get(name=player)
        except ObjectDoesNotExist:
            continue
        year = {
            'year': year_item.year,
            'tournaments': [],
            'statistic': statistic,
        }
        tournaments = year_item.tournament_year.all()
        for tournament_item in tournaments:
            try:
                results = tournament_item.results.get(player=player)
            except ObjectDoesNotExist:
                continue
            tournament = {
                'name': tournament_item.name,
                'results': json.loads(results.results),
            }
            year['tournaments'].append(tournament)
        context['years'].append(year)
    return render(request, 'profile.html', context)


def calendar(request):
    calendar_list = Calendar.objects.all()
    context = {
        'calendar': calendar_list
    }
    return render(request, 'calendar.html', context)


def goals(request):
    return render(request, 'goals.html')


def leadership(request):
    return render(request, 'leadership.html')


def documents(request):
    return render(request, 'documents.html')


def protocols(request):
    return render(request, 'protocols.html')


def regulations(request):
    years = Years.objects.all()
    regulations = Regulation.objects.filter(archive=False)
    context = {
        'years': years,
        'regulations': regulations,
    }
    return render(request, 'regulations.html', context)


def students_tournaments(request):
    student_tournament = StudentsTournaments.objects.first()
    context = {
        'student_tournament': student_tournament
    }
    return render(request, 'students_tournaments.html', context)


def contacts(request):
    return render(request, 'contacts.html')


@csrf_exempt
def ajax_parse_results(request):
    if request.method == 'POST':
        data = json.loads(request.POST['results'])
        tournament = Tournaments.objects.get(pk=data['id'])
        for player in data['players']:
            result = Results()
            year = Years.objects.get(year=datetime.datetime.now().year)
            user, status = Profile.objects.get_or_create(name=player['name'])
            user.rang = str(player['rang']).lower()
            user.save()
            statistic, status = Statistics.objects.get_or_create(name=user, year=year)
            statistic.year = year
            statistic.summ = statistic.summ + int(player['summ'])
            statistic.score = statistic.score + len(player['results'])
            if statistic.max < int(player['max']):
                statistic.max = int(player['max'])
            if statistic.min > int(player['min']):
                statistic.min = int(player['min'])
            statistic.mean = statistic.summ / statistic.score
            statistic.save()
            result.tournament = tournament
            result.player = user
            player['id'] = user.pk
            result.results = json.dumps(player, ensure_ascii=False)
            result.save()
        return HttpResponse(status=200)
