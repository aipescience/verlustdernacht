from django.core.management.base import BaseCommand

from api.utils import create_night


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('location', action='store', help='Location for this night')
        parser.add_argument('date', action='store', default=False, nargs='?', help='Date for this night')

    def handle(self, *args, **options):
        create_night(options['location'], options['date'])
