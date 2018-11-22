from datetime import datetime, timedelta

from django.core.management.base import BaseCommand

from api.utils import create_night


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('location', action='store', help='Location for this night')
        parser.add_argument('start', action='store', default=False, help='Start date')
        parser.add_argument('end', action='store', default=False, help='End date')

    def handle(self, *args, **options):

        start_date = datetime.strptime(options['start'], '%Y-%m-%d')
        end_date = datetime.strptime(options['end'], '%Y-%m-%d')

        date = start_date
        while date <= end_date:
            print(date.strftime('%Y-%m-%d'))
            create_night(options['location'], date.strftime('%Y-%m-%d'))
            date += timedelta(1)
