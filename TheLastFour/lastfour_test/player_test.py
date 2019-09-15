
import pytest
from lastfour_main import player

player1 = player.Player("Shashi Henra", prob=[30, 25, 5, 0, 5, 1, 4, 30])

run_can_score = [0,1,2,3,4,5,6,"OUT"]

def test_rand_score():
     score = player1.rand_score()
     assert score in run_can_score

def test_increase_ball():
     player1.increase_ball()#1
     player1.increase_ball()#2
     assert player1.balls == 2

def test_increase_runs():
     player1.increase_runs(5)#5
     player1.increase_runs(6)#11
     assert player1.runs == 11