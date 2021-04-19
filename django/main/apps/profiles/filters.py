import django_filters

from main.apps.profiles.models import Profile


class ProfileFilter(django_filters.FilterSet):
    class Meta:
        model = Profile
        fields = ['role', 'first_name', 'last_name']
