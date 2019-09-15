
def play_inning(inn,match,striker,non_striker):
	BALLS_IN_OVER = 6
	RUN_ODD = (1, 3, 5)
	while match.stop_condition(inn.score,inn.overs,inn.wickets) != True:
	        run_scored = striker.rand_score()

	        if run_scored != 'OUT':
	            striker.increase_score(run_scored)
	            inn.increase_score(run_scored,striker)
	        else:
	            striker.player_out()
	            inn.increase_wicket(striker)
	            break #because only one wicket

	        if inn.balls == BALLS_IN_OVER:
	            break #because only one over

	        if run_scored in RUN_ODD:
	            striker , non_striker = non_striker, striker

def cal_winner(first_inn,second_inn):
	MAX_BALLS_INN = 6
	if first_inn.score < second_inn.score:
		print('\nEnchai Won the match by {} balls remaining.\n'.format(MAX_BALLS_INN - (second_inn.balls)))
	elif first_inn.score > second_inn.score:
		print('\nLengaburu Won the match by {} runs.\n'.format(first_inn.score-second_inn.score))
	else:
		print('\nMatch Draw\n')