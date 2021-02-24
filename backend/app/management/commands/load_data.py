from backend.app import models
from django.core.management.base import BaseCommand, CommandError
from bs4 import BeautifulSoup
import requests
from django.db.models import Avg, Case, Count, F, Max, Min, Prefetch, Q, Sum, When, Exists, OuterRef, Subquery
from backend.users.models import User


class Command(BaseCommand):
    help = 'Delete and load all the data'

    def handle(self, *args, **options):
        self.stdout.write('Started deleting all models')
        self.stdout.write('Successfully deleted all models')
        # User.objects.all().delete()
        self.stdout.write("Started adding data. This may take few minutes, please don't interupt the commmand")
        if not User.objects.filter(email='admin@admin.com').count() > 0:
            user = User(email='admin@admin.com', first_name='admin',
                        last_name='admin', address="adress1",
                        phone_number="+44444444")
            user.set_password('password')
            user.is_superuser = True
            user.is_staff = True
            user.is_active = True
            user.save()
        self.stdout.write('Successfully loaded all the data')
