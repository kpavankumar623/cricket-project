class MatchRules:

    def __init__(self,WIN_SCORE,WICKETS_MAX,OVERS_MAX):
        self.WIN_SCORE = WIN_SCORE
        self.WICKETS_MAX = WICKETS_MAX
        self.OVERS_MAX = OVERS_MAX

    def stop_condition(self,score,overs,wickets):
        if score >= self.WIN_SCORE or overs >= self.OVERS_MAX or wickets >= self.WICKETS_MAX:
            return True
        else:
            return False

    #this funtion is for printing result of the match.
    def cal_winners(self,score ,wickets):
        """below conditions declare the winner"""
        actual_score = self.WIN_SCORE-1
        if score >= actual_score:
            print("Lengaburu WON by {} wickets".format(self.WICKETS_MAX - wickets))
        elif score == actual_score:
            print("Match DRAWN")
        else:
            print("Enchai WON the Match by {} runs".format(actual_score - score)) #Enchai score is 39.

    #fuction for print personal scores of batesmen
    def personal_scores(self,BATESMEN):
        """loop for print bates men personal score."""
        for batesmen in BATESMEN:
            print(batesmen)