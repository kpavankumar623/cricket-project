from player import Player
from innings import Inning
from match_rules import MatchRules

player1 = Player("Kirat Boli", prob=[5, 30, 25, 10, 15, 1, 9, 5])
player2 = Player("N.S Nodi", prob=[10, 40, 20, 5, 10, 1, 4, 10])
player3 = Player("R Rumrah", prob=[20, 30, 15, 5, 5, 1, 4, 20])
player4 = Player("Shashi Henra", prob=[30, 25, 5, 0, 5, 1, 4, 30])

team ="Lengaburu"
players = [player1,player2,player3,player4]
BATEMEN = {team: players}
inn = Inning()
match = MatchRules(40,3,4)

BALLS_IN_OVER = 6
RUN_ODD = (1, 3, 5)


striker = BATEMEN[team][0]
non_striker = BATEMEN[team][1]

print('\n{} overs left, {} runs to win\n'.format(match.OVERS_MAX - inn.overs, match.WIN_SCORE - inn.score))

while match.stop_condition(inn.score,inn.overs,inn.wickets) != True:
    try:
        run_scored = striker.rand_score()

        if run_scored != 'OUT':
            striker.increase_score(run_scored)
            inn.increase_score(run_scored,striker)
        else:
            striker.player_out()
            inn.increase_wicket(striker)
            striker = BATEMEN[team][inn.wickets + 1] #index error if wickets reached max

        if inn.balls == BALLS_IN_OVER:
                inn.increase_over(match.OVERS_MAX,match.WIN_SCORE)

        if inn.balls == BALLS_IN_OVER or run_scored in RUN_ODD:
            striker , non_striker = non_striker, striker
            
    except IndexError:
        break
    except ValueError:
        print("Player Probability of Scoring runs not clear")

print('\nLengaburu {}-{}({}.{})\n'.format(inn.score,inn.wickets,inn.overs,inn.balls))
match.cal_winners(inn.score,inn.wickets)
match.personal_scores(BATEMEN)