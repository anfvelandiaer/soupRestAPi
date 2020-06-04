from rest_framework import serializers
from soupApp.models import Tutorial, Table
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class TutorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutorial
        fields = ('id',
                  'title',
                  'description',
                  'published')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name',
                  'last_name',
                  'username',
                  'email',
                  'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validate_data):
        user = User(
            first_name=validate_data['first_name'],
            last_name=validate_data['last_name'],
            username=validate_data['username'],
            email=validate_data['email']
        )
        user.set_password(validate_data['password'])
        user.save()
        Token.objects.create(user=user)
        return user

    def validate_email(self, data):
        users = User.objects.filter(email=data)
        if len(users) != 0:
            raise serializers.ValidationError("Email exists")
        else: 
            return data


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = ('name',
                  'words',
                  'hunts')

    def create(self, validate_data):
        table = Table(
            name=validate_data['name'],
            words=validate_data['words'],
            hunts=validate_data['hunts'],
        )
        table.save()
        return table
