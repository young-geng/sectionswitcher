from switcher.routine import expire_verification, expire_match, find_match
from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):

    def handle(self, *args, **options):
        self.stdout.write("Running routine tasks")
        expire_verification()
        expire_match()
        find_match()

