from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        refresh = self.get_token(self.user)

        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        # add extra responses
        profile = self.user.profile
        data['username'] = str(self.user.username)
        data['firstName'] = str(profile.first_name)
        data['lastName'] = str(profile.last_name)
        data['role'] = str(profile.role)

        return data
