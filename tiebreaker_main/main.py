import sys
sys.path.append('..')
from player import Player
from innings import Inning
from match_rules import MatchRules
import helper

team1 = "Lengaburu"
team2 = "Enchai"
player1 = Player("Kirat Boli", prob=[5, 10, 25, 10, 25, 1, 14, 10],team=team1)
player2 = Player("N.S Nodi", prob=[5, 15, 15, 10, 20, 1, 19, 15],team=team1)
player3 = Player("DB Vellyers", prob=[5, 10, 25, 10, 25, 1, 14, 10],team=team2)
player4 = Player("H Mamla", prob=[5, 15, 15, 10, 20, 1, 19, 15],team=team2)

#assign players to each team
BATESMEN = {team1:[],team2:[]}
for player in Player.player:
	BATESMEN[player.team].append(player)

#first innings Lengaburu play
first_inn = Inning()
first_inn_rules = MatchRules(36,1,1)#winscore score here is max_score for over
striker = BATESMEN[team1][0]
non_striker = BATESMEN[team1][1]
print(team1 + " innings: ")
helper.play_inning(first_inn,first_inn_rules,striker,non_striker)

#second innings Enchai play
winscore = first_inn.score+1
second_inn = Inning()
second_inn_rules = MatchRules(winscore,1,1)# encahi has target  to reach
striker = BATESMEN[team2][0]
non_striker = BATESMEN[team2][1]
print("\n"+ team2 + " innings: ")
helper.play_inning(second_inn,second_inn_rules,striker,non_striker)

#result and personal score
helper.cal_winner(first_inn,second_inn)
second_inn_rules.personal_scores(BATESMEN)
