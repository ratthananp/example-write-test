from rest_framework import viewsets

from main.apps.profiles.filters import ProfileFilter
from main.apps.profiles.models import Profile
from main.apps.profiles.serializers import ProfileSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    filter_class = ProfileFilter
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all().order_by('first_name', 'last_name')
