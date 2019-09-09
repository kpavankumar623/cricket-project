from player import Player
import helper as help
import match

player1 = Player("Kirat Boli", prob=[5, 30, 25, 10, 15, 1, 9, 5])
player2 = Player("N.S Nodi", prob=[10, 40, 20, 5, 10, 1, 4, 10])
player3 = Player("R Rumrah", prob=[20, 30, 15, 5, 5, 1, 4, 20])
player4 = Player("Shashi Henra", prob=[30, 25, 5, 0, 5, 1, 4, 30])

mat = match.Match()
score = mat.score
overs = mat.overs
wickets = mat.wickets
balls = mat.balls

# given input data as Constants
BATESMEN = (player1, player2, player3, player4)
WIN_SCORE = 40
WICKETS_MAX = 3
OVERS_MAX = 4
BALLS_IN_OVER = 6
RUN_ODD = (1, 3, 5)

striker = BATESMEN[0] #kirat boli
non_striker = BATESMEN[1]  #N.S Nodi

""" main logic in present in this loop for over by over commentry"""
print('{}.{} Overs Left. {} runs to win.'.format(OVERS_MAX - overs, balls,
                                                 WIN_SCORE - score))

while score <= WIN_SCORE and overs < OVERS_MAX:
        balls = mat.increase_ball()
        striker.increase_ball()
        run_scored = striker.rand_score()

        if run_scored == 'OUT':
            wickets = mat.increase_wicket()
            print('{}.{} {} OUT'.format(overs, balls, striker.name))  # commentry when bates men out

            if wickets >= WICKETS_MAX:
                break
            striker = help.change_batesmen(wickets, BATESMEN)

        else:
            score = mat.increase_score(run_scored)
            striker.increase_runs(run_scored)
            print('{}.{} {} scores {} runs'.format(overs, balls, striker.name, run_scored))  # commentry when bates men scores run

            if run_scored in RUN_ODD or balls == BALLS_IN_OVER:
                striker, non_striker = help.exchange_strike(striker, non_striker)

        if balls == BALLS_IN_OVER:
            overs = mat.increase_over()
            balls = mat.set_zero()
            if overs != OVERS_MAX:
                print('\n{}.{} Overs Left. {} runs to win.'.format(OVERS_MAX - overs, balls, WIN_SCORE - score))  # commentry when over starts

print('\nLengaburu {}-{}({}.{})'.format(score,wickets,overs,balls))
help.cal_winners(score, WIN_SCORE, WICKETS_MAX,wickets)
help.personal_scores(BATESMEN)