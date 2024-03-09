import datetime

from webscrapper.models import databasestatewise, databasetotal

dbstate = databasestatewise()
dbtotal = databasetotal()

status = "initial"


def check():
    global status
    flag = int(0)
    dates = []
    for e in databasetotal.objects.all():
        dates.append(str(e.date))

    today_date = str(datetime.date.today())
    for w in dates:
        if w == today_date:
            flag = 1
            status = "date existed"
    return flag


def format(data, total):
    flag = check()

    if flag == 0:
        for i in range(32):
            r = databasestatewise(
                date=datetime.date.today(),
                state=data.state[i],
                confirm_case=data.confirm_case[i],
                cured=data.cured[i],
                death=data.death[i])
            r.save()

        q = databasetotal(
            date=datetime.date.today(),
            total_affected=total.total_affected,
            total_cured=total.total_cured,
            total_died=total.total_died,
            total_active=total.total_active)
        q.save()

        return "corngo updated"
    else:

        return status

