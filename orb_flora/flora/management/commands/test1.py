from django.core.management.base import BaseCommand, CommandError
from flora.models import Genus

class Command(BaseCommand):

    def handle(self, *args, **options):

        self.stdout.write("Unterminated line", ending="/n")
        self.stdout.write("Terminated line")
        oo=str(Genus.objects.all()[1].pk)
        self.stdout.write(oo, ending="!")