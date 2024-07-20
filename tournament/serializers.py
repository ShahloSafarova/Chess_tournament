from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Player, Tournament, Match
from rest_framework.exceptions import ValidationError

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class PlayerSerializer(serializers.ModelSerializer):
    def validate_rating(self, value):
        if value < 0:
            raise ValidationError("Rating must be a positive integer")
        return value

    class Meta:
        model = Player
        fields = '__all__'

class TournamentSerializer(serializers.ModelSerializer):
    players = serializers.PrimaryKeyRelatedField(queryset=Player.objects.all(), many=True)

    class Meta:
        model = Tournament
        fields = '__all__'

    def create(self, validated_data):
        players_data = validated_data.pop('players')
        tournament = Tournament.objects.create(**validated_data)
        tournament.players.set(players_data)
        return tournament

    def update(self, instance, validated_data):
        players_data = validated_data.pop('players')
        instance.name = validated_data.get('name', instance.name)
        instance.start_date = validated_data.get('start_date', instance.start_date)
        instance.end_date = validated_data.get('end_date', instance.end_date)
        instance.save()
        instance.players.set(players_data)
        return instance

class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = '__all__'


