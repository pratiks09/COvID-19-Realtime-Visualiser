from django.http import JsonResponse
from django.shortcuts import render

from webscrapper import scrappdatabase, scrappweb, process


# Create your views here.
def home(request):
    xaxis = []
    yaxis = []
    flag = int(0)
    scrappweb.scrapp()
    current_total_data = scrappweb.get_total_data_live()
    current_state_data = scrappweb.get_state_data_live()
    list_date = scrappdatabase.date(request)
    list_totalaffected = scrappdatabase.totalaffected(request)

    if flag == 0:
        xaxis = list_date
        yaxis = list_totalaffected

    status = process.format(current_state_data, current_total_data)
    return render(request, 'home.html',
                  {'current_statedata': current_state_data, 'current_total': current_total_data, 'xaxis': xaxis,
                   'yaxis': yaxis, 'status': status})

