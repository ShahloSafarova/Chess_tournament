from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.models import User
from .models import Player, Tournament, Match
from .serializers import UserSerializer, PlayerSerializer, TournamentSerializer, MatchSerializer
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from .permissions import IsAdminUserOrReadOnly
from .utils import calculate_leaderboard, swiss_pairing

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class LoginView(TokenObtainPairView):
    pass

class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    permission_classes = [IsAuthenticated, IsAdminUserOrReadOnly]

class TournamentViewSet(viewsets.ModelViewSet):
    queryset = Tournament.objects.all()
    serializer_class = TournamentSerializer
    permission_classes = [IsAuthenticated, IsAdminUserOrReadOnly]

    @action(detail=True, methods=['post'])
    def generate_pairings(self, request, pk=None):
        tournament = self.get_object()
        players = list(tournament.players.all())
        round_number = request.data.get('round_number', 1)  # Get the round number from request

        pairings = swiss_pairing(players)
        
        for player1, player2 in pairings:
            Match.objects.create(
                tournament=tournament,
                player1=player1,
                player2=player2,
                round_number=round_number
            )
        
        return Response({'status': 'pairings generated'})

class MatchViewSet(viewsets.ModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer
    permission_classes = [IsAuthenticated, IsAdminUserOrReadOnly]

@api_view(['GET'])
def leaderboard(request, tournament_id):
    tournament = Tournament.objects.get(id=tournament_id)
    players = calculate_leaderboard(tournament)  
    serializer = PlayerSerializer(players, many=True)
    return Response(serializer.data)

