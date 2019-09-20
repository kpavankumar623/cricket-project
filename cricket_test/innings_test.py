import pytest
from lastfour_main import innings

ma = innnigs.Inning
def tet_increase_ball():
   ma.increase_ball()#1
   ma.increase_ball()#2
   assert ma.balls == 2

def test_increase_score():
    ma.increase_score(5)
    assert ma.score == 5

def test_increase_over():
    ma.increase_over()
    assert ma.overs == 1

def test_increase_wicket():
    ma.increase_wicket()
    assert ma.wickets == 1

