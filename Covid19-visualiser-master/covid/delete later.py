from webscrapper.models import databasestatewise, databasetotal

list = []
objects = databasestatewise.objects.all()
print(objects)
