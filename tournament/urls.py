from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegisterView, LoginView, PlayerViewSet, TournamentViewSet, MatchViewSet, leaderboard

router = DefaultRouter()
router.register(r'players', PlayerViewSet)
router.register(r'tournaments', TournamentViewSet)
router.register(r'matches', MatchViewSet)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('', include(router.urls)),
    path('leaderboard/<int:tournament_id>/', leaderboard, name='leaderboard'),
]
