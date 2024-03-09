import bs4
import requests
from cronmodel import statedata
from cronmodel import totaldata

data = statedata()
total = totaldata()


def check(a):
    if a.isdigit():
        return a
    else:
        l = len(a)
        a = a[:l - 1]
        return a


def scrapp():
    global data
    global total
    sample = []
    res = requests.get('https://www.mohfw.gov.in/#state-data')
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    table = soup.find('section', id='state-data')
    heading = table.find_all('th')
    samle = table.find_all('td')
    for i in heading:
        data.headings.append(i.text)
    for i in samle:
        sample.append(i.text)

    column = len(data.headings)
    row = int(32)
    a = 0
    ss = int(0)
    for x in range(row):
        data.sno.append(int(check(sample[ss])))
        ss = ss + 1
        data.state.append(sample[ss])
        ss = ss + 1
        data.confirm_case.append(int(check(sample[ss])))
        ss = ss + 1
        data.cured.append(int(check(sample[ss])))
        ss = ss + 1
        data.death.append(int(check(sample[ss])))
        ss = ss + 1
        data.active_case.append(int(data.confirm_case[a] - data.cured[a] - data.death[a]))
        a = a + 1
    ss = ss + 1

    total.total_affected = int(check(sample[ss]))
    ss = ss + 1

    total.total_cured = int(check(sample[ss]))
    ss = ss + 1
    total.total_died = int(check(sample[ss]))
    samplee = total.total_affected - total.total_cured - total.total_died
    total.total_active = int(samplee)
    return None


scrapp()
print(total)


def get_state_data_live():
    global data
    return data


def get_total_data_live():
    global total
    return total
