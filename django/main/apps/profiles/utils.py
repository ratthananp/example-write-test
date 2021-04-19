from typing import TypedDict

from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError

from main.apps.profiles.models import Profile


class UserData(TypedDict):
    username: str
    email: str
    password: str


def is_user_email_duplicate(email: str) -> bool:
    return User.objects.filter(
        email=email
    ).exists()


def is_username_duplicate(username: str) -> bool:
    return User.objects.filter(
        username=username
    ).exists()


def create_user_for_profile(profile: Profile, user_data: UserData) -> None:
    username = user_data['username'].strip()
    if is_username_duplicate(username):
        raise ValidationError('Username is duplicate')

    email = user_data['email'].strip()
    if is_user_email_duplicate(email):
        raise ValidationError('Email is duplicate')

    user = User(
        username=username,
        email=email,
    )

    password = user_data['password']
    user.set_password(password)
    user.save()

    profile.user = user
    profile.save()
