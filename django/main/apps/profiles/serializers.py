from django_restql.mixins import DynamicFieldsMixin
from model_controller.serializers import ModelControllerSerializer
from model_controller.utils import EXCLUDE_MODEL_CONTROLLER_FIELDS

from main.apps.profiles.models import Profile
from main.apps.profiles.utils import create_user_for_profile


class ProfileSerializer(DynamicFieldsMixin, ModelControllerSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
        read_only_fields = EXCLUDE_MODEL_CONTROLLER_FIELDS

    def create(self, validated_data):
        instance = super(ProfileSerializer, self).create(validated_data)
        initial_data = self.initial_data
        create_user_for_profile(
            profile=instance,
            user_data=initial_data
        )
        return instance
