import os
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.db.utils import IntegrityError

class Command(BaseCommand):
    help = 'Create a default superuser if it does not exist'

    def add_arguments(self, parser):
        parser.add_argument(
            '--username',
            type=str,
            default='admin',
            help='Specify the username for the superuser (default: admin)',
        )
        parser.add_argument(
            '--email',
            type=str,
            default='admin@example.com',
            help='Specify the email for the superuser (default: admin@example.com)',
        )
        parser.add_argument(
            '--password',
            type=str,
            default='adminpassword',
            help='Specify the password for the superuser (default: adminpassword)',
        )

    def handle(self, *args, **kwargs):
        User = get_user_model()
        username = kwargs['username']
        email = kwargs['email']
        password = kwargs['password']

        try:
            if not User.objects.filter(username=username).exists():
                User.objects.create_superuser(
                    username=username,
                    email=email,
                    password=password
                )
                self.stdout.write(self.style.SUCCESS(f'Successfully created superuser: {username}'))
            else:
                self.stdout.write(self.style.WARNING(f'Superuser "{username}" already exists'))
        except IntegrityError as e:
            self.stdout.write(self.style.ERROR(f'Error creating superuser: {e}'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'An unexpected error occurred: {e}'))
