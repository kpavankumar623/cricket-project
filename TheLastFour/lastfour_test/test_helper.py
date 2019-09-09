import pytest
from lastfour_main import player
from lastfour_main import helper

player1 = player.Player("Kirat Boli", prob=[5, 30, 25, 10, 15, 1, 9, 5])
player2 = player.Player("N.S Nodi", prob=[10, 40, 20, 5, 10, 1, 4, 10])
player3 = player.Player("R Rumrah", prob=[20, 30, 15, 5, 5, 1, 4, 20])
player4 = player.Player("Shashi Henra", prob=[30, 25, 5, 0, 5, 1, 4, 30])

def test_change_strike():
    striker = player1
    nonstriker = player2
    striker , nonstriker = helper.exchange_strike(striker, nonstriker)
    assert striker.name == "N.S Nodi"

def test_change_batesmen():
    batesmen = [player1,player2,player3,player4]
    wicket = 1
    pla = helper.change_batesmen(wicket,batesmen)
    assert pla.name == 'R Rumrah'