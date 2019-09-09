class Match:

    def __init__(self, overs=0, score=0, wickets=0, balls=0):
        self.overs = overs
        self.score = score
        self.wickets = wickets
        self.balls = balls

    def increase_ball(self):
        """return over ball count by increasing of one"""
        self.balls += 1
        return self.balls

    def increase_score(self, runs):
        """return score by increasing of runs_scored"""
        self.score += runs
        return self.score

    def increase_over(self):
        """return over by increasing of one"""
        self.overs += 1
        return self.overs

    def increase_wicket(self):
        """return wicket by increasing of one"""
        self.wickets += 1
        return self.wickets
    def set_zero(self):
        """balls set to zero"""
        self.balls = 0
        return 0

