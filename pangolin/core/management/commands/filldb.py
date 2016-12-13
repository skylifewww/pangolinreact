from django.core.management import call_command
from django.core.management.base import NoArgsCommand

from pangolin.users.factories import generate_users


class Command(NoArgsCommand):
    help = 'Fill the database with test fixtures'

    def handle(self, *args, **options):
        self.stdout.write('Starting fill db\r\n')

        # fixture_list = []
        # call_command('loaddata', *fixture_list)

        generate_users()

        self.stdout.write('Completed fill db\r\n')
