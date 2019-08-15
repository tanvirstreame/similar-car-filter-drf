from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string
from ...models import Vehicle

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        total = 4
        for i in range(total):
            Vehicle.objects.create(name="BMW", model='A1', price=20000, odometer_reading=200)

        for k in range(total):
            Vehicle.objects.create(name="BMW", model='A2', price=19000, odometer_reading=100)
        
        for l in range(total):
            Vehicle.objects.create(name="BMW", model='A2', price=19000, odometer_reading=200)

        for m in range(total):
            Vehicle.objects.create(name="AUDI", model='A2', price=25000, odometer_reading=700)

        for n in range(total):
            Vehicle.objects.create(name="MERCEDIES", model='A6', price=25000, odometer_reading=700)