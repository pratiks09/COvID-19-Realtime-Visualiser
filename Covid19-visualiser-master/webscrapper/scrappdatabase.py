from webscrapper.models import databasetotal


def date(request):
    dates = []
    for e in databasetotal.objects.all():
        dates.append(str(e.date))
    return dates


def totalaffected(request):
    yaxiss = []
    for e in databasetotal.objects.all():
        yaxiss.append(e.total_affected)
    return yaxiss
