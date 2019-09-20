

def cal_winners(inn,match):
        """below conditions declare the winner"""
        actual_score = match.WIN_SCORE-1
        if inn.score >= actual_score:
            print("Lengaburu WON by {} wickets".format(match.WICKETS_MAX - inn.wickets))
        elif inn.score == actual_score:
            print("Match DRAWN")
        else:
            print("Enchai WON the Match by {} runs".format(actual_score - inn.score)) #Enchai score is 39.
