
def exchange_strike(stiker, non_stiker):
    """function for exchange striker when odd run comes or over complete"""
    return non_stiker, stiker


def change_batesmen(wicket, BATESMEN):
    """function for changing the bates when strike batesmen get out
    based on wicket we get next bates man if wicket 1 index 2 batesmen comes in to crease"""
    return BATESMEN[wicket+1]

#this function is for printing result of the match.
def cal_winners(score, WIN_SCORE, WICKETS_MAX,wickets):
    """below conditions declare the winner"""
    actual_score = WIN_SCORE-1
    if score >= actual_score:
        print("Lengaburu WON by {} wickets".format(WICKETS_MAX - wickets))
    elif score == actual_score:
        print("Match DRAWN")
    else:
        print("Enchai WON the Match by {} runs".format(actual_score - score)) #Enchai score is 39.

#fuction for print personal scores of batesmen
def personal_scores(BATESMEN):
    """loop for print bates men personal score."""
    for batesmen in BATESMEN:
        print(batesmen)