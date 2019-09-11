class Inning:

    def __init__(self, overs=0, score=0, wickets=0, balls=0):
        self.overs = overs
        self.score = score
        self.wickets = wickets
        self.balls = balls

    def increase_score(self, runs,striker):
        """return score by increasing of runs_scored and match ball"""
        self.score += runs
        self.balls += 1
        print('{}.{} {} scores {} runs'.format(self.overs, self.balls, striker.name, runs))

    def increase_over(self,OVERS_MAX,WIN_SCORE):
        """return over by increasing of 1"""
        self.balls = 0
        self.overs += 1
        if self.overs < OVERS_MAX:
            print('\n{} overs left, {} runs to win\n'.format(OVERS_MAX - self.overs,WIN_SCORE - self.score))

    def increase_wicket(self, striker):
        """return wicket by increasing of one"""
        self.wickets += 1
        self.balls += 1
        print('{}.{} {} OUT'.format(self.overs, self.balls, striker.name))