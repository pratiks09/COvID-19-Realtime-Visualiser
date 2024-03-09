from django.http import HttpResponse
import bs4
import pandas as pd
import requests

from django.shortcuts import render

sample = []
headings = []
sno = []
state = []
confirm_case = []
cured = []
death = []
total_affected = int()
total_cured = int()
total_died = int()
active_case = []
total_active = int()


def check(a):
    if a.isdigit():
        return a
    else:
        l = len(a)
        a = a[:l - 1]
        return a


# Create your views here.
def home():
    scrapp()
    print(total_affected)
    #return render(request, 'home.html', {'total_affected': total_affected})


def scrapp():
    res = requests.get('https://www.mohfw.gov.in/#state-data')
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    table = soup.find('section', id='state-data')
    print("website fetched")
    heading = table.find_all('th')
    samle = table.find_all('td')
    for i in heading:
        headings.append(i.text)
    for i in samle:
        sample.append(i.text)

    column = len(headings)
    row = int(33)

    a = 0
    ss = int(0)
    for x in range(row):
        sno.append(int(check(sample[ss])))
        ss = ss + 1
        state.append(sample[ss])
        ss = ss + 1
        confirm_case.append(int(check(sample[ss])))
        ss = ss + 1
        cured.append(int(check(sample[ss])))
        ss = ss + 1
        death.append(int(check(sample[ss])))
        ss = ss + 1
        active_case.append(int(confirm_case[a] - cured[a] - death[a]))
        a = a + 1
    ss = ss + 1

    total_affected = check(sample[ss])
    ss = ss + 1
    total_cured = check(sample[ss])
    ss = ss + 1
    total_died = check(sample[ss])
    total_active = sum(active_case)
    return None;
home()