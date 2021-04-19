from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from main.apps.profiles.models import Profile, Role
from django.db import transaction


class Command(BaseCommand):
    help = 'Create initial project data'

    def handle(self, *args, **options):
        with transaction.atomic():
            self._create_initial_user()

    @staticmethod
    def _create_initial_user():
        if not User.objects.exists():
            user = User.objects.create_superuser(
                username='admin',
                email='admin@example.com',
                password='admin'
            )

            Profile.objects.create(
                role=Role.ADMIN,
                user=user,
                first_name='admin',
                last_name='admin',
                created_user=user,
                updated_user=user
            )
