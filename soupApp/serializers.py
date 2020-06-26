from rest_framework import serializers
from soupApp.models import Table, Game
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username',
                  'email',
                  'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validate_data):
        user = User(
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

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('table',
                  'user',
                  'time')

    def create(self, validate_data):
        game = Game(
            time=validate_data['time'],
            table=validate_data['table'],
            user=validate_data['user'],
        )
        print(game.time)
        game.save()
        return game

class GameSerializer2(serializers.ModelSerializer):
    table_name = serializers.CharField(source='table.name')
    user_name = serializers.CharField(source='user.username')
    class Meta:
        model = Game
        fields = ('table_name',
                  'user_name',
                  'time')

    def create(self, validate_data):
        game = Game(
            time=validate_data['time'],
            table_name=validate_data['table'],
            user_name=validate_data['user'],
        )
        print(game.time)
        game.save()
        return game
