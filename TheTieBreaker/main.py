import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
from TheLastFour.lastfour_main import innings
from TheLastFour.lastfour_main import player
from TheLastFour.lastfour_main import match_rules
import helper

team1 = "Lengaburu"
team2 = "Enchai"
player1 = player.Player("Kirat Boli", prob=[5, 10, 25, 10, 25, 1, 14, 10],team=team1)
player2 = player.Player("N.S Nodi", prob=[5, 15, 15, 10, 20, 1, 19, 15],team=team1)
player3 = player.Player("DB Vellyers", prob=[5, 10, 25, 10, 25, 1, 14, 10],team=team2)
player4 = player.Player("H Mamla", prob=[5, 15, 15, 10, 20, 1, 19, 15],team=team2)

#assign players to each team
players = [player1,player2,player3,player4]
BATESMEN = {team1:[],team2:[]}
for player in players:
	BATESMEN[player.team].append(player)

#first innings Lengaburu play
first_inn = innings.Inning()
first_inn_rules = match_rules.MatchRules(36,1,1)#winscore score here is max_score for over
striker = BATESMEN[team1][0]
non_striker = BATESMEN[team1][1]
print(team1 + " innings: ")
helper.play_inning(first_inn,first_inn_rules,striker,non_striker)

#second innings Enchai play
winscore = first_inn.score+1
second_inn = innings.Inning()
second_inn_rules = match_rules.MatchRules(winscore,1,1)# encahi has target  to reach
striker = BATESMEN[team2][0]
non_striker = BATESMEN[team2][1]
print("\n"+ team2 + " innings: ")
helper.play_inning(second_inn,second_inn_rules,striker,non_striker)

#result and personal score
helper.cal_winner(first_inn,second_inn)
second_inn_rules.personal_scores(BATESMEN)
