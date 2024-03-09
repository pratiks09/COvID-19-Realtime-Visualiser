from django.db import models
import schedule
import time


# Create your models here.
class statedata():
    headings = []
    sno = []
    state = []
    confirm_case = []
    cured = []
    death = []
    active_case = []


class totaldata():
    total_affected = int()
    total_cured = int()
    total_died = int()
    total_active = int()


class databasestatewise(models.Model):
    date = models.DateField(auto_now=False, auto_now_add=False)
    state = models.CharField(max_length=200)
    confirm_case = models.PositiveIntegerField(default=0)
    cured = models.PositiveIntegerField(default=0)
    death = models.PositiveIntegerField(default=0)



class databasetotal(models.Model):
    date = models.DateField(auto_now=False, auto_now_add=False, unique=True)
    total_affected = models.PositiveIntegerField(default=0)
    total_cured = models.PositiveIntegerField(default=0)
    total_died = models.PositiveIntegerField(default=0)
    total_active = models.PositiveIntegerField(default=0)
