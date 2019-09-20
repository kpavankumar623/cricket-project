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

    #fuction for print personal scores of batesmen
    def personal_scores(self,BATESMEN):
        """loop for print bates men personal score."""
        for team in BATESMEN:
            print("\n"+team)
            for batesmen in BATESMEN[team]:
                print(batesmen)