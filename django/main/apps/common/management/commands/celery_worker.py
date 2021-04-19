import shlex
import subprocess

from django.core.management.base import BaseCommand
from django.utils import autoreload
from django.conf import settings


def restart_celery():
    DEBUG = settings.DEBUG
    cmd = 'pkill -9 celery'
    subprocess.call(shlex.split(cmd))
    if DEBUG:
        cmd = 'celery -A main worker -l DEBUG'
    else:
        cmd = 'celery -A main worker -l INFO'
    subprocess.call(shlex.split(cmd))


class Command(BaseCommand):

    def handle(self, *args, **options):
        print('Starting celery worker with autoreload...')
        autoreload.run_with_reloader(restart_celery)
