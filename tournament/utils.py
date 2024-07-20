from django.db.models import Sum, Case, When, Value, IntegerField

def swiss_pairing(players):
    players.sort(key=lambda x: x.rating, reverse=True)
    pairings = []
    for i in range(0, len(players) - 1, 2):
        pairings.append((players[i], players[i + 1]))
    return pairings


def calculate_leaderboard(tournament):
    players = tournament.players.annotate(
        points=Sum(
            Case(
                When(player1_matches__result='1-0', then=Value(1)),
                When(player2_matches__result='0-1', then=Value(1)),
                When(player1_matches__result='0.5-0.5', then=Value(0.5)),
                When(player2_matches__result='0.5-0.5', then=Value(0.5)),
                default=Value(0),
                output_field=IntegerField(),
            )
        )
    ).order_by('-points')
    return players
